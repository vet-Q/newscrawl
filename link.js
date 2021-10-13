const express = require('express');
const {spawn} = require('child_process');
const PORT = process.env.PORT || 5000
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();

app.use(express.static('./'));
// app.set('views', path.join(__dirname, 'views'));
app.use(bodyParser.urlencoded({extended : true}));


class DBMaker {
    constructor(host, PORT, user, password, databases){
        this.host= host,
        this.port=PORT,
        this.user=user,
        this.password=password,
        this.database=databases 
    }

    conn() {
        const connection = mysql.createConnection({
                host:'localhost',
                user:'root',
                password:'DJPY!',
                database:'djpy',
        })
        return connection.connect();
    }
}

let con = new DBMaker('localhost', '3306', 'root', 'DJPY!', 'djpy')
let connect = con.conn();

console.log(connect)


app.get('/data', (req, res) => {
    // 스크래핑 작업 수행
    const python = spawn('python',['main.py']);
    python.stdout.on('data', (data)=>{
        let datas = data.toString();
        return res.send(datas);
    })
    python.on('close',(code)=>{
        return console.log('end');
    })
   
})



// connect.query('SELECT * from datas limit 10', function(err,result,fields){
//     if(err){
//         console.log(err);
//     }
//     console.log(result)
// })

// con.end()


app.listen(PORT, () => console.log(`Listening on ${PORT}`))