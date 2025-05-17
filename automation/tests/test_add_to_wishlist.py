# TC015: Add Product to Wishlist
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_wishlist(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Login
        driver.find_element(By.LINK_TEXT, "Log in").click()
        
        # Wait for and fill login form
        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_field.send_keys("shees@example.com")  # Use valid email
        
        password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_field.send_keys("shees007")  # Use valid password
        
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
        login_button.click()

        # Step 2: Go to product page
        books_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books")))
        books_link.click()
        
        book = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "First Prize Pies")))
        book.click()

        # Step 3: Click "Add to wishlist"
        wishlist_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-wishlist button")))
        wishlist_button.click()

        # Step 4: Assert success message
        notification = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification")))
        assert "The product has been added to your wishlist" in notification.text, \
            f"❌ Wishlist confirmation not shown. Got: '{notification.text}'"

        print("✅ Test passed — Product added to wishlist.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_add_to_wishlist.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_add_to_wishlist.png")
        raise e
