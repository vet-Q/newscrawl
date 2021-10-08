const express = require('express');
const {spawn} = require('child_process');
const PORT = process.env.PORT || 5000
const bodyParser = require('body-parser');

const app = express();

app.use(express.static('./'));
// app.set('views', path.join(__dirname, 'views'));
app.use(bodyParser.urlencoded({extended : true}));

app.get('/data', (req, res) => {
    // 스크래핑 작업 수행
    const python = spawn('python',['main.py']);
    python.stdout.on('data', (data)=>{
        let datas = data.toString();
        res.send(datas);
    })
    // python.on('close',(code)=>{
    //     console.log('end');
    // })
   
})

app.listen(PORT, () => console.log(`Listening on ${PORT}`))