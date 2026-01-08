from playwright.sync_api import Page


class ButtonsPage:
    """Page Object for DemoQA Buttons page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/buttons"
        
        # Locators
        self.double_click_button = page.locator("#doubleClickBtn")
        self.right_click_button = page.locator("#rightClickBtn")
        self.click_me_button = page.get_by_role("button", name="Click Me", exact=True)
        
        # Message locators
        self.double_click_message = page.locator("#doubleClickMessage")
        self.right_click_message = page.locator("#rightClickMessage")
        self.dynamic_click_message = page.locator("#dynamicClickMessage")
        
    def navigate(self):
        """Navigate to the buttons page."""
        self.page.goto(self.url, wait_until="domcontentloaded")
        
    def double_click(self):
        """Perform double click on the double click button."""
        self.double_click_button.dblclick()
        
    def right_click(self):
        """Perform right click on the right click button."""
        self.right_click_button.click(button="right")
        
    def single_click(self):
        """Perform single click on the click me button."""
        self.click_me_button.click()
        
    def get_double_click_message(self) -> str:
        """Get double click message text."""
        return self.double_click_message.text_content()
        
    def get_right_click_message(self) -> str:
        """Get right click message text."""
        return self.right_click_message.text_content()
        
    def get_dynamic_click_message(self) -> str:
        """Get dynamic click message text."""
        return self.dynamic_click_message.text_content()
