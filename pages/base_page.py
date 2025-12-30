"""Base Page class for all page objects"""

from playwright.sync_api import Page, expect
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, page: Page, base_url: str = "https://staging.workflowpro.com"):
        """
        Initialize the base page
        
        Args:
            page: Playwright page object
            base_url: Base URL for the application
        """
        self.page = page
        self.base_url = base_url
        self.timeout = 30000
    
    def navigate(self, url: str):
        """Navigate to a URL"""
        full_url = url if url.startswith('http') else f"{self.base_url}{url}"
        logger.info(f"Navigating to {full_url}")
        self.page.goto(full_url)
    
    def click(self, selector: str):
        """Click an element"""
        logger.info(f"Clicking element: {selector}")
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill input field"""
        logger.info(f"Filling {selector} with text: {text}")
        self.page.fill(selector, text)
    
    def type_text(self, selector: str, text: str):
        """Type text character by character"""
        logger.info(f"Typing in {selector}: {text}")
        self.page.locator(selector).type(text)
    
    def get_text(self, selector: str) -> str:
        """Get text from element"""
        text = self.page.locator(selector).text_content()
        logger.info(f"Got text from {selector}: {text}")
        return text
    
    def is_visible(self, selector: str, timeout: Optional[int] = None) -> bool:
        """Check if element is visible"""
        try:
            self.page.locator(selector).is_visible(timeout=timeout or self.timeout)
            return True
        except:
            return False
    
    def wait_for_element(self, selector: str, timeout: Optional[int] = None):
        """Wait for element to be visible"""
        logger.info(f"Waiting for element: {selector}")
        self.page.locator(selector).wait_for(timeout=timeout or self.timeout)
    
    def wait_for_navigation(self):
        """Wait for page navigation"""
        logger.info("Waiting for page navigation")
        self.page.wait_for_load_state("networkidle")
    
    def take_screenshot(self, filename: str):
        """Take a screenshot"""
        logger.info(f"Taking screenshot: {filename}")
        self.page.screenshot(path=filename)
    
    def close(self):
        """Close the page"""
        logger.info("Closing page")
        self.page.close()
