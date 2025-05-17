# TC003: Login with Invalid Credentials
import pytest
import time
from selenium.webdriver.common.by import By

def login_user(driver, email, password):
    driver.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(1)

    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(2)

def assert_login_failed(driver):
    error_div = driver.find_element(By.CLASS_NAME, "message-error").text
    assert "Login was unsuccessful" in error_div, f"❌ Expected login failure message, got: {error_div}"
    print("✅ Correct error message shown for invalid login")

def test_login_invalid_credentials(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    valid_email = "shees@example.com"
    valid_password = "shees007"
    invalid_email = "invalid@example.com"
    invalid_password = "WrongPass123"

    try:
        # Case 1a: Invalid email + valid password
        login_user(driver, invalid_email, valid_password)
        assert_login_failed(driver)

        # Navigate back to home before next case
        driver.get("https://demo.nopcommerce.com/")
        time.sleep(1)

        # Case 1b: Valid email + invalid password
        login_user(driver, valid_email, invalid_password)
        assert_login_failed(driver)

        driver.get("https://demo.nopcommerce.com/")
        time.sleep(1)

        # Case 1c: Invalid email + invalid password
        login_user(driver, invalid_email, invalid_password)
        assert_login_failed(driver)

        print("✅ All invalid login cases passed.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_login_invalid_failure.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_login_invalid_failure.png")
        raise e
