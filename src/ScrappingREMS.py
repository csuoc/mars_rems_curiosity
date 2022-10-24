# Scraping REMS widget

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def ScrappingREMS():
    url2 = "http://cab.inta-csic.es/rems/es/"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    lista_ = []

    with driver:
        driver.get(url2)
        
        for i in range(1574):

            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID,"mw-previous")))
            #element.click()

            sol = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-sol']"))).text
            earth_day = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-terrestrial_date']"))).text
            month = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-season']"))).text
            maxtemp = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-max_temp']"))).text
            mintemp = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-min_temp']"))).text
            pressure = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-pressure']"))).text
            atmo_opacity = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='mw-atmo_opacity']"))).text
            
            new_dict = {
                "Earth Date": earth_day,
                "Sol": sol,
                "Month": month,
                "Min_temp": mintemp,
                "Max_temp": maxtemp,
                "Pressure": pressure,
                "Atmo_opacity": atmo_opacity
            }
            
            lista_.append(new_dict)
            element.click()

    widget = pd.DataFrame(lista_)
    
    return widget