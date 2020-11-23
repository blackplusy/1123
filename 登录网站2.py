#coding=utf-8
from selenium import webdriver
br=webdriver.Chrome()
#1.定义信息函数
#leixing 有2类参数，一个是用户名(username) 一个是密码(password)
def info(leixing,msg):
    br.find_element_by_name(leixing).click()
    br.find_element_by_name(leixing).clear()
    br.find_element_by_name(leixing).send_keys(msg)

#2.打开网页
br.get("http://ecshop.test1.shopex123.com/user.php")
#3.调用info函数，写入用户名信息
info('username','林志玲')
#4.调用info函数，写入密码信息
info('password','123456')
#5.点击登录
br.find_element_by_name("submit").click()
