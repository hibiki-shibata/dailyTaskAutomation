import time                          
from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
from datetime import datetime, timedelta, timezone
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

##file name info
print('file location:')
location = input()

#Prepare Process
lst = pd.read_csv("~/Downloads/"+location+".csv",header=None).values.tolist() ##File name change here
rows = len(lst) 
row = 1 
pbar1 = tqdm(range(rows-1))


## Setup environment 
service = Service('/Users/tomoyakai/Downloads/chromedriver_mac_arm64')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

# Get ChromeDriver version
chrome_version = driver.capabilities['chrome']['chromedriverVersion'].split()[0]


print(f"Using ChromeDriver version: {chrome_version}")


driver.get('https://accounts.google.com/signin/v2/identifier')
driver.implicitly_wait(50)

 
JST = timezone(timedelta(hours=+9), 'JST')
now = datetime.now(JST)
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
dt = now.strftime('%Y-%m-%d')

time.sleep(60)       

## Login Ops tool
driver.get('https://google.com/')
time.sleep(5)    
loginClick = driver.find_element(By.XPATH,'//a')
loginClick.click()
time.sleep(5) 


##strat

while row < rows:

    try:


        ##get to page ok
        url = 'https://google.com/route'
        driver.get(url)
       
        driver.implicitly_wait(10)
        time.sleep(4)

        ##Click on add settlement ok
        clickaddsettlement = driver.find_element(By.XPATH,'//*[@id="page-mount-point"ton/div[3]')
        clickaddsettlement.click()
        
        time.sleep(3)
        
        ##add venue name ok
        addvenuename = driver.find_element(By.XPATH,'//*[@')
        addvenuename.click()
        addvenuename.send_keys(lst[row][0])
        
        driver.implicitly_wait(12)
        time.sleep(3)

        ## Click on the search result (assuming it's a dropdown)
        searchresult = driver.find_elements(By.XPATH, "/html/body")
        searchresult[0].click()
        
        time.sleep(1)


        searchresult = driver.find_element(By.XPATH, "/html/")
        searchresult.click()
        
        time.sleep(1)


        ##input price in JPY
        inputprice = driver.find_element(By.XPATH,'/html/body')
        inputprice.click()
        inputprice.send_keys(lst[row][1])
      
        time.sleep(1)

        ##input VAT%
        inputvat = driver.find_element(By.XPATH,'/html/body/')
        inputvat.click()
        inputvat.send_keys("10")
        
        time.sleep(1)

        ##input note
        inputexplanation = driver.find_element(By.XPATH,'/html')
        
        inputexplanation.click()
        
        inputexplanation.send_keys(lst[row][2])
        
        time.sleep(1)

          ##click 
        producttypepick = driver.find_element(By.XPATH,'/html/body/div')
        producttypepick.click()
        
        producttypepick.click()
        
        action = ActionChains(driver)
        
        action.send_keys(Keys.ARROW_UP).send_keys(Keys.ENTER).perform()
        

        time.sleep(1)



        ##push put button
        # clickadd = driver.find_element(By.XPATH,'/html/body/div[8]/div/div/div/footer/button[2]/div[2]')
        clickadd = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(8) > div')
        
        clickadd.click()
        # print(0)



        time.sleep(12)

        row += 1
        pbar1.update(1)	
    
    except Exception as e: ##add error info
        print("An error occured:", e)
        
        
        
    

    


driver.quit()
        