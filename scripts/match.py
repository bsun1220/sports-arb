from fuzzywuzzy import fuzz


def match_source(caesar, draftkings, fandual, pointsbet):
    
    data = [caesar, draftkings, fandual, pointsbet]
    ref = ["caesar", "draftkings", "fandual", "pointsbet"]
    shared = []
    for i in range(len(data)):
        for event1index in range(len(data[i]) - 1, -1, -1):
            event1 = data[i][event1index]       
            found = False
            index = -1
            unique = True
            for j in range(i + 1, len(data)):
                for event2index in range(len(data[j]) - 1, -1, -1):
                    event2 = data[j][event2index]
                    match1 = fuzz.partial_ratio(event1["team1"], event2["team1"]) > 60
                    match2 = fuzz.partial_ratio(event1["team2"], event2["team2"]) > 60
                    match3 = fuzz.partial_ratio(event1["team1"], event2["team2"]) > 60
                    match4 = fuzz.partial_ratio(event1["team2"], event2["team1"]) > 60
                    
                    completed = False
                    if(match1 and match2):
                        team1 = event2["team1"]
                        team2 = event2["team2"]
                        completed = True
                    elif (match3 and match4):
                        team1 = event2["team2"]
                        team2 = event2["team1"]
                        completed = True
                    
                    if completed:
                        unique = False
                        if (not found):
                            shared_match = {}
                            shared_match["match"] = event1["match"]
                            shared_match["team1"] = event1["team1"]
                            shared_match["team2"] = event1["team2"]
                            
                            shared_match["spread"] = {}
                            spread1 = event1["spread"][event1["team1"]]
                            spread1["src"] = ref[i]
                            spread2 = event2["spread"][team1]
                            spread2["src"] = ref[j]
                            shared_match["spread"][event1["team1"]] = [spread1, spread2]
                            
                            spread3 = event1["spread"][event1["team2"]]
                            spread3["src"] = ref[i]
                            spread4 = event2["spread"][team2]
                            spread4["src"] = ref[j]
                            shared_match["spread"][event1["team2"]] = [spread3, spread4]
                            
                            money1 = event1["moneyline"][event1["team1"]]
                            money2 = event2["moneyline"][team1]
                            money1["src"] = ref[i]
                            money2["src"] = ref[j]
                            
                            money3 = event1["moneyline"][event1["team2"]]
                            money4 = event2["moneyline"][team2]
                            money3["src"] = ref[i]
                            money4["src"] = ref[j]
                            shared_match["moneyline"] = {}
                            shared_match["moneyline"][event1["team1"]] = [money1,money2]
                            shared_match["moneyline"][event1["team2"]] = [money3,money4]
                            
                            points1 = event1["points"][event1["team1"]]
                            points2 = event2["points"][team1]
                            points1["src"] = ref[i]
                            points2["src"] = ref[j]
                            
                            points3 = event1["points"][event1["team2"]]
                            points4 = event2["points"][team2]
                            points3["src"] = ref[i]
                            points4["src"] = ref[j]
                            shared_match["points"] = {}
                            shared_match["points"][event1["team1"]] = [points1,points2]
                            shared_match["points"][event1["team2"]] = [points3,points4]
                            
                            shared.append(shared_match)
                            index = len(shared) - 1
                            found = True
                            
                        else:
                            team1spread = event2["spread"][team1]
                            team1spread["src"] = ref[j]
                            team2spread = event2["spread"][team2]
                            team2spread["src"] = ref[j]
                            
                            shared[index]["spread"][event1["team1"]].append(team1spread)
                            shared[index]["spread"][event1["team2"]].append(team2spread)
                            
                            team1money = event2["moneyline"][team1]
                            team1money["src"] = ref[j]
                            team2money = event2["moneyline"][team2]
                            team2money["src"] = ref[j]
                            
                            shared[index]["moneyline"][event1["team1"]].append(team1money)
                            shared[index]["moneyline"][event1["team2"]].append(team2money)
                            
                            team1points = event2["points"][team1]
                            team1points["src"] = ref[j]
                            team2points = event2["points"][team2]
                            team2points["src"] = ref[j]
                            
                            shared[index]["points"][event1["team1"]].append(team1points)
                            shared[index]["points"][event1["team2"]].append(team2points)
                        del data[j][event2index]
            
            if unique:
                shared_match = event1
                shared_match["spread"][event1["team1"]]["src"] = ref[i]
                shared_match["spread"][event1["team1"]] = [shared_match["spread"][event1["team1"]]]
                shared_match["spread"][event1["team2"]]["src"] = ref[i]
                shared_match["spread"][event1["team2"]] = [shared_match["spread"][event1["team2"]]]
                shared_match["moneyline"][event1["team1"]]["src"] = ref[i]
                shared_match["moneyline"][event1["team1"]] = [shared_match["moneyline"][event1["team1"]]]
                shared_match["moneyline"][event1["team2"]]["src"] = ref[i]
                shared_match["moneyline"][event1["team2"]] = [shared_match["moneyline"][event1["team2"]]]
                shared_match["points"][event1["team1"]]["src"] = ref[i]
                shared_match["points"][event1["team1"]] = [shared_match["points"][event1["team1"]]]
                shared_match["points"][event1["team2"]]["src"] = ref[i]
                shared_match["points"][event1["team2"]] = [shared_match["points"][event1["team2"]]]
                shared.append(shared_match)

    return shared