import time
import method
from method import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver.get('https://testnet.bybit.com/zh-CN/tradingbot/')
method.login()

#首次创建
driver.find_element(By.CSS_SELECTOR,'._3qVRMTaiCTxNkwMRL62_ee._18N7vvAqcg4gp2TvpsTyA-').click()
time.sleep(3)
method.create()

#已有机器人创建
driver.find_element(By.CSS_SELECTOR,'._3qVRMTaiCTxNkwMRL62_ee._2HUsEQ-QURXsT8vr_3R7_t').click()
time.sleep(3)
method.create()

#跟单1日榜第一
driver.get('https://testnet.bybit.com/zh-CN/tradingbot/')
method.copy()

