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
s = requests.session()

s.keep_alive = False # 关闭多余连接
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
# web = webdriver.Chrome(options=option)
web = webdriver.Chrome()
url='https://kns.cnki.net/KNS8/AdvSearch?dbcode=SCDB'


def is_exit_xpath(xpath):
    try:
        web.find_element_by_xpath(xpath)
        return True
    except:
        return False

with open('person.txt',encoding='utf-8') as f:
    plist = f.read().splitlines()
nn = 0
for person  in plist:
    name = person
    filename = './GB/'+name+'.txt'
        #文件存在且有内容则跳过
    if os.path.exists(filename) and os.path.getsize(filename)!=0:
        continue

    try:
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
    except:
        print(name+' error' +'打开知网错误')

    try:
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



    except:
        print(name+' error' +'输入信息检索错误')
        continue

    try:


        time.sleep(2)
        xpath1= '//a[@title="清华大学"]'
        # 点击机构
        WebDriverWait(web, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/dl[7]/dt/b'))
        )
        web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/dl[7]/dt/b').click()
        WebDriverWait(web, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath1))
        )
        if  not is_exit_xpath(xpath1):
            print("此人现不属于清华机构")
            with open(filename,'w',encoding='utf-8') as f:
                f.write('此人现不属于清华机构')
            continue
        else:



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

            #定位清华大学勾选框
            t2 = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/dl[7]/dd//a[@title="清华大学"]')


            #定位机构项上方的学科项
            t22= web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/dl[5]/dt/b')
            #确定按钮
            t3 = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/a[1]')

            # 鼠标移动到机构列表里第一个机构，显示出下拉隐藏列表
            actions = ActionChains(web)
            actions.move_to_element(t1)
            actions.perform()

            #鼠标移动到清华大学勾选框并点击
            actions = ActionChains(web)
            actions.move_to_element(t2)
            actions.click(t2)
            actions.perform()

            #鼠标移动到学科项，关闭隐藏列表，准备点击确定按钮
            actions = ActionChains(web)
            actions.move_to_element(t22)
            actions.click(t22)
            actions.perform()
            # 点击确定按钮
            actions = ActionChains(web)
            actions.move_to_element(t3)
            actions.click(t3)
            actions.perform()
            time.sleep(4)
    except:
        print(name+' error' +'选择范围错误')
        continue

    try:
        # 全选框点击
        WebDriverWait(web, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input'))
        )
        web.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input').click()
    except:
        print(name + ' error' + '全选错误')
        continue

    try:
        #翻页
        if is_exit_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[2]/span[1]'):

            page_text=web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[2]/span[1]').get_attribute('textContent')
            import re

            k = re.findall(r'\d', page_text)
            ss = ''.join(k)
            # print(pattern.findall(pages)[1])
            page_num = int(ss)
            WebDriverWait(web, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//a[@id="PageNext"]'))
            )
            for i in range(0,page_num-1):
                xpath2 = '//a[@id="PageNext"]'
                if is_exit_xpath(xpath2):

                    web.find_element_by_xpath('//a[@id="PageNext"]').click()
                    time.sleep(2)
                    # 点击全选
                    WebDriverWait(web, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input'))
                    )
                    web.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label/input').click()
                else:
                    1
        else:
            1

    except:
        print(name+' error'+"翻页错误")
        continue

    try:
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
    except:
        print(name+' error' +'导出文献错误')
        continue


    try:
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
        # print(content.text)
    except:
        print(name + '  error!'+'提取文献错误')
        continue

    try:
        with open(filename,'w',encoding='utf-8') as f:
            f.write(content.text)
    except:
        print(name + '  error!'+'文件保存错误')
        continue



    try:
        web.close()
        web.switch_to.window(h)
        web.close()
        print(name + '  done!')
    except:
        print(name + '  error!'+'关闭页面错误')
        continue


    # web.close()
    #
    # web.switch_to.window()
    # web.close()
print("yes")