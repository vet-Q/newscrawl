const express = require('express');
const {spawn} = require('child_process');
const PORT = process.env.PORT || 5000
const bodyParser = require('body-parser');

const app = express();

app.use(express.static('./'));
// app.set('views', path.join(__dirname, 'views'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : true}));

app.get('/data', (req, res) => {
    // 스크래핑 작업 수행
    let dataTosend;
    const python = spawn('python',['main.py']);
    python.stdout.on('data', (data)=>{
        console.log(data.toString());
        res.send('hello')
    })
    python.on('close',(code)=>{
        console.log('작업완료');
    })
   
})

app.listen(PORT, () => console.log(`Listening on ${PORT}`))