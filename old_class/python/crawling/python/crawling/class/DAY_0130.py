#%%
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.careerbuilder.com/')
driver.implicitly_wait(0)
# id, 비밀번호 전달
# <input>의 이름이 id를 검색
#%%
driver.find_element_by_name('id').send_keys('shanghai1109')
driver.find_element_by_name('pw').send_keys('!Kk159753')
driver.find_element_by_xpath('//*[@id="log.login"]').click()
# %%
