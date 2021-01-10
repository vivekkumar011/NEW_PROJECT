from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="../resources/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.triphobo.com/")

# Click on Plan Your Next Vacation
driver.find_element_by_link_text("Plan Your Next Vacation").click()

# Use of explicit wait
wait = WebDriverWait(driver,10)
loc = (By.CSS_SELECTOR, "[placeholder='Where do you want to go?']")
sk = wait.until(EC.visibility_of_element_located(loc))
# WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='Where do you want to go?']"))

sk.send_keys("Houston")
sleep(3)
driver.find_element_by_xpath("//span[text()='Houston, Texas, United States']").click()
sleep(3)
driver.find_element_by_xpath("//input[@class='input-control hasDatepicker']").click() #clicking on from datepicker
driver.find_element_by_xpath("(//a[text()='18'])[2]").click() #selecting from Date
driver.find_element_by_xpath("//input[@class='input-control hasDatepicker']").click() #clicking on to datepicker
driver.find_element_by_xpath("(//a[text()='22'])[2]").click() #selecting to Date

driver.find_element_by_css_selector("span[class='button p-color full-width start-planning']").click() #Click Start Planning

# Getting locator of NEXT
next_loc = (By.CSS_SELECTOR,"span[id='js_city_step_next']")
# Clicking on NEXT when its visible
cl = wait.until(EC.visibility_of_element_located(next_loc))
cl.click()
sleep(2)
skip_loc = (By.CSS_SELECTOR,"span[class='next-button js_city_step_move next-btn-dsk']")
cl = wait.until(EC.visibility_of_element_located(skip_loc))
cl.click()

sleep(2)
skip_2_loc = By.CSS_SELECTOR,"span[class='next-button js_city_step_move next-btn-dsk']"
(wait.until(EC.visibility_of_element_located(skip_2_loc))).click()

sleep(2)
editable_loc = By.XPATH,"//li[@class='view-tab calendar']"       #"//span[text()='Editable view']"
wait = WebDriverWait(driver,20)
(wait.until(EC.visibility_of_element_located(editable_loc))).click()


"""
Assignment3(Most Important Assignment for entire training):
- go to triphobo.com website
- Click "Later" in be updated box (this may not appear, then ignore)
- Click on "PLAN YOUR NEXT VACATION" button on the homepage
- Type Where do you want to go? field, Houston in Texas
- Select Start and End date of your journey
- Click on button "Start Planning"
- Click on "Next - About Your Trip"
- Click on "Skip to About You"
- Click on "Trip Overview"
- Click on "Editable View"
- Drag "Children's museum from day 3 to day 4"
- Click on Save plan -> Finish Planning
"""


#driver.close()