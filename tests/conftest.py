"""Pytest configuration and fixtures"""

import pytest
from playwright.sync_api import sync_playwright
import logging
from utils.config_reader import ConfigReader
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config():
    """Load configuration"""
    config_dir = os.path.join(os.path.dirname(__file__), "..", "config")
    return ConfigReader.get_env_config(config_dir)


@pytest.fixture(scope="session")
def credentials():
    """Load credentials"""
    config_dir = os.path.join(os.path.dirname(__file__), "..", "config")
    return ConfigReader.get_credentials(config_dir)


@pytest.fixture(scope="session")
def tenants():
    """Load tenants configuration"""
    config_dir = os.path.join(os.path.dirname(__file__), "..", "config")
    return ConfigReader.get_tenants(config_dir)


@pytest.fixture
def browser():
    """Create a browser instance for each test"""
    playwright = sync_playwright().start()
    config = ConfigReader.get_env_config()
    
    # Create browser based on configuration
    browser_type = getattr(playwright, config.get('browser', 'chromium'))
    browser = browser_type.launch(headless=config.get('headless', False))
    
    logger.info(f"Browser launched: {config.get('browser', 'chromium')}")
    
    yield browser
    
    browser.close()
    playwright.stop()
    logger.info("Browser closed")


@pytest.fixture
def page(browser, config):
    """Create a page for each test"""
    page = browser.new_page(
        viewport={
            "width": config.get('viewport_width', 1920),
            "height": config.get('viewport_height', 1080)
        }
    )
    page.set_default_timeout(config.get('timeout', 30000))
    
    logger.info("New page created")
    
    yield page
    
    # Take screenshot on failure
    if hasattr(page, 'context'):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=f"{screenshots_dir}/screenshot_{timestamp}.png")
    
    page.close()
    logger.info("Page closed")


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--env", action="store", default="staging",
        help="Environment to run tests against"
    )


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "smoke: Mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: Mark test as regression test"
    )
