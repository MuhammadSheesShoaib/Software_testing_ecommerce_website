# TC002: Login with Valid Credentials
import pytest
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# ---------- Helper Function ----------
def login_user(driver, email, password):
    driver.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(1)

    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(3)

# ---------- Fixture Setup using undetected-chromedriver ----------
@pytest.fixture
def setup():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114 Safari/537.36")

    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()

# ---------- Test Case ----------
def test_login_with_valid_credentials(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    # Replace with a valid email/password you've registered
    valid_email = "shees@example.com"
    valid_password = "shees007"

    try:
        login_user(driver, valid_email, valid_password)

        # Assertion: Check if logout link is displayed (means logged in)
        logout_button = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed(), "❌ Log out button not visible. Login might have failed."

        print(f"✅ Login successful for user: {valid_email}")

    except Exception as e:
        # Screenshot on failure
        driver.save_screenshot("screenshots/test_login_failure.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_login_failure.png")
        raise e
