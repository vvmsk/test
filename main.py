from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math
import random

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    # button = browser.find_element_by_tag_name("button")
    #
    # button.click()

    #Ваш код, который заполняет обязательные поля
    input1=browser.find_element_by_css_selector(".btn")
    input1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # alert = browser.switch_to.alert
    # alert.accept()
    x_el = browser.find_element_by_css_selector("[id='input_value']")
    x=x_el.text
    y=str(math.log(abs(12*math.sin(int(x)))))
    input2 = browser.find_element_by_css_selector("[id='answer']")
    input2.send_keys(y)
    # input2 = browser.find_element_by_css_selector("[name='lastname']")
    # input2.send_keys("yy")
    # input3 = browser.find_element_by_css_selector("[name='email']")
    # input3.send_keys("yyy")
    # file_path = ("D:\\Selenium\\Chrome\\test.txt")
    # input4 = browser.find_element_by_css_selector("[id='file']")
    # input4.send_keys(file_path)

       # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

