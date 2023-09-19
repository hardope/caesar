const express = require('express')
const Database = require('./storage')
const app = express();

app.use(express.json())

const db = new Database()

app.get('/', (req, res) => {
    res.send('Hello World!')
    return
})

app.get('/users', (req, res) => {
    res.send(db.get_all())
    return
})

app.get('/user/:id', (req, res) => {
    const user = db.get_one(req.params.id)
    if(!user) return res.status(404).send('The user with the given ID was not found.')
    res.send(user)
    return
})

app.post('/user', (req, res) => {
    data = db.new(req.body)
    if (data.error) return res.status(400).send(data.error)
    res.send(data)
    return 
})

app.put('/user/:id', (req, res) => {
    const user = db.update(req.params.id, req.body)
    if(!user) return res.status(404).send('The user with the given ID was not found.')
    if (user.error) return res.status(400).send(user.error)
    res.send(user)
    return
})

app.delete('/user/:id', (req, res) => {
    const user = db.delete(req.params.id)
    if(!user) return res.status(404).send('The user with the given ID was not found.')
    res.send(user)
    return
})

const port = process.env.PORT || 3000;
app.listen(port, () => {console.log(`The application is running on localhost:${port}!`)})