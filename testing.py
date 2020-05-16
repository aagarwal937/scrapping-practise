#from selenium import webdriver

#url = 'https://www.aliexpress.com/premium/laptop.html?d=y&origin=y&catId=0&initiative_id=SB_20200512133329&SearchText=laptop'

#driver = webdriver.Chrome()
#driver.get(url)


from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
except WebDriverException as e:
    print("\nChrome crashed on launch:")
    print(e)
    print("Trying again in 10 seconds..")
    sleep(10)
    self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
    print("Success!\n")
except Exception as e:
    raise Exception(e)
