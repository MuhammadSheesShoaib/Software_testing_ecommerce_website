# TC020: Filter by Category
import pytest
import time
from selenium.webdriver.common.by import By

def test_filter_by_category_shoes(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")
    try:
        # Step 1: Click on "Apparel"
        driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']/li/a[contains(text(),'Apparel')]").click()
        time.sleep(2)

        # Step 2: Click on "Shoes" category
        driver.find_element(By.LINK_TEXT, "Shoes").click()
        time.sleep(2)

        # Step 3: Assertion – Check title or breadcrumb
        page_title = driver.title
        breadcrumb = driver.find_element(By.CLASS_NAME, "page-title").text

        assert "Shoes" in page_title or "Shoes" in breadcrumb, \
            f"❌ Expected to land on Shoes page, but title was '{page_title}' and breadcrumb was '{breadcrumb}'"

        print("✅ Test passed — Filtered to Shoes category successfully.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_filter_by_category_failure.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_filter_by_category_failure.png")
        raise e
