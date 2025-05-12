const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.PORT || 3000;
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/mydb';

mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('Mongo connection error:', err));

app.get('/', (req, res) => {
    res.send('Hello from Node.js + MongoDB app! 🟢');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
