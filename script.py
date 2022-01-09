from selenium import webdriver
import time

#Load static data for the test
name = "Иван"
family = "Иванов"
firmName = "Facebook is new Meta"
street = "1164 Борисова Градина, София"
city = "София"
email = "something@gmail.com"
postCode = "1164"
phone = "0879999999"

#Load the driver for Google Chrome
driver = webdriver.Chrome(executable_path="C:\\Users\\Balantaim\\Documents\\selenium-java-4.0.0\\WebDrivers\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.set_script_timeout(60)
driver.get('https://expresswater.bg/shop/')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/aside[2]/ul/li[2]/a').click()
time.sleep(2)

if (driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/ul/li[4]/div/a[2]').is_displayed()):
	driver.find_element_by_css_selector('body > div.container > div > div > div.col-xl-9.col-xl-push-3.col-lg-8.col-lg-push-4.col-md-8.col-md-push-4.text-page > ul > li.has-post-thumbnail.product.type-product.post-3432.status-publish.last.instock.product_cat-water.product_cat-215.product_tag-219.product_tag-226.product_tag-220.shipping-taxable.purchasable.product-type-simple > div > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart.btn').click()
	driver.find_element_by_css_selector('body > div.container > div > div > div.col-xl-9.col-xl-push-3.col-lg-8.col-lg-push-4.col-md-8.col-md-push-4.text-page > ul > li.has-post-thumbnail.product.type-product.post-3432.status-publish.last.instock.product_cat-water.product_cat-215.product_tag-219.product_tag-226.product_tag-220.shipping-taxable.purchasable.product-type-simple > div > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart.btn').click()

time.sleep(2)
driver.get('https://expresswater.bg/product/trapezna-voda-serdika-19l/')
time.sleep(2)
driver.find_element_by_name('add-to-cart').click()

time.sleep(2)
driver.get('https://expresswater.bg/checkout/')

driver.find_element_by_xpath('//*[@id=\"ship-to-different-address-checkbox\"]').click()
txtBoxName = driver.find_element_by_id('billing_first_name')
txtBoxName.send_keys(name)


# driver.quit()
