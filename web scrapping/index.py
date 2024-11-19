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

urls = ['https://www.amazon.in/Samsung-Inches-Smart-UA43T5450AKXXL-Black/dp/B0BFFHGML2/ref=sr_1_4?crid=27C6SF3A99DF0&dib=eyJ2IjoiMSJ9.MTT3fIvC-gXLOgfeBDB7RLy2PW_ABcGhNOcz3LciOTsj5sMxNcHyAknPy2CHjAKzRx8fvmuLifPanc-4_9lRbMn_XnyTzpzyHBvbeFWVqoYVPAi8uCNUENm8XC_QLZuMhai3RPDS1L6SNPgAvvnCCh605XHHPrjMPZX-j-dihYK8sUhztv2Sbwj7B-KRhLRV7LXd3w64i38kTIiAZ0Z7XFHX0Jqbbyl6eDCTPhseqR0.Bn92FwiBl3XLQ6_RASkUJytM-vOM0oGH0Qu0Y0et8ZQ&dib_tag=se&keywords=television%2B43%2Binch%2Bsmart%2Btv&qid=1732016851&sprefix=television%2Caps%2C239&sr=8-4&th=1',
        'https://www.amazon.in/Starshine-Storage-Powered-MediaTek-Display/product-reviews/B0CMTZNPXR/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

with open('reviews.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        driver.get(url)
        driver.implicitly_wait(70)
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