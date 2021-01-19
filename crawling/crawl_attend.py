import requests
from selenium import webdriver
import time

# set the chrome driver
options=webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('—disable-dev-shm-usage')
options.add_argument('—single-process')
options.add_argument('—no-sandbox')
options.add_argument("—remote-debugging-port=9222")
driver=webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)
driver.implicitly_wait(3)
driver.get('http://eknu.champstudy.com/index.html?b2b=Y')
# lms login page
driver.find_element_by_name('id').send_keys('니학번')
driver.find_element_by_name('pw').send_keys('니학번')
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/a/img').click()
print('login success')
driver.find_element_by_xpath('//*[@id="layer2"]/div/div[2]/div/div[1]/table/tbody/tr[5]/td/a/img').click()
print('into subpage')
while True:
    w=4 #아예 한번도 수강 안햇을경우 w=4, 두번째 챕터부터하려면 w=7
    while True:
        try:
            driver.find_element_by_css_selector('#layer1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(10) > td > table > tbody > tr:nth-child(%s) > td:nth-child(8) > a > img' %w).click()
            print('into list page')
            w+=3
            try:
                m=4
                while True:
                    try:
                        driver.find_element_by_css_selector('#layer1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(9) > td > table > tbody > tr:nth-child(%s) > td:nth-child(6) > a > img' %m).click()
                        time.sleep(8)
                        print('attend')
                        driver.switch_to.window(driver.window_handles[1])
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        m+=2
                    except:
                        break
                driver.back()
            except:
                driver.quit()
        except:
            driver.quit()
            break
