import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
size = "L"
name = ""
email = ""
tel = ""
address = ""
city = ""
state = ""
zip_code = ""
card = ""
security_code = ""
card_month = ""
card_year = ""

def cop(link):
    driver.get(link)
    driver.find_element_by_id("size").send_keys(size)
    driver.find_element_by_name("commit").click()
    driver.get("http://www.supremenewyork.com/checkout")
    driver.find_element_by_id("order_billing_name").send_keys(name)
    driver.find_element_by_id("order_email").send_keys(email)
    driver.find_element_by_id("order_tel").send_keys(tel)
    driver.find_element_by_id("bo").send_keys(address)
    driver.find_element_by_id("order_billing_zip").send_keys(zip_code)
    driver.find_element_by_id("order_billing_city").send_keys(city)
    driver.find_element_by_id("order_billing_state").send_keys(state)
    driver.find_element_by_id("cnb").send_keys(card)
    driver.find_element_by_id("credit_card_month").send_keys(card_month)
    driver.find_element_by_id("credit_card_year").send_keys(card_year)
    driver.find_element_by_id("vval").send_keys(security_code)
    elem = driver.find_elements_by_class_name("icheckbox_minimal")[1]
    hover = ActionChains(driver).move_to_element(elem).perform()
    elem.click()
    elem = driver.find_element_by_name("commit").click()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            cop(item)
    else:
        print "No links entered"
