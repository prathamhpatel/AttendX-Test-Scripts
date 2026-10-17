"""
AttendX - Attendance Marking Test
A logged-in faculty member selects a class and subject, marks students
Present / Absent and saves. Saving without selecting a class must fail.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from conftest import BASE_URL, login


def open_attendance_page(driver):
    login(driver, "faculty01", "Faculty@123")
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    driver.get(f"{BASE_URL}/attendance")


def test_mark_attendance(driver):
    open_attendance_page(driver)
    Select(driver.find_element(By.ID, "class-select")).select_by_visible_text("CE-7A")
    Select(driver.find_element(By.ID, "subject-select")).select_by_visible_text("Software Testing")
    driver.find_element(By.ID, "load-students").click()

    rows = driver.find_elements(By.CSS_SELECTOR, "table#students tbody tr")
    assert len(rows) > 1, "Student list did not load"

    # First student Present, second student Absent
    rows[0].find_element(By.CSS_SELECTOR, "input[value='P']").click()
    rows[1].find_element(By.CSS_SELECTOR, "input[value='A']").click()
    driver.find_element(By.ID, "save-attendance").click()

    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "success-msg"))
    )
    assert "Attendance saved" in msg.text


def test_save_without_class_selected(driver):
    open_attendance_page(driver)
    driver.find_element(By.ID, "save-attendance").click()
    error = driver.find_element(By.CLASS_NAME, "error-msg").text
    assert error == "Please select a class and subject"
