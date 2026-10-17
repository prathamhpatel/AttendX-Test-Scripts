"""
AttendX - Login Test
Checks that a faculty member can log in with valid credentials and that
invalid / empty credentials are rejected with the correct message.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import login


def test_valid_login(driver):
    login(driver, "faculty01", "Faculty@123")
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    assert "Dashboard" in driver.title


def test_invalid_password(driver):
    login(driver, "faculty01", "wrongpass")
    error = driver.find_element(By.CLASS_NAME, "error-msg").text
    assert error == "Invalid username or password"


def test_empty_fields(driver):
    login(driver, "", "")
    error = driver.find_element(By.CLASS_NAME, "error-msg").text
    assert error == "Username and password are required"
