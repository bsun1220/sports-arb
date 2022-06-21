import React, {useEffect, useState}from "react";
import Card from "./card";
import "./content.css"
import axios from "axios"

export default function Content(){

    const [data, setData] = useState("");
    const [element, setElement] = useState("");

    useEffect(()=>{
        const func = async() =>{
            const request = await axios.get("https://sportsarb.herokuapp.com/sports");
            setData(request.data[0]["data"]);
        };
        func();
    },[])


    useEffect(()=>{
        if(data !== ""){
            const list = [];
            data.forEach((match) => {
                list.push(<Card key = {match.match} src = {match}/>)
            })
            setElement(list);
        }
    },[data]);

    return(<div id = {"content"}>
        <h1>Opportunities of The Day</h1>
        <hr/>
        {element}
    </div>)
}