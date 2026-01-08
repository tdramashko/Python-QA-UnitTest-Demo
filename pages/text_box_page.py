from playwright.sync_api import Page


class TextBoxPage:
    """Page Object for DemoQA Text Box page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/text-box"
        
        # Locators
        self.full_name_input = page.locator("#userName")
        self.email_input = page.locator("#userEmail")
        self.current_address_input = page.locator("#currentAddress")
        self.permanent_address_input = page.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output_section = page.locator("#output")
        
    def navigate(self):
        """Navigate to the text box page."""
        self.page.goto(self.url, wait_until="domcontentloaded")
        
    def fill_form(self, full_name: str, email: str, current_address: str, permanent_address: str):
        """Fill out the text box form."""
        self.full_name_input.fill(full_name)
        self.email_input.fill(email)
        self.current_address_input.fill(current_address)
        self.permanent_address_input.fill(permanent_address)
        
    def submit(self):
        """Click the submit button."""
        self.submit_button.click()
        
    def get_output_text(self) -> str:
        """Get the output section text."""
        return self.output_section.text_content()
