# TC007: Add Product to Cart
import pytest
import time
from selenium.webdriver.common.by import By

def test_add_product_to_cart(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Navigate to 'Computers > Notebooks' category
        driver.find_element(By.LINK_TEXT, "Computers").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Notebooks").click()
        time.sleep(2)

        # Step 2: Choose a product (e.g., first one in list)
        product = driver.find_element(By.XPATH, "(//h2[@class='product-title']/a)[1]")
        product_name = product.text
        product.click()
        time.sleep(2)

        # Step 3: Click 'Add to cart'
        driver.find_element(By.ID, "add-to-cart-button-4").click()  # ID may differ per product
        time.sleep(3)

        # Step 4: Assert confirmation message
        confirmation = driver.find_element(By.CLASS_NAME, "bar-notification").text
        assert "The product has been added to your shopping cart" in confirmation, \
            f"❌ Product not added to cart, got message: {confirmation}"

        print(f"✅ Test passed — '{product_name}' successfully added to cart.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_add_product_to_cart.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_add_product_to_cart.png")
        raise e
