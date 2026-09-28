from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os
import time


def test_ecommerce_purchase():

    # Read test data
    with open("test_data/test_data.json", "r") as file:
        test_data = json.load(file)

    email = test_data["email"]
    password = test_data["password"]
    product = test_data["product"]
    quantity = test_data["quantity"]

    os.makedirs("screenshots", exist_ok=True)

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
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
        ).send_keys(email)

        driver.find_element(
            By.ID, "input-password"
        ).send_keys(password)

        driver.find_element(
            By.XPATH, "//input[@value='Login']"
        ).click()

        time.sleep(3)

        driver.save_screenshot(
            "screenshots/01_login.png"
        )

        # Search product
        search_box = driver.find_element(
            By.NAME, "search"
        )

        search_box.send_keys(product)

        driver.find_element(
            By.CSS_SELECTOR,
            "button.btn.btn-default.btn-lg"
        ).click()

        time.sleep(3)

        driver.save_screenshot(
            "screenshots/02_product_search.png"
        )

        # Add product
        driver.find_element(
            By.CSS_SELECTOR,
            "button[onclick*='cart.add']"
        ).click()

        time.sleep(3)

        driver.save_screenshot(
            "screenshots/03_product_added.png"
        )

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
        quantity_box.send_keys(quantity)

        driver.find_element(
            By.XPATH,
            "//button[@type='submit' and contains(@data-original-title, 'Update')]"
        ).click()

        time.sleep(3)

        # Verify quantity
        actual_quantity = driver.find_element(
            By.CSS_SELECTOR,
            "input[name^='quantity']"
        ).get_attribute("value")

        assert actual_quantity == quantity

        driver.save_screenshot(
            "screenshots/04_final_cart.png"
        )

    finally:
        driver.quit()