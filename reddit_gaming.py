from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
from collections import Counter

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("https://www.reddit.com/r/gaming/")
wait = WebDriverWait(driver, 20)

get_texts = ""
last_height = driver.execute_script("return document.body.scrollHeight")
SCROLL_PAUSE_TIME = 0.5
all_txt = ""


while(True):
    

    ##DRIVER 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    time.sleep(3)

    redditText = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".text-16")))
    for text in redditText:
        if text.text:
            all_text= "".join(text.text)
            all_txt += all_text + "\n"
            print(all_txt)

with open("rgaming.txt", "w", encoding="utf-8") as file:
    file.write(all_txt)

"""counter = Counter(file.split())
for t in counter.most_common(10):
    get_texts = t[0]"""