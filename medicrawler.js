const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const ExcelJS = require('exceljs');


const URL = 'https://medisys.newsbrief.eu/rss/?type=search&mode=advanced&atLeast=african+swine+fever'


async function getHtml() {
    const x = await axios.get(URL);
    let result = {};
    let titles = [];
    let links = [];
    let pubDates = [];
    let $ = cheerio.load(x.data,{xmlMode:true});
    $('item').each(function(){
        let title, list, pubDate;
        title = $(this).children('title').text();
        list = $(this).children('link').text();
        pubDate = $(this).children('pubDate').text();
        titles.push(title);
        links.push(list);
        pubDates.push(pubDate);
    })
    result.title = titles;
    result.link = links;
    result.pubDates = pubDates;
    return result
}

const writefiles = async(filename)=>{
    const workbook = new ExcelJS.Workbook();
    const worksheet = workbook.addWorksheet();

    const {title,link,pubDates} = await getHtml();

    const serialNum = [];    
    for (i=1; i<101; i++){
        serialNum.push(i);
    };
    console.log(serialNum)

    const rawData = [{header: '연번', data: serialNum},
                     {header: 'title', data: title},
                     {header: 'link', data:link},
                     {header: 'date', data:pubDates},];

    rawData.forEach((data, index) => {
        worksheet.getColumn(index + 1).values = [data.header, ...data.data];
    });
    await workbook.xlsx.writeFile(`./${filename}.xlsx`)
}


writefiles('news data')
// getHtml().then(res=> console.log(res))
module.exports = writefiles

