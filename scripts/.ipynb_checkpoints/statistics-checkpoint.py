

def stat(data):
    
    
    for event in data:
        print(event["match"])
        
        #spread
        print("Spread Information")
        spread1odds = event["spread"][event["team1"]]["odds"]
        spread2odds = event["spread"][event["team2"]]["odds"]
        if 1/spread1odds + 1/spread2odds < 1:
            print("arbitrage found:")
            print(event["team1"] + " at " + event["spread"][event["team1"]]["src"])
            print(event["team2"] + " at " + event["spread"][event["team2"]]["src"])
        else:
            print("total market opportunity is " + str(1/spread1odds + 1/spread2odds))
            
            
        print("Moneyline Information")
        money1odds = event["moneyline"][event["team1"]]["odds"]
        money2odds = event["moneyline"][event["team2"]]["odds"]
        if 1/money1odds + 1/money2odds < 1:
            print("arbitrage found:")
            print(event["team1"] + " at " + event["moneyline"][event["team1"]]["src"])
            print(event["team2"] + " at " + event["moneyline"][event["team2"]]["src"])
        else:
            print("total market opportunity is " + str(1/money1odds + 1/money2odds))
        
        print("Points Information")
        point1odds = event["points"][0]["odds"]
        point2odds = event["points"][1]["odds"]
        if 1/point1odds + 1/point2odds < 1:
            print("arbitrage found:")
            print(event["points"][0]["amount"] + " at " + event["points"][0]["src"])
            print(event["points"][1]["amount"] + " at " + event["points"][1]["src"])
        else:
            print("total market opportunity is " + str(1/point1odds + 1/point2odds))
                  
            