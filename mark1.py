from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com')
driver.find_element_by_class_name('button-1').click()
lnk_Customers_menu_text = 'Customers'
driver.find_element_by_link_text('Customers').click()
lnk_Customers_submenu_xpath = '/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/i'
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/i').click()
table_rows = '//*[@id="customers-grid"]/tbody/tr'
rows = driver.find_elements_by_xpath(table_rows)
print(rows)


