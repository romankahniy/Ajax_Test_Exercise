from appium import webdriver
from selenium.webdriver.common.by import By
import time

capabilities = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'Nexus 5 API 29',
    'appPackage': 'com.ajaxsystems',
    'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
    'app': 'D:\\Study\\PythonProject\\AjaxTests\\app_binaries\\com.ajaxsystems_2022-08-19.apk'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
time.sleep(5)

driver.find_element(By.ID, 'com.ajaxsystems:id/registration').click()
time.sleep(5)

name = driver.find_element(By.ID, 'com.ajaxsystems:id/name')
name.clear()
name.send_keys('Roman Kakhnii')

email = driver.find_element(By.ID, 'com.ajaxsystems:id/login')
email.clear()
email.send_keys('super.rk76@gmail.com')

email_confirmation = driver.find_element(By.ID, 'com.ajaxsystems:id/loginConfirm')
email_confirmation.clear()
email_confirmation.send_keys('super.rk76@gmail.com')

phone_number = driver.find_element(By.ID, 'com.ajaxsystems:id/phone')
phone_number.clear()
phone_number.send_keys('992145170')

password = driver.find_element(By.ID,'com.ajaxsystems:id/password')
password.clear()
password.send_keys('Roman1223334444!')

password_confirmation = driver.find_element(By.ID, 'com.ajaxsystems:id/passwordConfirm')
password_confirmation.clear()
password_confirmation.send_keys('Roman1223334444!')

driver.find_element(By.ID, 'com.ajaxsystems:id/agreement').click()

driver.find_element(By.ID, 'com.ajaxsystems:id/mTitle').click()

