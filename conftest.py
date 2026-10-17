"""
Shared pytest fixtures for the AttendX test suite.
The browser fixture and login helper are used by every test file.
"""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# AttendX staging URL - override with:  export ATTENDX_URL=http://<host>:<port>
BASE_URL = os.getenv("ATTENDX_URL", "http://localhost:8080")


@pytest.fixture
def driver():
    """Start a fresh Chrome session for each test and close it afterwards."""
    drv = webdriver.Chrome()
    drv.maximize_window()
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


def login(driver, username, password):
    """Open the AttendX login page and submit the given credentials."""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()
