import time
from selenium.webdriver.support.ui import Select # Install selenium packages using pip on pycharm
from selenium import webdriver
from twilio.rest import Client
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


account_sid = os.getenv('ACCOUNT_SID') #your sid
auth_token = os.getenv('AUTH_TOKEN') # your token
from_num = os.getenv('FROM_NUMBER')
to_num = os.getenv('TO_NUMBER')
client = Client(account_sid, auth_token)


driver=webdriver.PhantomJS() # Insatll phantomJS from the net and put the path of the exe file here

driver.implicitly_wait(4)
trial = 0;
#while True:
now = time.time()
driver.get("https://webapp4.asu.edu/catalog/")

subject = "SER"
classNum = "516"
driver.find_element_by_id('subjectEntry').send_keys(subject)
driver.find_element_by_id('catNbr').send_keys(classNum)
searchBtn = driver.find_element_by_id('go_and_search').click()
#table = driver.find_element_by_id('CatalogList')
#print(table)
#availSeats = driver.find_elements_by_css_selector('availableSeatsColumnValue')
#print(driver.find_elements_by_css_selector('.col-xs-3')[0].get_attribute('innerHTML').strip())

if(driver.find_elements_by_css_selector('.col-xs-3') and len(driver.find_elements_by_css_selector('.col-xs-3')) > 0):
    print(driver.find_elements_by_css_selector('.col-xs-3')[0].get_attribute('innerHTML').strip())
    numSeats = driver.find_elements_by_css_selector('.col-xs-3')[0].get_attribute('innerHTML').strip()
    if(int(numSeats) > 0):
        print("Yaay" + numSeats + " for " + subject + classNum) 
        #change numbers
        client.api.account.messages.create(to=to_num, from_=from_num, body="Just " + numSeats +" seats left for " + subject + " "+classNum)
    else:
        print("Uh no.")

else:
    print("No")
