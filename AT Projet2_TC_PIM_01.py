from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Verify that the username textbox is visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    if username_input.is_displayed():
        print("Username textbox is visible.")
    else:
        print("Username textbox is not visible.")

    # Step 3: Provide the username
    username_input.send_keys("Admin")

    # Wait for the "Forgot your password?" link to be clickable
    forgot_password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='resetPassword']"))
    )

    # Optional: Verify navigation to the reset password page
    reset_password_page = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(), 'Reset Password')]"))
    )

    if reset_password_page.is_displayed():
        print("Navigated to the Reset Password page successfully.")

finally:
    # Close the browser
    driver.quit()
