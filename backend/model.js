// backend/models/binDataModel.js
const mongoose = require('mongoose');

const binDataSchema = new mongoose.Schema({
  time: String,
  fillLevel: Number
});

// Create and export the model
const BinData = mongoose.model('BinData', binDataSchema);
module.exports = BinData;

