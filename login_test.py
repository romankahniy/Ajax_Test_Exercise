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

driver.find_element(By.ID, 'com.ajaxsystems:id/login').click()
time.sleep(5)

log = driver.find_element(By.ID, 'com.ajaxsystems:id/login')
log.clear()
log.send_keys('qa.ajax.app.automation@gmail.com')

pas = driver.find_element(By.ID, 'com.ajaxsystems:id/password')
pas.clear()
pas.send_keys('qa_automation_password')

driver.find_element(By.ID, 'com.ajaxsystems:id/next').click()
time.sleep(10)

driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
time.sleep(2)

driver.find_element(By.ID, 'com.ajaxsystems:id/cancel_button').click()