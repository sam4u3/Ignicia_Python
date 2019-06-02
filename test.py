import os
from selenium import webdriver
import time

chromedriver = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('https://google.com')

# driver.find_element_by_class_name("gb_d").click()
driver.find_element_by_id("gb_70").click()
driver.find_element_by_id("identifierId").send_keys("sayarmendis26@gmail.com")
driver.find_element_by_class_name("RveJvd").click()
time.sleep(3)
driver.find_element_by_class_name("whsOnd").send_keys("sayarm80")
driver.find_element_by_class_name("CwaK9").click()

print("a")
driver.quit()









# For Full Page ScreenShot :


# driver.quit()from selenium import webdriver
#
# from Screenshot import Screenshot_Clipping
#
# ob = Screenshot_Clipping.Screenshot()
# driver = webdriver.Chrome()
# url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
# driver.get(url)
# img_url = ob.full_Screenshot(driver, save_path=r'D:\Sayar Mendis\Python_Projects\Selenium\test',
#                              image_name='Myimage.png')
# print(img_url)
# driver.close()
#
# driver.quit()
#
# # For Html Element Clipping :
#
# from Screenshot import Screenshot_Clipping
# from selenium import webdriver
#
# ob = Screenshot_Clipping.Screenshot()
# driver = webdriver.Chrome()
# url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
# driver.get(url)
#
# element = driver.find_element_by_class_name('signup-prompt')
# img_url = ob.get_element(driver, element, r'D:\Sayar Mendis\Python_Projects\Selenium\test')
# print(img_url)
#
# driver.close()
#
# driver.quit()
#
# # For Html Element Clipping with Hiding Element :
#
# from Screenshot import Screenshot_Clipping
# from selenium import webdriver
#
#
# ob=Screenshot_Clipping.Screenshot()
# driver = webdriver.Chrome()
# url = "https://github.com/sam4u3"
# driver.get(url)
# Hide_elements = ['class=avatar width-full height-full avatar-before-user-status']  # Use full class name
# img_url = ob.full_Screenshot(driver, save_path=r'D:\Sayar Mendis\Python_Projects\Selenium\test', elements=Hide_elements,
#                              image_name='Myimage.png')
# print(img_url)
# driver.close()
