# TC005: Search for Existing Product
import pytest
import time
from selenium.webdriver.common.by import By
from utils.helpers import search_product

def test_search_existing_product(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Search for a known product
        search_product(driver, "First Prize Pies")

        # Step 2: Wait for results
        time.sleep(2)

        # Step 3: Assertion – Check product list contains expected item(s)
        product_titles = driver.find_elements(By.CSS_SELECTOR, ".product-title a")
        assert any("First Prize Pies" in title.text for title in product_titles), \
            "❌ Product 'First Prize Pies' not found in search results"

        print("✅ Product search successful — 'First Prize Pies' found in results.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_search_failure.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_search_failure.png")
        raise e
