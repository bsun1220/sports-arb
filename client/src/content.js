import React from "react";
import Card from "./card";
import "./content.css"

export default function Content(){
    return(<div id = {"content"}>
        <h1>Opportunities of The Day</h1>
        <hr/>
        <Card/>
        <Card/>
    </div>)
}