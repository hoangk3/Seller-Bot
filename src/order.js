const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
  tk: { type: String, required: true },
  mk: { type: String, required: true },
  orderCode: { type: String, required: true, unique: true }, 
  type: { type: String, required: true },
  apiKey: { type: String, required: true },
  apiKeyMain: { type: String, required: true, default: 'main' },
  createdAt: { type: Date, default: Date.now }, 
});

const Order = mongoose.model('Order', orderSchema);

module.exports = Order;
