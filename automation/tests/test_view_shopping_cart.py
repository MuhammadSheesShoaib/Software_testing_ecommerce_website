# TC008: View Shopping Cart
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_shopping_cart(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Navigate to category and add product to cart
        driver.find_element(By.LINK_TEXT, "Computers").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Notebooks").click()
        time.sleep(2)

        product = driver.find_element(By.XPATH, "(//h2[@class='product-title']/a)[1]")
        product_name = product.text
        product.click()
        time.sleep(2)

        driver.find_element(By.ID, "add-to-cart-button-4").click()
        time.sleep(3)

        # Wait for notification to disappear (max 10 seconds)
        notification = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "bar-notification"))
        )

        # Step 2: Click on 'Shopping cart' at top
        cart_link = driver.find_element(By.CLASS_NAME, "cart-label")
        cart_link.click()
        time.sleep(2)

        # Step 3: Assert that product is displayed in cart
        cart_items = driver.find_elements(By.CLASS_NAME, "product-name")
        assert any(product_name in item.text for item in cart_items), \
            f"❌ Expected product '{product_name}' not found in cart."

        print(f"✅ Test passed — '{product_name}' is displayed in shopping cart.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_view_shopping_cart.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_view_shopping_cart.png")
        raise e
