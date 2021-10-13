const mariadb = require('mariadb');

class DBMaker {
    constructor(host, PORT, user, password, databases) {
        this.host= host,
        this.port=PORT,
        this.user=user,
        this.password=password,
        this.database=databases 
    }
    async conn() {

        const pool = mariadb.createPool({
            host:this.host,
            user:this.user,
            password:this.password,
            database:this.database,
        })

        let connected = await pool.getConnection();
        connected.query('USE djpy');
        let rows = await connected.query('SELECT * from datas')
        // let data = await JSON.stringify(rows,null,2);
        console.log(rows);
        return rows;
    }   
}

let con = new DBMaker('127.0.0.1','3306','root','DJPY!','djpy')

con.conn()
