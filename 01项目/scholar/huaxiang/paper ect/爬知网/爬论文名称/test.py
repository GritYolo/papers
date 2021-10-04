'测试用'
import requests
import json
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import urllib
import time
import os
from lxml import etree
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
web = webdriver.Chrome(options=option)
# web = webdriver.Chrome()
url='https://kns.cnki.net/KNS8/AdvSearch?dbcode=SCDB'





nn = 0

name = '王建勇'
filename = './test/'+name+'.txt'




s = requests.session()
s.keep_alive = False  # 关闭多余连接
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
# web = webdriver.Chrome(options=option)
# web = webdriver.Chrome(options=option)
web = webdriver.Chrome()
url = 'https://kns.cnki.net/KNS8/AdvSearch?dbcode=SCDB'
#打开知网
web.get(url)
WebDriverWait(web, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/input'))
)
# #print(name+' error' +'打开知网错误')Y

# try:
# 输入信息
WebDriverWait(web, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/input'))
)
web.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/input').click()

web.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/input').send_keys(name)
WebDriverWait(web, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input'))
)
time.sleep(2)
web.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input').click()



#点击机构
WebDriverWait(web, 10).until(
EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/dl[7]/dt/b'))
)
# except:
#     #print(name+' error' +'输入信息检索错误')
#     continue

# try:

#点击机构
web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/dl[7]/dt/b').click()


# 鼠标移动到机构，显示出隐藏列表
# WebDriverWait(web, 10).until(
#     EC.visibility_of_element_located(
#         (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/dl[7]/dd/div/ul[1]/li[1]/a'))
# )
WebDriverWait(web, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/dl[7]/dd/div/ul[1]/li[1]/a'))
)
t1 = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/dl[7]/dd/div/ul[1]/li[1]/a')
time.sleep(1)
actions = ActionChains(web)
actions.move_to_element(t1)
actions.perform()
#清华大学勾选框
t2 = web.find_element_by_xpath('//a[@title="清华大学"]')
t22= web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/dl[5]/dt/b')
#确定范围
t3 = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/a[1]')
actions = ActionChains(web)
actions.move_to_element(t1)
actions.perform()

actions = ActionChains(web)
actions.move_to_element(t2)
actions.click(t2)
actions.perform()

actions = ActionChains(web)
actions.move_to_element(t22)
actions.click(t22)
actions.perform()


actions = ActionChains(web)
actions.move_to_element(t3)
actions.click(t3)
actions.perform()
time.sleep(4)
# except:
#print(name+' error' +'选择范围错误')


# try:
# 全选框点击
WebDriverWait(web, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input'))
)
web.find_element_by_xpath(
    '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input').click()
# except:
#print(name + ' error' + '全选错误')

# try:
#翻页
page_text=web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[2]/span[1]').get_attribute('textContent')
import re

k = re.findall(r'\d', page_text)
ss = ''.join(k)
# #print(pattern.findall(pages)[1])
page_num = int(ss)
WebDriverWait(web, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//a[@id="PageNext"]'))
)
for i in range(0,page_num-1):

    web.find_element_by_xpath('//a[@id="PageNext"]').click()
    time.sleep(2)
    # 点击全选
    WebDriverWait(web, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input'))
    )
    web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input').click()
#print("kkk")


# except:
#print(name+' error'+"翻页错误")

# try:
# 导出文献格式
first = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/ul[1]/li[2]/a')
second = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/ul[1]/li[2]/ul/li[1]/a')
target = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/ul[1]/li[2]/ul/li[1]/ul/li[1]/a')


actions = ActionChains(web)
actions.move_to_element(first)
actions.move_to_element(second)
actions.click(target)
actions.perform()

web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/a[1]').click()
time.sleep(5)
# except:
#print(name+' error' +'导出文献错误')


# try:
#获取当前页柄
global h
h = web.current_window_handle
all_h=web.window_handles
web.switch_to.window(all_h[1])
WebDriverWait(web, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="result"]/ul'))
        )
content = web.find_element_by_xpath('//*[@id="result"]/ul')
# #print(content.text)
# except:
#print(name + '  error!'+'提取文献错误')

# try:
with open(filename,'w',encoding='utf-8') as f:
    f.write(content.text)
# except:
#print(name + '  error!'+'文件保存错误')



# try:
web.close()
web.switch_to.window(h)
web.close()
#print(name + '  done!')
# except:
#print(name + '  error!'+'关闭页面错误')


    # web.close()
    #
    # web.switch_to.window()
    # web.close()
#print("yes")