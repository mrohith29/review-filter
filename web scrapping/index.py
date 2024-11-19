from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

chrome_options = Options()

chrome_driver_path = r"C:\Users\mariy\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.amazon.in/Starshine-Storage-Powered-MediaTek-Display/product-reviews/B0CMTZNPXR/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1')

driver.implicitly_wait(10)

with open('reviews.txt', 'w', encoding='utf-8') as file:

    while True:
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        review_divs = soup.find_all('div', {'data-hook': 'review'})

        for review in review_divs:
            review_text = review.find('span', {'data-hook': 'review-body'}).get_text(strip=True)
            file.write(review_text + '\n')

        action = ActionChains(driver)
        action.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)  # Adjust time as needed

        try:
            next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
            if next_button:
                next_button.click()
                time.sleep(2)  # Wait for the next page to load
            else:
                break  # No more pages
        except Exception as e:
            break  # No more pages or other issue

driver.quit()