# TC004: Logout User
import pytest
import time
from selenium.webdriver.common.by import By
from utils.helpers import login_user

def test_logout_user(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Login first
        login_user(driver, "shees@example.com", "shees007")

        # Step 2: Click Logout
        time.sleep(2)
        logout_link = driver.find_element(By.LINK_TEXT, "Log out")
        logout_link.click()
        time.sleep(2)

        # Step 3: Assertion – "Log in" should reappear, "Log out" should disappear
        assert driver.find_element(By.LINK_TEXT, "Log in").is_displayed(), "❌ Log in link not visible after logout"
        assert not any("Log out" in el.text for el in driver.find_elements(By.LINK_TEXT, "Log out")), "❌ Still showing 'Log out' after clicking"

        print("✅ Logout successful — redirected to homepage")

    except Exception as e:
        driver.save_screenshot("screenshots/test_logout_failure.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_logout_failure.png")
        raise e
