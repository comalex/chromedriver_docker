# http://danielfrg.com/blog/2015/09/28/crawling-python-selenium-docker/
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

YOUR_DOCKERHOST_IP = None # You need to fix YOUR_DOCKERHOST_IP

if YOUR_DOCKERHOST_IP is None:
    raise Exception("You need to fix YOUR_DOCKERHOST_IP var")

driver = webdriver.Remote(command_executor='http://%s:4444/wd/hub' % YOUR_DOCKERHOST_IP, 
    desired_capabilities=DesiredCapabilities.CHROME)
driver.get("http://www.yelp.com")
driver.close()
