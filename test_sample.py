from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
 
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.get("https://www.microsoft.com/en-us/microsoft-teams/log-in")
elem = driver.find_element_by_link_text('Download now')
elem.text
'Download'
elem.get_attribute('href')
'https://www.microsoft.com/en-us/microsoft-teams/download-app'
elem.click()
elem = driver.find_element_by_link_text('Download for desktop')
elem.text 
'Download for desktop'
elem.get_attribute('href')
'https://www.microsoft.com/en-us/microsoft-teams/download-app#desktopAppDownloadregion'
elem.click()

print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.quit()
