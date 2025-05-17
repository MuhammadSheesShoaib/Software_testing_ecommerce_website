# TC014: Submit Product Review
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_submit_product_review(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Log in as registered user
        driver.find_element(By.LINK_TEXT, "Log in").click()
        
        # Wait for and fill login form
        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_field.send_keys("shees@example.com")  # Replace with valid user
        
        password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_field.send_keys("shees007")  # Replace with valid password
        
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
        login_button.click()
        time.sleep(2)

        # Step 2: Navigate to any product
        driver.find_element(By.LINK_TEXT, "Books").click()
        time.sleep(2)
        
        # Wait for and click on specific book
        book_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "First Prize Pies")))
        book_link.click()
        time.sleep(2)

        # Step 3: Click 'Add your review'
        review_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add your review")))
        review_link.click()
        time.sleep(2)

        # Step 4: Fill review form
        title_field = wait.until(EC.presence_of_element_located((By.ID, "AddProductReview_Title")))
        title_field.send_keys("Excellent Book")
        
        review_text = wait.until(EC.presence_of_element_located((By.ID, "AddProductReview_ReviewText")))
        review_text.send_keys("Very informative and well written.")
        
        rating = wait.until(EC.element_to_be_clickable((By.ID, "addproductrating_4")))
        rating.click()
        time.sleep(1)

        # Step 5: Submit review
        submit_button = wait.until(EC.element_to_be_clickable((By.NAME, "add-review")))
        submit_button.click()

        # Step 6: Assertion — Wait for and verify confirmation message
        notification = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification")))
        assert "Product review is successfully added." in notification.text, \
            f"❌ Expected review confirmation message, got: {notification.text}"

        print("✅ Test passed — Product review submitted successfully.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_submit_product_review.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_submit_product_review.png")
        raise e
