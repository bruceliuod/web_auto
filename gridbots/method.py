
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
driver = webdriver.Chrome(service=Service("./bruce/bot_webauto/drivers/chromedriver.exe"))

#未登录时点击创建跳转登录
def login():
    driver.find_element(By.CSS_SELECTOR,'._3qVRMTaiCTxNkwMRL62_ee._18N7vvAqcg4gp2TvpsTyA-').click()
    frame=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/iframe')))
    driver.switch_to.frame(frame)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/div/div/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/input').send_keys('autouser1_sgp@snapmail.cc')
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/div/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/input').send_keys('Admin123456@@@')
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/a').click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

#创建BTCUSDT机器人
def create():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[4]/div[1]/div[1]/input').send_keys('40000')
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[4]/div[3]/div[1]/input').send_keys('50000')
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[6]/input').send_keys('13')
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[10]/input').send_keys('260')
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[3]/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    time.sleep(2)

#跟单1日榜第一
def copy():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div[4]/input').send_keys('500')
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[3]/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    time.sleep(2)

#我的机器人-详情-挂单-套利
def running_bot():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/ul/li[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/ul/li[3]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    time.sleep(2)

#设置不允许跟单
def follow():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    time.sleep(2)

#以close_mode 1 关闭机器人
def close():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/button[2]/span').click()
    driver.find_element(By.CSS_SELECTOR,'._3qVRMTaiCTxNkwMRL62_ee._4vx0Oa-Rl9yQujnDMwZ27').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/a').click()
    time.sleep(2)