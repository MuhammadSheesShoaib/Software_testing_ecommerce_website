# TC019: Change Currency to Euro
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_change_currency_to_euro(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.nopcommerce.com/")
    
    try:
        # Step 1: Change currency to Euro on homepage
        currency_text = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='customerCurrency']/option[contains(text(),'US Dollar')]")))
        currency_text.click()
        
        currency_dropdown = Select(driver.find_element(By.ID, "customerCurrency"))
        currency_dropdown.select_by_visible_text("Euro")
        
        # Wait for homepage prices to update to Euro
        def euro_prices_present(driver):
            try:
                prices = driver.find_elements(By.CSS_SELECTOR, ".prices .price")
                return any("€" in price.text for price in prices)
            except:
                return False
                
        wait.until(euro_prices_present)
        print("✓ Currency changed to Euro on homepage")
        
        # Step 2: Navigate to Books category
        books_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books")))
        books_link.click()
        
        # Step 3: Click on a specific book
        book_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "First Prize Pies")))
        book_link.click()
        
        # Step 4: Verify product price is in Euros
        product_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.price-value-37, .product-price")))
        price_text = product_price.text
        
        print("Product price:", price_text)
        assert "€" in price_text, f"❌ Product price not in Euros. Got: {price_text}"

        print("✅ Test passed — Product price shown in Euros:", price_text)

    except Exception as e:
        driver.save_screenshot("screenshots/test_change_currency_to_euro.png")
        print("❌ Test failed. Screenshot saved at screenshots/test_change_currency_to_euro.png")
        raise e
