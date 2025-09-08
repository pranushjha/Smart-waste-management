// binDataModel.js
const mongoose = require('mongoose');

const binDataSchema = new mongoose.Schema({
  time: String,        // The time when the bin fill level was recorded
  fillLevel: Number    // The fill level of the bin (e.g., 30% full)
});

const BinData = mongoose.model('BinData', binDataSchema);

module.exports = BinData;
