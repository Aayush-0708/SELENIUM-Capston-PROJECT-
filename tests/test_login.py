from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json


def handle_alert():
    try:
        alert = driver.switch_to.alert
        print("Alert found:", alert.text)
        alert.accept()
        print("Alert accepted")
    except:
        print("No alert found")


# Read JSON
with open("test_data/test_data.json", "r") as file:
    test_data = json.load(file)

EMAIL = test_data["email"]
PASSWORD = test_data["password"]
PRODUCT = test_data["product"]
QUANTITY = test_data["quantity"]

os.makedirs("screenshots", exist_ok=True)

driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)

# Login
driver.find_element(
    By.XPATH, "//span[text()='My Account']"
).click()

driver.find_element(
    By.LINK_TEXT, "Login"
).click()

time.sleep(2)

driver.find_element(
    By.ID, "input-email"
).send_keys(EMAIL)

driver.find_element(
    By.ID, "input-password"
).send_keys(PASSWORD)

driver.find_element(
    By.XPATH, "//input[@value='Login']"
).click()

time.sleep(3)

# Search
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys(PRODUCT)

driver.find_element(
    By.CSS_SELECTOR,
    "button.btn.btn-default.btn-lg"
).click()

time.sleep(3)

# Add to cart
driver.find_element(
    By.CSS_SELECTOR,
    "button[onclick*='cart.add']"
).click()

time.sleep(2)

# Handle popup/alert if available
handle_alert()

# Open cart
driver.find_element(
    By.LINK_TEXT, "Shopping Cart"
).click()

time.sleep(3)

# Update quantity
quantity_box = driver.find_element(
    By.CSS_SELECTOR,
    "input[name^='quantity']"
)

quantity_box.clear()
quantity_box.send_keys(QUANTITY)

driver.find_element(
    By.XPATH,
    "//button[@type='submit' and contains(@data-original-title, 'Update')]"
).click()

time.sleep(3)

# Verify
actual_quantity = driver.find_element(
    By.CSS_SELECTOR,
    "input[name^='quantity']"
).get_attribute("value")

if actual_quantity == QUANTITY:
    print("PASS: Cart quantity verified successfully")
else:
    print("FAIL: Cart quantity verification failed")

driver.save_screenshot(
    "screenshots/04_final_cart.png"
)

driver.quit()

print("Automation completed successfully")