from selenium import webdriver
from convertodds import *
import time


def get_data():
    driver = webdriver.Chrome("/Users/bennysun/Downloads/chromedriver")
    driver.get("https://sportsbook.draftkings.com/featured?category=game-lines&subcategory=basketball")
    driver.execute_script("window.scrollTo(0, 700)") 
    buttons = driver.find_elements_by_xpath('//div[@class="sportsbook-featured-accordion__wrapper sportsbook-accordion__wrapper collapsed"]')
    for button in buttons:
        button.click()
        time.sleep(5)

    events = driver.find_elements_by_xpath('//table[@class="sportsbook-table"]')
    event_list = []
    for event in events:
        event_list.append(event.text.split("\n"))
    
    return event_list

def transform_data(data):
    clean_list = []
    for event in data:
        if(len(event) == 21):
            del event[6]
            del event[13]
        
        df = {}
        df["match"] = event[5].upper() + " AT " + event[12].upper()
        df["date"] = event[4]
        df["team1"] = event[5]
        df["team2"] = event[12]
        
        odds1 = american_to_dec(int(event[7]))
        odds2 = american_to_dec(int(event[14]))
        df["spread"] = {}
        df["spread"][df["team1"]] = {"amount":float(event[6]),"odds":odds1}
        df["spread"][df["team2"]] = {"amount":float(event[13]),"odds":odds2}
        
        odds1 = american_to_dec(int(event[11]))
        odds2 = american_to_dec(int(event[18]))
        df["moneyline"] = {}
        df["moneyline"][df["team1"]] = {"odds":odds1}
        df["moneyline"][df["team2"]] = {"odds":odds2}
        
        odds1 = american_to_dec(int(event[10]))
        odds2 = american_to_dec(int(event[17]))
        
        ref = {"O":"Over","U":"Under"}
        
        df["points"] = {}
        
        amount1 = ref[event[8]] + event[9]
        amount2 = ref[event[15]] + event[16]
        df["points"][df["team1"]] = {"amount":amount1,"odds":odds1}
        df["points"][df["team2"]] = {"amount":amount2,"odds":odds2}
        
        clean_list.append(df)
    return clean_list

def draft_king():
    data = get_data()
    return transform_data(data)

    
    