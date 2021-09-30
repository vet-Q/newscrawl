const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const express = require('express');
const bodyParser = require('body-parser');
const { html } = require('cheerio/lib/api/manipulation');


app = express();

app.use(express.static('./'));
// app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : true}));

app.get('/data',async(req, res)=>{
    const data = await NewsConcate(disease='African swine fever');
    res.send(data)
})

app.post('/data',async(req,res)=>{
    let disease = req.body.diseaseInfo?req.body.diseaseInfo:'African swine fever';
    console.log(disease)
    const data = await NewsConcate(disease);
    let wantdata = JSON.stringify(data);
    wantdata = JSON.parse(wantdata);
    wantdata = wantdata[disease]
    res.render('good',{title:"HELLO",diseaseInfo:wantdata})
})

app.listen(3000,()=>{
    console.log('3000번 포트에서 실행중입니다.')
})

const getHtml = async(disease) => {
    const disease1 = disease
    let URL = 'https://medisys.newsbrief.eu/rss/'
    const data = await axios.get(URL,{params:{ 
        type:`search`,
        mode:`advanced`,
        language:`en`,
        atLeast:`${disease}`}
    });
    const $ = cheerio.load(data.data, {xmlMode:true});

    const result = [];

    $('item').each(function(){
        let newsOne= {};
        newsOne.title = $(this).children('title').text();
        newsOne.link = $(this).children('link').text();
        newsOne.pubDate = $(this).children('pubDate').text();
        newsOne.category = $(this).children('category').text();
        result.push(newsOne);
    })

    return result
}


const NewsConcate = async(disease)=>{
    let dis = disease;
    const wantTotal = {};
    const newsList = ['African swine fever']
    const data = await getHtml(dis);
    wantTotal[`${dis}`] = data
    // console.log(wantTotal)
    return wantTotal
}

