import React, { useEffect, useState} from "react";
import "./card.css";

export default function Card(props){

    const [slist, setSList] = useState("");
    const [mlist, setMList] = useState("");
    const [plist, setPList] = useState("");

    useEffect(()=> {
        const team1 = props.src.team1;
        const team2 = props.src.team2;
        const spread = props.src.spread;
        const spread1odds = spread[team1]["odds"];
        const spread2odds = spread[team2]["odds"];

        const spreadsMarketMargin = 1/spread1odds + 1/spread2odds;
        const pstyle = {"color":"gray", "margin":"0px", "wordWrap":"wrap", "textAlign":"left"};
        
        if(spreadsMarketMargin < 1){
            const list = []
            list.push(<p key = {Math.random()} style = {pstyle}>Arbitrage Found!</p>);
            const spreadtext = `Spread was ${spread[team1]["amount"]} and ${spread[team2]["amount"]}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{spreadtext}</p>);
            const team1text = `Team1: ${team1} from ${spread[team1]["src"].toUpperCase()}`;
            const team2text = `Team2: ${team2} from ${spread[team2]["src"].toUpperCase()}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{team1text}</p>);
            list.push(<p key = {Math.random()} style = {pstyle}>{team2text}</p>);
            const stake1 = Math.round((1000 * 1/spread1odds)/spreadsMarketMargin * 100)/100;
            const stake2 = Math.round((1000 * 1/spread2odds)/spreadsMarketMargin * 100)/100;
            const staketext = `You must invest $${stake1} and $${stake2} respectively`;
            list.push(<p key = {Math.random()} style = {pstyle}>{staketext}</p>);
            const profit = (1 - spreadsMarketMargin) * 1000;
            const profittext = `Expected Profit is $${Math.round(profit * 100)/100}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{profittext}</p>);
            setSList(list);
        }
        else{
            const list = []
            list.push(<p key = {Math.random()} style = {pstyle}>Arbitrage Not Found!</p>);
            const spreadtext = `Spread was ${spread[team1]["amount"]} and ${spread[team2]["amount"]}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{spreadtext}</p>);
            const team1text = `Team1: ${team1} with odds of ${Math.round(spread1odds * 100)/100} from ${spread[team1]["src"].toUpperCase()}`;
            const team2text = `Team2: ${team2} with odds of ${Math.round(spread2odds * 100)/100} from ${spread[team2]["src"].toUpperCase()}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{team1text}</p>);
            list.push(<p key = {Math.random()} style = {pstyle}>{team2text}</p>);
            setSList(list);
        }

        const moneyline = props.src.moneyline;
        const money1odds = moneyline[team1]["odds"];
        const money2odds = moneyline[team2]["odds"];
        const moneyMarketMargin = 1/money1odds + 1/money2odds;

        if(moneyMarketMargin < 1){
            const list = []
            list.push(<p key = {Math.random()} style = {pstyle}>Arbitrage Found!</p>);
            const team1text = `Team1: ${team1} from ${moneyline[team1]["src"].toUpperCase()}`;
            const team2text = `Team2: ${team2} from ${moneyline[team2]["src"].toUpperCase()}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{team1text}</p>);
            list.push(<p key = {Math.random()} style = {pstyle}>{team2text}</p>);
            const stake1 = Math.round((1000 * 1/money1odds)/moneyMarketMargin * 100)/100;
            const stake2 = Math.round((1000 * 1/money2odds)/moneyMarketMargin * 100)/100;
            const staketext = `You must invest $${stake1} and $${stake2} respectively`;
            list.push(<p key = {Math.random()} style = {pstyle}>{staketext}</p>);
            const profit = (1 - moneyMarketMargin) * 1000;
            const profittext = `Expected Profit is $${Math.round(profit * 100)/100}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{profittext}</p>);
            setMList(list);
        }
        else{
            const list = []
            list.push(<p key = {Math.random()} style = {pstyle}>Arbitrage Not Found!</p>);
            const team1text = `Team1: ${team1} with odds of ${Math.round(money1odds * 100)/100} from ${moneyline[team1]["src"].toUpperCase()}`;
            const team2text = `Team2: ${team2} with odds of ${Math.round(money2odds * 100)/100} from ${moneyline[team2]["src"].toUpperCase()}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{team1text}</p>);
            list.push(<p key = {Math.random()} style = {pstyle}>{team2text}</p>);
            setMList(list);
        }


        const points = props.src.points;
        const points1odds = points[0]["odds"]
        const points2odds = points[1]["odds"];
        const pointsMarketMargin = 1/points1odds + 1/points2odds;

        if(pointsMarketMargin < 1){
            const list = []
            list.push(<p key = {Math.random()} style = {pstyle}>Arbitrage Found!</p>);
            const team1text = `${points[0]["amount"]} from ${points[0]["src"].toUpperCase()}`;
            const team2text = `${points[1]["amount"]} from ${points[1]["src"].toUpperCase()}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{team1text}</p>);
            list.push(<p key = {Math.random()} style = {pstyle}>{team2text}</p>);
            const stake1 = Math.round((1000 * 1/points1odds)/pointsMarketMargin * 100)/100;
            const stake2 = Math.round((1000 * 1/points2odds)/pointsMarketMargin * 100)/100;
            const staketext = `You must invest $${stake1} and $${stake2} respectively`;
            
            list.push(<p key = {Math.random()} style = {pstyle}>{staketext}</p>);
            const profit = (1 - pointsMarketMargin) * 1000;
            const profittext = `Expected Profit is $${Math.round(profit * 100)/100}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{profittext}</p>);
            setPList(list);
        }
        else{
            const list = []
            list.push(<p key = {Math.random()} style = {pstyle}>Arbitrage Not Found!</p>);
            const team1text = `${points[0]["amount"]} with odds of ${Math.round(points1odds * 100)/100} from ${points[0]["src"].toUpperCase()}`;
            const team2text = `${points[1]["amount"]} with odds of ${Math.round(points2odds * 100)/100} from ${points[1]["src"].toUpperCase()}`;
            list.push(<p key = {Math.random()} style = {pstyle}>{team1text}</p>);
            list.push(<p key = {Math.random()} style = {pstyle}>{team2text}</p>);
            setPList(list);
        }

    },[props]);

    return(
    <div className = {"card"}>
        <h1 style = {{"color":"black", "fontWeight":"bold", "marginInline":"auto"}}>{props.src.match}</h1>
        <hr style = {{"backgroundColor":"black", "width":"100%"}}/>
        <h1 style = {{"color":"black", "marginInline":"auto"}}> Spread</h1>
        {slist}
        <h1 style = {{"color":"black", "marginInline":"auto","marginTop":"10px"}}> Money Line</h1>
        {mlist}
        <h1 style = {{"color":"black", "marginInline":"auto","marginTop":"10px"}}> Points </h1>
        {plist}
    </div>)
}