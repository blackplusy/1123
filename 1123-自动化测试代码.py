#coding=utf-8
#设置字符集为utf-8
from selenium import webdriver
#从selenium库中导入webdriver驱动程序
br=webdriver.Chrome()
#定义可以操控的浏览器 chrome
br.get("https://www.baidu.com")
#浏览器打开网页的地址
#1.id定位
# br.find_element_by_id("kw").send_keys("美国大选")
#2.name定位
# br.find_element_by_name("wd").send_keys("混元太极马保国")
#3.class定位
# br.find_element_by_class_name("s_ipt").send_keys("电光5连鞭！")
#4.tag定位
# br.find_element_by_tag_name("input").send_keys("123")
#5.link定位
# br.find_element_by_link_text("hao123").click()
#6.partial link定位
# br.find_element_by_partial_link_text("闻").click()
#7.xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("拜登")
#8.css定位
br.find_element_by_css_selector("#kw").send_keys("特朗普")