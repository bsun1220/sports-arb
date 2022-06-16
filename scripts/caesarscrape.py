from selenium import webdriver
from convertodds import *

def get_data():
    driver = webdriver.Chrome("/Users/bennysun/Downloads/chromedriver")
    driver.get("https://www.williamhill.com/us/nj/bet/basketball/events/all?id=5806c896-4eec-4de1-874f-afed93114b8c")
    events = driver.find_elements_by_xpath('//div[@class="eventList"]')
    
    event_list = []
    for event in events:
        event_list.append(event.text.split("\n"))
                        
    return event_list

def clean_data(data):
    clean_list = []
    for event in data:
        df = {}
        df["match"] = event[0]
        df["date"] = event[1].split(" |")[0]
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
    
    return clean_list

def caesar():
    data = get_data()
    return clean_data(data)
        
        