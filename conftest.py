import pytest
from playwright.sync_api import Page, BrowserContext


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    # Set default timeout to 60 seconds for flaky demoqa.com
    page.set_default_timeout(60000)
    # Set default navigation timeout to 90 seconds
    page.set_default_navigation_timeout(90000)
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context settings."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(page: Page, request):
    """Take screenshot on test failure."""
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        try:
            screenshot_path = f"screenshots/{request.node.name}.png"
            page.screenshot(path=screenshot_path, timeout=5000)
            print(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")


def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot fixture."""
    if call.when == "call":
        item.rep_call = call
