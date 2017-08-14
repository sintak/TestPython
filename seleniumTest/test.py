from selenium import webdriver  
driver = webdriver.PhantomJS(executable_path="C:\ProgramData\Anaconda3\Scripts\phantomjs.exe")  
driver.get("http://www.baidu.com")  
data = driver.title  
print(data)

driver.get("http://www.csdn.net")    
data = driver.title  
driver.save_screenshot('csdn.png')  
print(data)