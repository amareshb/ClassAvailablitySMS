import time
from selenium.webdriver.support.ui import Select # Install selenium packages using pip on pycharm
from selenium import webdriver
from twilio.rest import Client

account_sid = "" #your sid
auth_token = "" # your token

client = Client(account_sid, auth_token)


driver=webdriver.PhantomJS("D:/Stuff/ASU/Phantom/phantomjs-2.1.1-windows/bin/phantomjs.exe") # Insatll phantomJS from the net and put the path of the exe file here

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
        client.api.account.messages.create(to="+19999999999",from_="+19999999999",body="Just " + numSeats +" seats left for " + subject + " "+classNum)
    else:
        print("Uh no.")

else:
    print("No")
