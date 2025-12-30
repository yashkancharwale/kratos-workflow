"""Login Page Object"""

from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Login page object"""
    
    # Selectors
    EMAIL_INPUT = "input[type='email']"
    PASSWORD_INPUT = "input[type='password']"
    LOGIN_BUTTON = "button:has-text('Sign In')"
    ERROR_MESSAGE = ".error-message"
    FORGOT_PASSWORD_LINK = "a:has-text('Forgot Password')"
    SIGNUP_LINK = "a:has-text('Sign Up')"
    REMEMBER_ME_CHECKBOX = "input[type='checkbox']"
    
    def __init__(self, page):
        super().__init__(page)
    
    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate("/login")
        self.wait_for_element(self.EMAIL_INPUT)
    
    def login(self, email: str, password: str):
        """Perform login"""
        logger.info(f"Attempting login with email: {email}")
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_navigation()
    
    def login_with_remember_me(self, email: str, password: str):
        """Login with remember me checked"""
        logger.info(f"Attempting login with remember me: {email}")
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.REMEMBER_ME_CHECKBOX)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_navigation()
    
    def get_error_message(self) -> str:
        """Get error message"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def click_forgot_password(self):
        """Click forgot password link"""
        self.click(self.FORGOT_PASSWORD_LINK)
        self.wait_for_navigation()
    
    def click_signup(self):
        """Click signup link"""
        self.click(self.SIGNUP_LINK)
        self.wait_for_navigation()
