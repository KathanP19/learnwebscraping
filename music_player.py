from selenium import webdriver
import time

user_input = input('Enter artist name: ')

driver = webdriver.Chrome(executable_path= r"D:\Tracker APP\dynamic_webscraper\chromedriver.exe")
driver.get('https://www.jiosaavn.com/')
driver.implicitly_wait(10)

def weekly_top_song():
    playall = driver.find_element_by_xpath('//*[@id="top-15"]/div[1]/a')
    link = playall.get_attribute('href')
    driver.get(link)
    play_song = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/button').click()

def searchforartist(tosearch):
    search_place = driver.find_element_by_xpath('//*[@id="search"]')
    search_place.send_keys(tosearch)
    search_place.send_keys(u'\ue007')

def stop(data):
    time.sleep(data)
    driver.close()

def play_radio():    
    driver.find_element_by_xpath('//*[@id="main"]/div/ol/li[1]/div[3]/div/div[1]/div/div/span/a').click()
    driver.find_element_by_xpath('//*[@id="main"]/div/section/div/ul/li[1]/a').click()
    stop(60)
        

searchforartist(user_input)
play_radio()
