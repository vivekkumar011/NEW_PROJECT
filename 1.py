from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="../resources/chromedriver.exe")
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com/")
driver.find_element(By.ID, "loginname").send_keys("stc123")
driver.find_element(By.ID,"loginbutton").submit()
alert1 = driver.switch_to.alert
assert (alert1.text) == "Please enter Password"
alert1.accept()
driver.find_element_by_xpath("//button[text() = 'Contact us!']").click()
parent_win_handle = driver.current_window_handle
driver.switch_to.window("Contact")
driver.find_element_by_css_selector("span[class='glyphicon glyphicon-search']").click()
WebDriverWait(driver,5).until(expected_conditions.alert_is_present())
alert2 = driver.switch_to.alert
print ("Printing message in alert2: ", alert2.text)
alert2.send_keys('London')
alert2.accept()
driver.close()
driver.switch_to.window(parent_win_handle)
driver.find_element_by_css_selector("img[id='logo']").click()
alert3 = driver.switch_to.alert
print ("Printing message in alert3: ", alert3.text)
alert3.dismiss()
driver.close()

"""
Assignment1
1. Alerts - Goto http://selenium-examples.nichethyself.com/
2. Type username as stc123
3. Click on Submit
4. Handle the alert. Verify that the message displayed on alert is "Please enter Password" 
5. Click on "Contact Us" menu on the top left.
6. Switch to Contact Us window
7. Click on Search icon
8. Alert will be displayed. 
9. Type London in the box.
10. Click on OK
11. Close Contact Us window
12. Switch back to main window
13. Click on boat icon on top left hand side of the page. 
14. handle the alert by clicking on cancel
"""
