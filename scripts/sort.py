def sort_data(data):
    
    clean_data = []
    for event in data:
        obj = {}
        obj["match"] = event["match"]
        obj["team1"] = event["team1"]
        obj["team2"] = event["team2"]
        obj["spread"] = {}
        
        maxteam1 = 0;
        maxteam1index = 0; 
        index = 0
        for spread in event["spread"][event["team1"]]:
            if(spread["odds"] > maxteam1):
                maxteam1 = spread["odds"]
                maxteam1index = index
            index = index + 1
        
        obj["spread"][event["team1"]] = event["spread"][event["team1"]][maxteam1index]
        
        maxteam2 = 0;
        maxteam2index = 0; 
        index = 0
        for spread in event["spread"][event["team2"]]:
            if(spread["odds"] > maxteam2):
                maxteam2 = spread["odds"]
                maxteam2index = index
            index = index + 1
        
        obj["spread"][event["team2"]] = event["spread"][event["team2"]][maxteam2index]
        
        maxteam1 = 0;
        maxteam1index = 0; 
        index = 0
        for moneyline in event["moneyline"][event["team1"]]:
            if(moneyline["odds"] > maxteam1):
                maxteam1 = moneyline["odds"]
                maxteam1index = index
            index = index + 1
        
        obj["moneyline"] = {}
        obj["moneyline"][event["team1"]] = event["moneyline"][event["team1"]][maxteam1index]
        
        maxteam2 = 0;
        maxteam2index = 0; 
        index = 0
        for moneyline in event["moneyline"][event["team2"]]:
            if(moneyline["odds"] > maxteam2):
                maxteam2 = moneyline["odds"]
                maxteam2index = index
            index = index + 1
        
        obj["moneyline"][event["team2"]] = event["moneyline"][event["team2"]][maxteam2index]
        
        underodds = 0
        underentry = {}
        overodds = 0
        overentry = {}
        
        for team in event["points"]:
            
            for entry in event["points"][team]:
                if(entry["amount"][0] == "O"):
                    if entry["odds"] > overodds:
                        overentry = entry
                        overodds = entry["odds"]
                elif entry["amount"][0] == "U":
                    if entry["odds"] > underodds:
                        underentry = entry
                        underodds = entry["odds"]
        obj["points"] = [underentry, overentry]
        
        clean_data.append(obj)
    return clean_data
        