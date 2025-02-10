//const express = reqire('express');
import express from 'express';
import __dirname from './util/rootpath.js'

const app = express();

app.get('/', (req, res) => {
    res.send('szep napot'); //localhost:3000
});

app.get('/', (req, res) => {
    res.send('<h1>hello world!</h1>'); //localhost:3000/hello
});

app.get('/index', (req, res) => {
    res.send('./views/index.html');             //localhost:3000
});

app.listen(3000, () => {
    console.log('server runs on port 3000');
});