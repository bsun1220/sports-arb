import React from "react";
import "./card.css";

export default function Card(props){
    return(
    <div className = {"card"}>
        <h1 style = {{"color":"black", "fontWeight":"bold"}}> MATCH</h1>
        <hr style = {{"backgroundColor":"black", "width":"100%"}}/>
        <h1 style = {{"color":"black"}}> Spread</h1>
        <p style = {{"color":"gray", "margin":"0px"}}>Hello</p>
        <p style = {{"color":"gray", "margin":"0px"}}>Hello</p>
        <h1 style = {{"color":"black"}}> Money Line</h1>
        <p style = {{"color":"gray", "margin":"0px"}}>Hello</p>
        <p style = {{"color":"gray", "margin":"0px"}}>Hello</p>
        <h1 style = {{"color":"black"}}> Points </h1>
        <p style = {{"color":"gray", "margin":"0px"}}>Hello</p>
        <p style = {{"color":"gray", "margin":"0px"}}>Hello</p>
    </div>)
}