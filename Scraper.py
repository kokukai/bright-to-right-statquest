import time
import csv
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

def scrape(channel_id='statquest'):
    options = ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)


    driver.get(f"https://www.youtube.com/@{channel_id}/videos")

    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    container = driver.find_element(By.ID, 'contents')
    videos_blocks = container.find_elements(By.TAG_NAME, 'ytd-rich-grid-row')

    # Open a CSV file in write mode
    with open('video_titles.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Title"])

        for block in videos_blocks:
            videos = block.find_elements(By.TAG_NAME, 'ytd-rich-item-renderer')
            for video in videos:
                title = video.find_element(By.TAG_NAME, 'h3').text
                # Write the title to the CSV file
                writer.writerow([title])

    driver.quit()
