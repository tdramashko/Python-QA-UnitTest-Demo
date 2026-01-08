from playwright.sync_api import Page


class AccessibilityPage:
    """Page Object for DemoQA accessibility testing."""

    def __init__(self, page: Page):
        self.page = page
        self.text_box_url = "https://demoqa.com/text-box"
        self.buttons_url = "https://demoqa.com/buttons"
        
    def navigate_to_text_box(self):
        """Navigate to the text box page."""
        self.page.goto(self.text_box_url, wait_until="domcontentloaded")
        
    def navigate_to_buttons(self):
        """Navigate to the buttons page."""
        self.page.goto(self.buttons_url, wait_until="domcontentloaded")
        
    def check_aria_labels(self, element_selector: str) -> dict:
        """Check aria attributes for an element."""
        element = self.page.locator(element_selector)
        return {
            "aria-label": element.get_attribute("aria-label"),
            "role": element.get_attribute("role"),
            "aria-required": element.get_attribute("aria-required"),
        }
        
    def get_semantic_structure(self) -> dict:
        """Get semantic HTML structure information."""
        return self.page.evaluate("""() => {
            return {
                hasMain: !!document.querySelector('main, [role="main"]'),
                hasHeader: !!document.querySelector('header, [role="banner"]'),
                hasNav: !!document.querySelector('nav, [role="navigation"]'),
                buttonCount: document.querySelectorAll('button').length,
                inputCount: document.querySelectorAll('input').length
            };
        }""")
        
    def keyboard_navigation_test(self, start_element: str, tab_count: int):
        """Test keyboard navigation by tabbing through elements."""
        self.page.locator(start_element).focus()
        for _ in range(tab_count):
            self.page.keyboard.press("Tab")
        return self.page.evaluate("document.activeElement.id")
        
    def check_color_contrast(self, element_selector: str) -> dict:
        """Check color contrast for text elements."""
        element = self.page.locator(element_selector)
        return self.page.evaluate("""(selector) => {
            const el = document.querySelector(selector);
            const style = window.getComputedStyle(el);
            return {
                color: style.color,
                backgroundColor: style.backgroundColor,
                fontSize: style.fontSize
            };
        }""", element_selector)
        
    def check_form_labels(self, input_id: str) -> dict:
        """Check if form inputs have proper labels."""
        return self.page.evaluate("""(id) => {
            const input = document.getElementById(id);
            const label = document.querySelector(`label[for="${id}"]`);
            return {
                hasLabel: !!label,
                labelText: label ? label.textContent : null,
                hasPlaceholder: !!input.getAttribute('placeholder'),
                placeholderText: input.getAttribute('placeholder')
            };
        }""", input_id)
