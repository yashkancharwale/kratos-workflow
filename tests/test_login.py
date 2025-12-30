"""Login tests"""

import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData
import logging

logger = logging.getLogger(__name__)


@pytest.mark.smoke
def test_successful_login(page, credentials):
    """Test successful login"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    
    # Get credentials
    user = credentials['test_users']['admin']
    
    # Perform login
    login_page.login(user['email'], user['password'])
    
    # Verify login was successful (adjust selector based on your app)
    page.wait_for_url("**/dashboard")
    assert "/dashboard" in page.url
    logger.info("Login successful")


@pytest.mark.smoke
def test_login_with_invalid_credentials(page, credentials):
    """Test login with invalid credentials"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    
    # Attempt login with invalid credentials
    login_page.login("invalid@example.com", "wrongpassword")
    
    # Verify error is displayed
    assert login_page.is_error_displayed()
    error_msg = login_page.get_error_message()
    assert "Invalid" in error_msg or "incorrect" in error_msg.lower()
    logger.info("Invalid credentials error displayed correctly")


@pytest.mark.smoke
def test_login_with_empty_email(page):
    """Test login with empty email"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    
    # Try to submit without email
    login_page.fill(login_page.PASSWORD_INPUT, "password123")
    login_page.click(login_page.LOGIN_BUTTON)
    
    # Verify error is displayed
    assert login_page.is_error_displayed()
    logger.info("Empty email validation working")


@pytest.mark.smoke
def test_login_with_remember_me(page, credentials):
    """Test login with remember me"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    
    # Get credentials
    user = credentials['test_users']['admin']
    
    # Login with remember me
    login_page.login_with_remember_me(user['email'], user['password'])
    
    # Verify login was successful
    page.wait_for_url("**/dashboard")
    assert "/dashboard" in page.url
    logger.info("Remember me login successful")


@pytest.mark.regression
def test_forgot_password_link(page):
    """Test forgot password link navigation"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    
    # Click forgot password link
    login_page.click_forgot_password()
    
    # Verify navigation
    assert "/forgot-password" in page.url
    logger.info("Forgot password navigation successful")


@pytest.mark.regression
def test_signup_link(page):
    """Test signup link navigation"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    
    # Click signup link
    login_page.click_signup()
    
    # Verify navigation
    assert "/signup" in page.url
    logger.info("Signup navigation successful")
