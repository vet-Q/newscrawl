const express = require('express');
const app = express();
 
const items = [{
    name: '우유',
    price: '2000'
}, {
    name: '홍차',
    price: '5000'
}, {
    name: '커피',
    price: '5000'
}]
 
app.use(express.static('project'));
 
app.get("/drink", (request, response) => {
    response.send(items)
})
app.post("/drink", (request, response) => {
    items.push({
        name: "테스트",
        price: "테스트"
    })
    response.send(items[items.length - 1])
})
 
app.get("/drink/:id", (request, response) => {
    const id = Number(request.params.id)
    response.send(items[id])
})
 
app.put("/drink/:id", (request, response) => {
    const id = Number(request.params.id)
    items[id].name = "테스트"
    items[id].price = 1000
    response.send(items[id])
})
 
app.delete("/drink/:id", (request, response) => {
    const id = Number(request.params.id)
    items.splice(id, 1)
    response.send("success")
})
 
app.listen(52273, () => {
    console.log('Server Running at http://127.0.0.1:52273')
})
