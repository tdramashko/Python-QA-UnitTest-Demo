from playwright.sync_api import Page, ViewportSize


class ResponsivePage:
    """Page Object for responsive design testing across different screen sizes."""

    # Common viewport sizes
    VIEWPORTS = {
        "mobile_small": {"width": 375, "height": 667},      # iPhone SE
        "mobile_medium": {"width": 390, "height": 844},     # iPhone 12/13
        "mobile_large": {"width": 414, "height": 896},      # iPhone 11 Pro Max
        "tablet_portrait": {"width": 768, "height": 1024},  # iPad
        "tablet_landscape": {"width": 1024, "height": 768}, # iPad landscape
        "laptop": {"width": 1366, "height": 768},           # Common laptop
        "laptop_large": {"width": 1440, "height": 900},     # MacBook Pro
        "desktop": {"width": 1920, "height": 1080},         # Full HD
        "desktop_large": {"width": 2560, "height": 1440},   # 2K display
    }

    def __init__(self, page: Page):
        self.page = page
        self.text_box_url = "https://demoqa.com/text-box"
        self.buttons_url = "https://demoqa.com/buttons"
        
    def set_viewport(self, device_type: str):
        """Set viewport size for a specific device type."""
        if device_type not in self.VIEWPORTS:
            raise ValueError(f"Unknown device type: {device_type}")
        
        viewport = self.VIEWPORTS[device_type]
        self.page.set_viewport_size(viewport)
        
    def get_viewport_size(self) -> ViewportSize:
        """Get current viewport size."""
        return self.page.viewport_size
        
    def navigate_to_text_box(self):
        """Navigate to text box page."""
        self.page.goto(self.text_box_url, wait_until="domcontentloaded")

    def navigate_to_buttons(self):
        """Navigate to buttons page."""
        self.page.goto(self.buttons_url, wait_until="domcontentloaded")
        """Check if element is visible in viewport."""
        element = self.page.locator(selector)
        return element.is_visible()
        
    def get_element_size(self, selector: str) -> dict:
        """Get element dimensions."""
        return self.page.locator(selector).bounding_box()
        
    def check_mobile_menu_visible(self) -> bool:
        """Check if mobile menu/hamburger is visible."""
        # DemoQA may have mobile navigation elements
        mobile_menu = self.page.locator(".header-wrapper, .mobile-menu, [class*='menu']").first
        return mobile_menu.is_visible() if mobile_menu.count() > 0 else False
        
    def get_computed_style(self, selector: str, property: str) -> str:
        """Get computed CSS property value for an element."""
        return self.page.evaluate(f"""(selector) => {{
            const el = document.querySelector(selector);
            return window.getComputedStyle(el).getPropertyValue('{property}');
        }}""", selector)
        
    def check_responsive_layout(self) -> dict:
        """Check various layout characteristics for responsive design."""
        return self.page.evaluate("""() => {
            const body = document.body;
            const container = document.querySelector('.container, .main-header, .text-center');
            
            return {
                bodyWidth: body.offsetWidth,
                containerWidth: container ? container.offsetWidth : null,
                scrollWidth: document.documentElement.scrollWidth,
                hasHorizontalScroll: document.documentElement.scrollWidth > window.innerWidth,
                viewportWidth: window.innerWidth,
                viewportHeight: window.innerHeight
            };
        }""")
        
    def take_screenshot(self, filename: str):
        """Take screenshot of current page."""
        self.page.screenshot(path=f"screenshots/{filename}")
