const a=require("express")
const chalk=require("chalk") 
const path=require("path")
var app=a();
const booksrouter=a.Router();

app.set('views','./src/views');
app.set('view engine','ejs');
app.use(a.static(path.join(__dirname,"/public")));
booksrouter.route('/')
.get((req,res)=>{
    res.render('books',{nav:[
        {link:'/books',title:"Books"},
        {link:'/authors',title:"Authors"}],title:"Books"})
})
;
booksrouter.route('/single')
.get((req,res)=>{
    res.send("hello single book")
})
app.use('/books',booksrouter)
app.get('/',(req,res)=>{
    res.render('index',{nav:[
        {link:'/books',title:"Books"},
        {link:'/authors',title:"Authors"}],title:"library"})
})
app.listen(3000,()=>{
    console.log("listening to the port"+chalk.cyan('3000'));
});