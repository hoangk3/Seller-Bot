const mongoose = require('mongoose');

const accountSchema = new mongoose.Schema({
  tk: { type: String, required: true },
  mk: { type: String, required: true },
  apiKey: { type: String, required: true }, 
  createdAt: { type: Date, default: Date.now },
});

const Account = mongoose.model('Account', accountSchema);

module.exports = Account;
