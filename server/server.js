const express = require("express");
const app = express();
const cors = require("express");
const bodyParser = require("body-parser");

const port = process.env.PORT || 5000
app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});

app.get("/", (req, res) => {
    res.send("Hello");
})