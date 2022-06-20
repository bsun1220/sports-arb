from selenium import webdriver
from convertodds import *
import time

def get_data():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.williamhill.com/us/nj/bet/basketball/events/all")
    
    buttons = driver.find_elements_by_xpath('//div[@class="expanderHeader collapsed"]')
    
    value = 0;
    length = 1000/(len(buttons) + 1)
    for button in buttons:
        button.click()
        value += length
        driver.execute_script("window.scrollTo(0," + str(value)+")") 
        time.sleep(2)
    
    events = driver.find_elements_by_xpath('//div[@class="eventList"]')
    
    event_list = []
    for event in events:
        lst = event.text.split("\n")
        if (len(lst) % 17 != 0):
            continue
        
        for i in range(0, len(lst), 17):
            event_list.append(lst[i:i+17])
                        
    return event_list

def clean_data(data):
    clean_list = []
    for event in data:
        try:
            df = {}
            df["match"] = event[0]

            df["team1"] = event[2]
            df["team2"] = event[3]
            df["spread"] = {}
            odds1 = american_to_dec(int(event[6]))
            odds2 = american_to_dec(int(event[8]))
            df["spread"][event[2]] = {"amount":float(event[5]), "odds":odds1}
            df["spread"][event[3]] = {"amount":float(event[7]), "odds":odds2}

            df["moneyline"] = {}
            odds1 = american_to_dec(int(event[10]))
            odds2 = american_to_dec(int(event[11]))
            df["moneyline"][event[2]] = {"odds":odds1}
            df["moneyline"][event[3]] = {"odds":odds2}

            df["points"] = {}
            odds1 = american_to_dec(int(event[14]))
            odds2 = american_to_dec(int(event[16]))
            df["points"][event[2]] = {"amount":event[13], "odds":odds1}
            df["points"][event[3]] = {"amount":event[15], "odds":odds2}

            clean_list.append(df)
        except:
            pass
    
    return clean_list

def caesar():
    data = get_data()
    return clean_data(data)
        
        