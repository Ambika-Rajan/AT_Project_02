from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Launch the URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Log in as Admin
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Admin")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Step 3: Navigate to Admin page
    admin_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']"))
    )
    admin_menu.click()

    # Step 4: Validate the title of the page
    expected_title = "OrangeHRM"
    actual_title = driver.title
    if actual_title == expected_title:
        print(f"Title validation passed: {actual_title}")
    else:
        print(f"Title validation failed: expected '{expected_title}', got '{actual_title}'")

    # Step 5: Validate the options are displayed on Admin page
    options = [
        "User Management",
        "Job",
        "Organization",
        "Qualifications",
        "Nationalities",
        "Corporate Banking",
        "Configuration"
    ]

    for option in options:
        try:
            option_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, option))
            )
            print(f"'{option}' is displayed on the Admin page.")
        except Exception as e:
            print(f"'{option}' is NOT displayed on the Admin page.")

finally:
    # Close the browser
    driver.quit()
