from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
a = 3
DRIVER_PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://discord.com/channels/@me")
driver.find_element_by_name("email").click()
driver.find_element_by_name("email").send_keys("""Your email""")
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").send_keys("""Your Password""" + Keys.ENTER)
driver.implicitly_wait(3)
while (True):
    if (driver.current_url == "https://discord.com/channels/@me"):
        driver.find_element_by_tag_name("html").send_keys(Keys.ESCAPE)
        break
while a < 78:
        driver.find_element_by_id("private-channels-" + str(a)).click()
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div[2]")
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div[2]").send_keys("""Your Message""" + Keys.ENTER)
        
        a = a + 1