from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://web.whatsapp.com")

def start():
    my_latest_num = 0

    while(True):
        rows = driver.find_elements(By.XPATH, "//*[@role='row']")
        texts = []
        for row in rows:
            try:
                texts += row.text.split("\n")

            except Exception:
                pass

        found_number = False
        i = 1
        while (not found_number):
            try:
                num = texts[-i]
                num = int(num) + 1
                found_number = True

            except Exception:
                i += 1
                found_number = False
                if (i > len(texts)):
                    print("Fatal error, exiting...")
                    raise KeyboardInterrupt
                    break


        if num > my_latest_num + 1:
            keyboard = driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
            keyboard.send_keys(int(num))
            keyboard.send_keys(Keys.RETURN)
            my_latest_num = num

input("Please press Enter after you log in to whatsapp and enter the group...")
start()