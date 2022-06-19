from selenium import webdriver
from convertodds import *
import time

def get_data():
    driver = webdriver.Chrome("/Users/bennysun/Downloads/chromedriver")
    driver.get("https://nj.pointsbet.com/sports/basketball")
    time.sleep(15)
    events = driver.find_elements_by_xpath('//div[@class = "fdz3fpy f1yn18fe f93i66z"]')
    event_list = []
    for event in events:
        element = event.text.split("\n")
        if(len(element) == 17):
            del element[11]
            del element[4]
        
        event_list.append(element)
    
    return event_list

def transform_data(data):
    clean_list = []
    
    for event in data:
        try:
            df = {}
            df["match"] = event[3].upper() + " AT " + event[9].upper()
            df["team1"] = event[3]
            df["team2"] = event[9]

            odds1 = american_to_dec(int(event[5]))
            odds2 = american_to_dec(int(event[11]))
            df["spread"] = {}
            df["spread"][df["team1"]] = {"amount":float(event[4]), "odds":odds1}
            df["spread"][df["team2"]] = {"amount":float(event[10]), "odds":odds2}

            odds1 = american_to_dec(int(event[8]))
            odds2 = american_to_dec(int(event[14]))
            df["moneyline"] = {}
            df["moneyline"][df["team1"]] = {"odds":odds1}
            df["moneyline"][df["team2"]] = {"odds":odds2}

            odds1 = american_to_dec(int(event[7]))
            odds2 = american_to_dec(int(event[13]))
            if (event[6][0:2] == "Ov"):
                amount1 = "Over" + event[6][2:]
                amount2 = "Under" + event[12][2:]
            else:
                amount1 = "Under" + event[6][2:]
                amount2 = "Over" + event[12][2:]

            df["points"] = {}
            df["points"][df["team1"]] = {"amount":amount1, "odds":odds1}
            df["points"][df["team2"]] = {"amount":amount2, "odds":odds2}
            clean_list.append(df)
        except:
            pass
    
    return clean_list

def pointsbet():
    data = get_data()
    return transform_data(data)