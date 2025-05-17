# TC013: Checkout with Registered User
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_with_registered_user(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.nopcommerce.com/")
    
    try:
        # Step 1: Click Login
        driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(1)

        # Step 2: Enter valid login credentials
        driver.find_element(By.ID, "Email").send_keys("shees@example.com")  # Replace with a valid registered email
        driver.find_element(By.ID, "Password").send_keys("shees007")  # Replace with the correct password
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(2)

        # Step 3: Navigate to product category and add product
        driver.find_element(By.LINK_TEXT, "Computers").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Notebooks").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//h2[@class='product-title']/a)[1]").click()
        time.sleep(2)

        driver.find_element(By.ID, "add-to-cart-button-4").click()
        time.sleep(2)

        # Wait for notification to disappear
        wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "bar-notification"))
        )

        # Step 4: Click Shopping Cart icon
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-label")))
        cart_button.click()
        time.sleep(2)

        # Step 5: Agree to terms and click Checkout
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(3)

        # Step 6: Assertion – verify form prefilled (e.g., email shown)
        email_field = driver.find_element(By.ID, "BillingNewAddress_Email")
        assert email_field.get_attribute("value") != "", "❌ Email field is empty, form not prefilled."

        print("✅ Test passed — Checkout form prefilled for registered user.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_checkout_registered_user.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_checkout_registered_user.png")
        raise e
