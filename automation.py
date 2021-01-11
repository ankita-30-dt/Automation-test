#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import string


# In[2]:


chromedriver=r"/usr/bin/chromedriver" # path of chromedriver
driver = webdriver.Chrome(chromedriver)
act = ActionChains(driver)


# In[3]:


driver.get('https://demojanus.thexfuture.com/authentication/signin')

user = driver.find_element_by_xpath('//*[@formcontrolname="email" ]')
user.send_keys('janus@thexfuture.com')

passd=  driver.find_element_by_xpath("//*[@type='password' ]")
passd.send_keys('Wedigtech@123')


button = driver.find_element_by_xpath("//*[@type='submit' ]")
button.click()

print('User Successfully Logined In')

time.sleep(5)


# In[9]:


button = driver.find_element_by_xpath("//*[@class='btn bg-red waves-effect' and contains(text(),'Post a Use Case')]")
button.click()

enter = driver.find_element_by_xpath("//*[@minlength='ucstitleMinLength' ]")
enter.send_keys("test case new")

tick = driver.find_element_by_xpath("//*[@class='material-icons' and contains(text(),'check') ]")
tick.click()
print("clicked")

time.sleep(3)


# In[ ]:




