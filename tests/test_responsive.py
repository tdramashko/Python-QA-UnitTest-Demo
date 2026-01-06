import pytest
from playwright.sync_api import Page, expect
from pages.responsive_page import ResponsivePage


class TestResponsiveDesign:
    """Tests for responsive design across different screen resolutions."""

    def test_mobile_small_viewport(self, page: Page):
        """Test layout on small mobile device (iPhone SE - 375x667)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("mobile_small")
        responsive_page.navigate_to_text_box()
        
        # Verify viewport size
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 375
        assert viewport["height"] == 667
        
        # Check no horizontal scroll
        layout = responsive_page.check_responsive_layout()
        assert not layout["hasHorizontalScroll"], "Should not have horizontal scroll on mobile"

    def test_mobile_medium_viewport(self, page: Page):
        """Test layout on medium mobile device (iPhone 12/13 - 390x844)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("mobile_medium")
        responsive_page.navigate_to_buttons()
        
        # Verify viewport
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 390
        
        # Check buttons are visible
        assert responsive_page.is_element_visible("#doubleClickBtn")
        assert responsive_page.is_element_visible("#rightClickBtn")

    def test_tablet_portrait_viewport(self, page: Page):
        """Test layout on tablet in portrait mode (iPad - 768x1024)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("tablet_portrait")
        responsive_page.navigate_to_text_box()
        
        # Verify viewport
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 768
        assert viewport["height"] == 1024
        
        # Check form elements are visible
        assert responsive_page.is_element_visible("#userName")
        assert responsive_page.is_element_visible("#userEmail")

    def test_tablet_landscape_viewport(self, page: Page):
        """Test layout on tablet in landscape mode (1024x768)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("tablet_landscape")
        responsive_page.navigate_to_text_box()
        
        # Verify viewport
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 1024
        
        # Check layout adapts properly
        layout = responsive_page.check_responsive_layout()
        assert layout["viewportWidth"] == 1024

    def test_laptop_viewport(self, page: Page):
        """Test layout on common laptop screen (1366x768)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("laptop")
        responsive_page.navigate_to_buttons()
        
        # Verify viewport
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 1366
        assert viewport["height"] == 768
        
        # Check all buttons visible
        buttons = page.locator("button").all()
        assert len(buttons) >= 3, "All buttons should be visible on laptop"

    def test_desktop_full_hd_viewport(self, page: Page):
        """Test layout on Full HD desktop (1920x1080)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("desktop")
        responsive_page.navigate_to_text_box()
        
        # Verify viewport
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 1920
        assert viewport["height"] == 1080
        
        # Check layout utilizes space properly
        layout = responsive_page.check_responsive_layout()
        assert layout["viewportWidth"] == 1920

    def test_desktop_2k_viewport(self, page: Page):
        """Test layout on 2K desktop (2560x1440)."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport("desktop_large")
        responsive_page.navigate_to_buttons()
        
        # Verify viewport
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == 2560
        assert viewport["height"] == 1440
        
        # Verify no horizontal scroll on large screens
        layout = responsive_page.check_responsive_layout()
        assert not layout["hasHorizontalScroll"]

    @pytest.mark.parametrize("device_type", [
        "mobile_small",
        "mobile_medium", 
        "tablet_portrait",
        "laptop",
        "desktop"
    ])
    def test_form_accessibility_across_devices(self, page: Page, device_type: str):
        """Test that form remains accessible across different device sizes."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport(device_type)
        responsive_page.navigate_to_text_box()
        
        # All form inputs should be visible and accessible
        assert responsive_page.is_element_visible("#userName")
        assert responsive_page.is_element_visible("#userEmail")
        assert responsive_page.is_element_visible("#submit")
        
        # Form should be usable
        page.locator("#userName").fill("Test User")
        page.locator("#userEmail").fill("test@example.com")
        
        # Submit button should be clickable
        submit_btn = page.locator("#submit")
        expect(submit_btn).to_be_enabled()

    @pytest.mark.parametrize("device_type,width,height", [
        ("mobile_small", 375, 667),
        ("tablet_portrait", 768, 1024),
        ("laptop", 1366, 768),
        ("desktop", 1920, 1080),
    ])
    def test_viewport_dimensions(self, page: Page, device_type: str, width: int, height: int):
        """Verify viewport dimensions are set correctly for each device type."""
        responsive_page = ResponsivePage(page)
        responsive_page.set_viewport(device_type)
        
        viewport = responsive_page.get_viewport_size()
        assert viewport["width"] == width, f"Width should be {width} for {device_type}"
        assert viewport["height"] == height, f"Height should be {height} for {device_type}"

    def test_responsive_content_layout(self, page: Page):
        """Test content layout adapts from mobile to desktop."""
        responsive_page = ResponsivePage(page)
        
        # Test mobile layout
        responsive_page.set_viewport("mobile_small")
        responsive_page.navigate_to_text_box()
        mobile_layout = responsive_page.check_responsive_layout()
        
        # Test desktop layout
        responsive_page.set_viewport("desktop")
        responsive_page.navigate_to_text_box()
        desktop_layout = responsive_page.check_responsive_layout()
        
        # Desktop should have wider viewport
        assert desktop_layout["viewportWidth"] > mobile_layout["viewportWidth"]
        
        # Both should not have horizontal scroll
        assert not mobile_layout["hasHorizontalScroll"]
        assert not desktop_layout["hasHorizontalScroll"]
