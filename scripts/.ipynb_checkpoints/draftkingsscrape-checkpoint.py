from selenium import webdriver
from convertodds import *
import time


def get_data():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://sportsbook.draftkings.com/featured?category=game-lines&subcategory=basketball")
    remove = driver.find_elements_by_xpath('//div[@class = "sportsbook-welcome-modal__close"]')
    if(len(remove) > 0):
        remove[0].click()
    
    buttons = driver.find_elements_by_xpath('//div[@class="sportsbook-featured-accordion__wrapper sportsbook-accordion__wrapper collapsed"]')
    if(len(buttons) != 0):
        driver.execute_script("arguments[0].scrollIntoView();", buttons[0])
        buttons = driver.find_elements_by_xpath('//div[@class="sportsbook-featured-accordion__wrapper sportsbook-accordion__wrapper collapsed"]')
        
    for button in buttons:
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        time.sleep(4)
    
    events = driver.find_elements_by_xpath('//tbody[@class="sportsbook-table__body"]')
    event_list = []
    
    for event in events:
        lst = event.text.split("\n")
        if (len(lst) == 17):
            del lst[2]
            del lst[10]
        event_list.append(lst)
    
    return event_list

def transform_data(data):
    clean_list = []
    for event in data:
        if(len(event) == 21):
            del event[6]
            del event[13]
        try:
            df = {}
            df["match"] = event[1].upper() + " AT " + event[8].upper()
            df["team1"] = event[1]
            df["team2"] = event[8]

            odds1 = american_to_dec(int(event[3]))
            odds2 = american_to_dec(int(event[10]))
            df["spread"] = {}
            df["spread"][df["team1"]] = {"amount":float(event[2]),"odds":odds1}
            df["spread"][df["team2"]] = {"amount":float(event[9]),"odds":odds2}

            odds1 = american_to_dec(int(event[7]))
            odds2 = american_to_dec(int(event[14]))
            df["moneyline"] = {}
            df["moneyline"][df["team1"]] = {"odds":odds1}
            df["moneyline"][df["team2"]] = {"odds":odds2}

            odds1 = american_to_dec(int(event[6]))
            odds2 = american_to_dec(int(event[13]))

            ref = {"O":"Over","U":"Under"}

            df["points"] = {}

            amount1 = ref[event[4]] + event[5]
            amount2 = ref[event[11]] + event[12]
            df["points"][df["team1"]] = {"amount":amount1,"odds":odds1}
            df["points"][df["team2"]] = {"amount":amount2,"odds":odds2}

            clean_list.append(df)
        except:
            pass
        
    return clean_list

def draftking():
    data = get_data()
    return transform_data(data)

    
    