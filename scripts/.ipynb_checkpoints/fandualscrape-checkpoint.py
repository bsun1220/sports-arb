from selenium import webdriver
from convertodds import *
import time

def get_data():
    driver = webdriver.Chrome("/Users/bennysun/Downloads/chromedriver")
    driver.get("https://sportsbook.fanduel.com/basketball?tab=upcoming")
    
    events = driver.find_elements_by_xpath('//div[@class = "t ab v w x ic h bk id ai"]')
    
    event_list = []
    for event in events:
        event_list.append(event.text.split("\n"))
    
    return event_list

def transform_data(data):
    clean_list = []
    for event in data:
        if(len(event) != 12):
            continue
        
        df = {}
        df["match"] = event[0].upper() + " AT " + event[1].upper()
        df["team1"] = event[0]
        df["team2"] = event[1]
        
        odds1 = american_to_dec(int(event[3]))
        odds2 = american_to_dec(int(event[8]))
        df["spread"] = {}
        df["spread"][df["team1"]] = {"amount":float(event[2]), "odds":odds1}
        df["spread"][df["team2"]] = {"amount":float(event[7]), "odds":odds2}
        
        odds1 = american_to_dec(int(event[4]))
        odds2 = american_to_dec(int(event[9]))
        df["moneyline"] = {}
        df["moneyline"][df["team1"]] = {"odds":odds1}
        df["moneyline"][df["team2"]] = {"odds":odds2}
        
        if(event[5][0] == "O"):
            amount1 = "Over" + event[5][1:]
            amount2 = "Under" + event[10][1:]
        else:
            amount1 = "Under" + event[5][1:]
            amount2 = "Over" + event[10][1:]
        
        odds1 = american_to_dec(int(event[6]))
        odds2 = american_to_dec(int(event[11]))
        df["points"] = {}
        df["points"][df["team1"]] = {"amount":amount1, "odds":odds1}
        df["points"][df["team2"]] = {"amount":amount2, "odds":odds2}
        
        clean_list.append(df)
    
    return clean_list

def fandual():
    data = get_data()
    return transform_data(data)