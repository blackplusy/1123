#coding=utf-8
from selenium import webdriver
br=webdriver.Chrome()
#1.打开网页
br.get("http://ecshop.test1.shopex123.com/user.php")
#2.点击用户名输入框
br.find_element_by_name("username").click()
#3.清空用户名输入框
br.find_element_by_name("username").clear()
#4.输入用户名信息
br.find_element_by_name("username").send_keys("林志玲")
#5.点击密码输入框
br.find_element_by_name("password").click()
#6.清空密码输入框
br.find_element_by_name("password").clear()
#7.输入密码信息
br.find_element_by_name("password").send_keys("123456")
#8.点击登录
br.find_element_by_name("submit").click()

