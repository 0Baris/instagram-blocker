from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_block_list_from_file(filename="block_list.txt"):
    """
    Engellenicek kullanıcıları txt dosyasından okur ve listeye aktarır.
    Args:
        filename (str): Dosya adı.
    """
    try:
        with open(filename, 'r') as file:
            return tuple(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"'{filename}' doesn't exists.")
        return tuple()

def block_accounts(username,password,block_list):
    """
    Selenium ile otomatik instagram engelleme aracı.
    Args:
        username (str): İnstagram kullanıcı adı.
        password (str): İnstagram şifresi.
        block_list (tuple): Engellenmesi istenen kullanıcıların listesi.
    """
    wait = time.sleep

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options) 
    driver.set_window_size(1600, 900)

    url = "https://www.instagram.com/"

    driver.get(url)

    try: 
        driver.find_element
        instagram_username = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input') 
        instagram_username.send_keys(username)
        wait(5)

        instagram_password =  driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input') 
        instagram_password.send_keys(password)
        wait(5)

        login_button = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        wait(15)

        for account in block_list:
            try:
                driver.get(f"https://www.instagram.com/{account}/")
                wait(10)

                options = driver.find_element(By.CSS_SELECTOR, 'svg[class*="x1lliihq"] circle[cx="18"]')
                options.click()
                wait(5)

                block_button = driver.find_element(By.XPATH, value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div/button[1]')
                block_button.click()
                wait(5)

                block_sure_button = driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/button[1]')
                block_sure_button.click()
                wait(5)

                print(f"*{account}* isimli hesap engellendi.")
                wait(35)

            except:
                print(f"*{account}* Hesap önceden engellenmiş olabilir, Sonraki hesaba geçiliyor.")
                continue

        print("""
            
Tüm kullanıcılar engellendi, Github üzerinden bana yıldız bırakarak destek olabilir misin?

https://github.com/0Baris/instagram-blocker

        """)

        driver.close()

    except:
        print("Kullanıcı bilgileriniz doğru değil!")
        driver.close()
