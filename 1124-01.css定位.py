from selenium import webdriver
br=webdriver.Chrome()
# br.find_element_by_css_selector('input').send_keys("123")
br.get("https://www.baidu.com")
# br.find_element_by_css_selector("#kw").send_keys("凡尔赛")
# br.find_element_by_css_selector(".s_ipt").send_keys("绿茶")
# br.find_element_by_css_selector("[name='wd']").send_keys("TFBOYS")
# br.find_element_by_css_selector("input#kw").send_keys("游戏")
# br.find_element_by_css_selector("input.s_ipt").send_keys("巧碧螺")
br.find_element_by_css_selector("input[name='wd']").send_keys("55开")