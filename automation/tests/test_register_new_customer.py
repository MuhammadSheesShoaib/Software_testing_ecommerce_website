# TC001: Register New Customer
import pytest
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import generate_random_email, fill_registration_form
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ---------- Fixture using undetected-chromedriver ----------
@pytest.fixture
def setup():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114 Safari/537.36")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()


# ---------- Test Case ----------
def test_register_new_customer(setup):
    driver = setup
    wait = WebDriverWait(driver, 20)  # Increased wait time to 20 seconds
    
    try:
        # Step 1: Navigate to site and click Register
        driver.get("https://demo.nopcommerce.com/")
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        
        # Step 2: Generate test data
        email = "shees@example.com"
        password = "shees007"

        # Step 3: Fill registration form
        fill_registration_form(
            driver,
            gender="male",
            first_name="Shees",
            last_name="Shoaib",
            company="Unburden",
            email=email,
            password=password
        )

        # Step 4: Handle CAPTCHA if present
        try:
            captcha_frame = wait.until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]"))
            )
            driver.switch_to.frame(captcha_frame)
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))
            ).click()
            driver.switch_to.default_content()
        except TimeoutException:
            print("⚠️ CAPTCHA not found or skipped")

        # Step 5: Submit registration
        register_button = wait.until(
            EC.element_to_be_clickable((By.ID, "register-button"))
        )
        register_button.click()

        # Step 6: Verify success message
        try:
            result_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "result"))
            )
            success_message = result_element.text.strip()
            assert "Your registration completed" in success_message, \
                f"❌ Expected 'Your registration completed', got '{success_message}'"
            
            # Step 7: Click continue
            continue_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.register-continue-button"))
            )
            continue_button.click()
            
            print(f"✅ Test passed — Account created with email: {email}")
            
        except (TimeoutException, NoSuchElementException) as e:
            print(f"❌ Failed to verify registration success: {str(e)}")
            raise

    except Exception as e:
        driver.save_screenshot("screenshots/test_register_failure.png")
        print(f"❌ Test failed. Error: {str(e)}")
        print("Screenshot saved at screenshots/test_register_failure.png")
        raise
    
    
