import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def generate_random_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@example.com"

def fill_registration_form(driver, gender, first_name, last_name, company, email, password):
    wait = WebDriverWait(driver, 10)

    # Select gender
    if gender.lower() == "male":
        driver.find_element(By.ID, "gender-male").click()
    elif gender.lower() == "female":
        driver.find_element(By.ID, "gender-female").click()

    # Fill in the form fields
    wait.until(EC.visibility_of_element_located((By.ID, "FirstName"))).send_keys(first_name)
    wait.until(EC.visibility_of_element_located((By.ID, "LastName"))).send_keys(last_name)
    wait.until(EC.visibility_of_element_located((By.ID, "Email"))).send_keys(email)
    wait.until(EC.visibility_of_element_located((By.ID, "Company"))).send_keys(company)

    # Check the newsletter box
    newsletter_checkbox = wait.until(EC.presence_of_element_located((By.ID, "Newsletter")))
    if not newsletter_checkbox.is_selected():
        newsletter_checkbox.click()

    # Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for password fields and fill them
    wait.until(EC.visibility_of_element_located((By.ID, "Password"))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword"))).send_keys(password)

def login_user(driver, email, password):
    driver.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(1)

    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(2)

def search_product(driver, product_name):
    from selenium.webdriver.common.by import By
    search_input = driver.find_element(By.ID, "small-searchterms")
    search_input.clear()
    search_input.send_keys(product_name)
    driver.find_element(By.CSS_SELECTOR, "button.search-box-button").click()    