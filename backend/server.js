// backend/server.js

const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const BinData = require('./models/binDataModel');  // Import the model

const app = express();
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect("mongodb://localhost:27017/iotOverflow", { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("Could not connect to MongoDB", err));

// POST route to save bin data
app.post("/saveBinData", async (req, res) => {
  const { time, fillLevel } = req.body;

  const newBinData = new BinData({
    time,
    fillLevel,
  });

  try {
    await newBinData.save();
    res.status(201).send("Bin data saved successfully");
  } catch (error) {
    res.status(400).send("Error saving bin data");
  }
});

// GET route to fetch bin data
app.get("/getBinData", async (req, res) => {
  try {
    const binData = await BinData.find();
    res.json(binData);
  } catch (error) {
    res.status(400).send("Error fetching bin data");
  }
});

// Start the server
app.listen(5001, () => console.log("Server running on port 5001"));
