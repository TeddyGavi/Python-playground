from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Find the search input field and enter "cats"
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("cats")

# Submit the search query
search_input.submit()

# Wait for search results to load
time.sleep(2)

# Find the URLs of the first 10 search results
result_links = driver.find_elements(By.XPATH, "//div[@class='tF2Cxc']/descendant::a")
result_urls = [link.get_attribute("href") for link in result_links[:10]]

# Write the URLs to a text file
with open("parsed_cats.txt", "w") as file:
    for url in result_urls:
        file.write(url + "\n")

# Close the browser
driver.quit()
