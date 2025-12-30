"""Test data generators and utilities"""

from faker import Faker

fake = Faker()


class TestData:
    """Generate test data"""
    
    @staticmethod
    def get_random_email() -> str:
        """Generate random email"""
        return fake.email()
    
    @staticmethod
    def get_random_name() -> str:
        """Generate random name"""
        return fake.name()
    
    @staticmethod
    def get_random_password(length: int = 12) -> str:
        """Generate random password"""
        return fake.password(length=length)
    
    @staticmethod
    def get_random_phone() -> str:
        """Generate random phone number"""
        return fake.phone_number()
    
    @staticmethod
    def get_random_address() -> str:
        """Generate random address"""
        return fake.address()
    
    @staticmethod
    def get_random_company() -> str:
        """Generate random company name"""
        return fake.company()
