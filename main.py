from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Instantiate the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Load the target page
captcha_page_url = "https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php"
driver.get(captcha_page_url)

# Solve the Captcha
print("Solving Captcha")
solver = TwoCaptcha("2CAPTCHA_API_KEY")
response = solver.recaptcha(sitekey='SITE_KEY', url=captcha_page_url)
code = response['code']
print(f"Successfully solved the Captcha. The solve code is {code}")

# Set the solved Captcha
recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response')
driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

# Submit the form
submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn.click()

# Pause the execution so you can see the screen after submission before closing the driver
input("Press enter to continue")
driver.close()

