# TC009: Remove Product from Cart
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_remove_product_from_cart(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Navigate to Books and add product to cart
        driver.find_element(By.LINK_TEXT, "Books").click()
        time.sleep(1)

        # Find and click on "First Prize Pies" book
        product = driver.find_element(By.XPATH, "//h2[@class='product-title']/a[contains(text(), 'First Prize Pies')]")
        product_name = product.text
        product.click()
        time.sleep(2)

        # Wait for and click the add to cart button (using a more general selector)
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='add-to-cart-button']"))
        )
        add_to_cart_button.click()
        time.sleep(3)

        # Wait for notification to disappear (max 10 seconds)
        notification = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "bar-notification"))
        )

        # Step 2: Click on 'Shopping cart' at top
        cart_link = driver.find_element(By.CLASS_NAME, "cart-label")
        cart_link.click()
        time.sleep(2)

        # Step 3: Verify product is in cart
        cart_items = driver.find_elements(By.CLASS_NAME, "product-name")
        assert any(product_name in item.text for item in cart_items), \
            f"❌ Expected product '{product_name}' not found in cart."

        # Step 4: Click the remove button (X)
        remove_button = driver.find_element(By.CLASS_NAME, "remove-btn")
        remove_button.click()
        time.sleep(2)

        # Step 5: Assert cart is empty
        cart_msg = driver.find_element(By.CLASS_NAME, "order-summary-content").text
        assert "Your Shopping Cart is empty!" in cart_msg, \
            f"❌ Cart not empty. Message: {cart_msg}"

        print("✅ Test passed — Product removed, cart is now empty.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_remove_product_from_cart.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_remove_product_from_cart.png")
        print(f"Error details: {str(e)}")
        raise e
