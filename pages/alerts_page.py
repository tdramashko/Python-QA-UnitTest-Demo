from playwright.sync_api import Page, Dialog


class AlertsPage:
    """Page Object for DemoQA Alerts, Frames & Windows - Alerts section."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/alerts"
        
        # Locators
        self.simple_alert_button = page.locator("#alertButton")
        self.timer_alert_button = page.locator("#timerAlertButton")
        self.confirm_alert_button = page.locator("#confirmButton")
        self.prompt_alert_button = page.locator("#promtButton")  # Note: typo in demoqa id
        
        # Result message locators
        self.confirm_result = page.locator("#confirmResult")
        self.prompt_result = page.locator("#promptResult")
        
        # Dialog handler storage
        self.dialog_message = None
        self.dialog_type = None
        
    def navigate(self):
        """Navigate to the alerts page."""
        self.page.goto(self.url, wait_until="domcontentloaded")
        
    def click_simple_alert(self):
        """Click button that triggers simple alert."""
        self.simple_alert_button.click()
        
    def click_timer_alert(self):
        """Click button that triggers timed alert (appears after 5 seconds)."""
        self.timer_alert_button.click()
        
    def click_confirm_alert(self):
        """Click button that triggers confirm box."""
        self.confirm_alert_button.click()
        
    def click_prompt_alert(self):
        """Click button that triggers prompt box."""
        self.prompt_alert_button.click()
        
    def get_confirm_result(self) -> str:
        """Get the result message after handling confirm alert."""
        return self.confirm_result.text_content()
        
    def get_prompt_result(self) -> str:
        """Get the result message after handling prompt alert."""
        return self.prompt_result.text_content()
        
    def setup_dialog_handler(self, action: str = "accept", prompt_text: str = None):
        """
        Set up a handler for dialogs.
        
        Args:
            action: 'accept' to click OK, 'dismiss' to click Cancel
            prompt_text: Text to enter in prompt dialog (if applicable)
        """
        def handle_dialog(dialog: Dialog):
            self.dialog_message = dialog.message
            self.dialog_type = dialog.type
            
            if action == "accept":
                if prompt_text and dialog.type == "prompt":
                    dialog.accept(prompt_text)
                else:
                    dialog.accept()
            else:
                dialog.dismiss()
        
        self.page.on("dialog", handle_dialog)
        
    def remove_dialog_handler(self):
        """Remove the dialog handler."""
        self.page.remove_listener("dialog", lambda dialog: None)
        
    def wait_for_alert(self, timeout: int = 10000):
        """Wait for an alert to appear."""
        self.page.wait_for_event("dialog", timeout=timeout)
