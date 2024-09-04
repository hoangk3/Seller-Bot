
const mongoose = require('mongoose');

mongoose.connect('mongodb+srv://nakanohuy5:DI3R5oJpLpcY4Is3@cluster0.yxaflwl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', {
});

const db = mongoose.connection;

db.on('error', console.error.bind(console, 'Lỗi kết nối MongoDB:'));

db.once('open', function() {
  console.log('Đã kết nối đến MongoDB');
});

module.exports = db;
