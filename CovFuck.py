import time
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://authserver.nwu.edu.cn/authserver/login?service=https%3A%2F%2Fapp.nwu.edu.cn%2Fa_nwu%2Fapi%2Fsso%2Fcas%3Fredirect%3Dhttps%253A%252F%252Fapp.nwu.edu.cn%252Fsite%252Fncov%252Fdailyup%26from%3Dwap")
account_field = browser.find_element_by_name("username")
password_filed = browser.find_element_by_id('password')
account_field.send_keys('2018103399')#填写账号
password_filed.send_keys('******')#填写密码
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[1]/form/p[6]/button').click()
time.sleep(10)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[4]/div/input').click()
time.sleep(10)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[5]').click()
time.sleep(10)
browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]').click()
browser.quit()
