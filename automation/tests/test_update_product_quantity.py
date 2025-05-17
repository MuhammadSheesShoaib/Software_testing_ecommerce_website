# TC010: Update Product Quantity in Cart
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_update_product_quantity_in_cart(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.nopcommerce.com/")

    try:
        # Step 1: Add a product to cart
        driver.find_element(By.LINK_TEXT, "Books").click()
        time.sleep(1)

        # Find and click on "First Prize Pies" book
        product = driver.find_element(By.XPATH, "//h2[@class='product-title']/a[contains(text(), 'First Prize Pies')]")
        product.click()
        time.sleep(2)

        # Wait for and click the add to cart button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='add-to-cart-button']"))
        )
        add_to_cart_button.click()
        time.sleep(3)

        # Wait for notification to disappear
        wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "bar-notification"))
        )

        # Step 2: Go to cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-label")))
        cart_button.click()

        # Step 3: Update quantity - wait for cart page to load and find elements
        quantity_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "qty-input")))
        current_quantity = int(quantity_input.get_attribute("value"))
        new_quantity = current_quantity + 1

        # Focus on the input field
        actions = ActionChains(driver)
        actions.move_to_element(quantity_input).click().perform()
        time.sleep(1)

        # Select all text and delete it
        quantity_input.send_keys(Keys.CONTROL + "a")
        quantity_input.send_keys(Keys.DELETE)
        time.sleep(1)

        # Type the new value and press Enter to confirm
        quantity_input.send_keys(str(new_quantity))
        quantity_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # Verify the quantity was updated
        updated_quantity = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "qty-input")))
        final_value = updated_quantity.get_attribute("value")
        assert final_value == str(new_quantity), \
            f"❌ Expected quantity '{new_quantity}', got '{final_value}'"

        print("✅ Test passed — Product quantity updated in cart.")

    except Exception as e:
        driver.save_screenshot("screenshots/test_update_product_quantity.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_update_product_quantity.png")
        raise e
