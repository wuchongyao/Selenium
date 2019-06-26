# -*- coding:utf-8 -*-
# date:2019-06-26
# author:wuchongyao


from selenium import webdriver


browser = webdriver.Firefox(executable_path=r"d:\git\Selenium\geckodriver")
browser.get("http://www.baidu.com")

# 通过id定位
# browser.find_element_by_id("kw").send_keys("selenium")

# 通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")

# 通过tag name方式定位
# browser.find_element_by_tag_name("input").send_keys("selenium")

# 通过class name 方式定位
# browser.find_element_by_class_name("s_ipt").send_keys("selenium

# 通过CSS 方式定位
# browser.find_element_by_css_selector("#kw").send_keys("selenium")

# 通过xpath 方式定位
# browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

browser.find_element_by_id("su").click()


#browser.quit()