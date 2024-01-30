from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (replace 'chrome' with 'firefox' or 'edge' for other browsers)
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.example.com")

# Find an element by its ID and interact with it
# element = driver.find_element_by_id("some_id")
# element.click()

# Find an element by its name and input text
# element = driver.find_element_by_name("some_name")
# element.send_keys("Some text")

# Close the browser
# driver.close()
