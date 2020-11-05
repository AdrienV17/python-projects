from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('http://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
test_message = 'Hello! This is a Test!!!'
user_message.send_keys(test_message)

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert test_message in output_message.text

chrome_browser.quit()