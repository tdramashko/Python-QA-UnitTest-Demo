from playwright.sync_api import Page


class WebTablesPage:
    """Page Object for DemoQA Web Tables page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/webtables"
        
        # Locators
        self.add_button = page.locator("#addNewRecordButton")
        self.search_box = page.locator("#searchBox")
        self.table = page.locator(".rt-table")
        self.table_rows = page.locator(".rt-tbody .rt-tr-group")
        
        # Registration form locators
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#userEmail")
        self.age_input = page.locator("#age")
        self.salary_input = page.locator("#salary")
        self.department_input = page.locator("#department")
        self.submit_button = page.locator("#submit")
        
    def navigate(self):
        """Navigate to the web tables page."""
        self.page.goto(self.url, wait_until="domcontentloaded")
        
    def click_add_button(self):
        """Click the add new record button."""
        self.add_button.click()
        
    def fill_registration_form(self, first_name: str, last_name: str, email: str, 
                               age: str, salary: str, department: str):
        """Fill out the registration form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.age_input.fill(age)
        self.salary_input.fill(salary)
        self.department_input.fill(department)
        
    def submit_form(self):
        """Submit the registration form."""
        self.submit_button.click()
        
    def search(self, search_text: str):
        """Search for a record in the table."""
        self.search_box.fill(search_text)
        
    def get_table_row_count(self) -> int:
        """Get the number of rows with data in the table."""
        count = 0
        for row in self.table_rows.all():
            # Check if row has any text content
            if row.text_content().strip():
                count += 1
        return count
        
    def delete_row(self, row_index: int):
        """Delete a specific row by index (0-based)."""
        delete_button = self.page.locator(f".rt-tbody .rt-tr-group:nth-child({row_index + 1}) #delete-record-{row_index + 1}")
        delete_button.click()
        
    def edit_row(self, row_index: int):
        """Edit a specific row by index (0-based)."""
        edit_button = self.page.locator(f".rt-tbody .rt-tr-group:nth-child({row_index + 1}) #edit-record-{row_index + 1}")
        edit_button.click()
