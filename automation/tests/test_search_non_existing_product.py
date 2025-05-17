# TC006: Search for Non-Existing Product
import pytest
import time
from selenium.webdriver.common.by import By
from utils.helpers import search_product

def test_search_non_existing_product(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Search for a non-existing product
        search_product(driver, "xyz123nonexistentitem")

        # Step 2: Wait for result
        time.sleep(2)

        # Step 3: Assertion – Verify the "no products found" message appears
        message = driver.find_element(By.CLASS_NAME, "no-result").text
        assert message == "No products were found that matched your criteria.", \
            f"❌ Unexpected message: {message}"

        print("✅ Test passed — Proper message displayed for non-existing product.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_search_non_existing_product.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_search_non_existing_product.png")
        raise e
