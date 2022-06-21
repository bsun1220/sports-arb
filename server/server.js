const express = require("express");
const app = express();
const cors = require("cors");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const port = process.env.PORT || 5000;
const uri = process.env.ATLAS_URI || "mongodb+srv://bsun1220:jrabbit11@cluster0.pzxdkfx.mongodb.net/?retryWrites=true&w=majority";

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

mongoose.connect(uri,{
    useNewUrlParser: true,
    useUnifiedTopology:true
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error: "));
db.once("open", function () {
  console.log("Mongoose Connected Successfully");
});

const Schema = mongoose.Schema;

const DataSchema = new Schema({
    data:{
    }
})

const Data = mongoose.model("Data", DataSchema);

const Router = express.Router();
Router.get("/sports", async(req, res) =>{
    const data = await Data.find({});
    try{
        res.send(data);
    }
    catch(error){
        res.status(500).send(error);
    }
});

Router.post("/sports", async(req, res) => {
    const data = new Data(req.body);
    try{
        await data.save();
        res.send("Success");
    }
    catch (error){
        res.status(500).send(error);
    }
});

Router.put("/sports", async(req, res) => {
    const newData = req.body.data;
    await Data.updateOne({}, {
        data: newData
      });
    res.send("Success");
});

app.use(Router);

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});

app.get("/", (req, res) => {
    res.send("Hello");
})
