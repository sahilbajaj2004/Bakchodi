from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set your message and contact name here
CONTACT_NAME = "Friend's Name"  # Change to your contact's name as it appears in WhatsApp
MESSAGE = "Hello from Python!"
REPEAT = 10  # Number of times to send the message

# Path to your ChromeDriver (download from https://chromedriver.chromium.org/downloads)
CHROMEDRIVER_PATH = "chromedriver.exe"  # Ensure chromedriver.exe is in your PATH or provide full path

driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://web.whatsapp.com/")
print("Scan the QR code to log in to WhatsApp Web.")
time.sleep(15)  # Wait for user to scan QR code

# Search for the contact
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(CONTACT_NAME)
time.sleep(2)

# Click on the contact
contact = driver.find_element(By.XPATH, f'//span[@title="{CONTACT_NAME}"]')
contact.click()
time.sleep(2)

# Find the message box and send messages in a loop
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
for i in range(REPEAT):
	message_box.send_keys(MESSAGE)
	message_box.send_keys(Keys.ENTER)
	time.sleep(1)

print(f"Sent '{MESSAGE}' to {CONTACT_NAME} {REPEAT} times.")
driver.quit()
