
import time
import method
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
method.driver.get('https://testnet.bybit.com/zh-CN/tradingbot/')
method.driver.maximize_window()
method.driver.implicitly_wait(30)
method.login()

# #首次创建
# driver.find_element(By.CSS_SELECTOR,'._3qVRMTaiCTxNkwMRL62_ee._18N7vvAqcg4gp2TvpsTyA-').click()
# time.sleep(2)
# method.create()

#已有机器人创建
method.driver.find_element(By.CSS_SELECTOR,'._3qVRMTaiCTxNkwMRL62_ee._2HUsEQ-QURXsT8vr_3R7_t').click()
time.sleep(2)
method.create()

# #跟单1日榜第一
# method.copy()

# #我的机器人-详情-挂单-套利
# method.running_bot()

# #设置不可跟单
# method.follow()

#关闭机器人
method.close()
