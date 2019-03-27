function ans()
{
    var x= parseInt(document.getElementById("a").value);
var y= parseInt( document.getElementById("b").value);
var opt=document.getElementById("opt").value;

if (opt=="add")
{
    z=x+y;
}     
else if(opt=="sub") 
{
    z=x-y;
}
else if(opt=="mul") 
{
    z=x*y;
}
else
{
    z=x/y;
}

            


  console.log(z);
  document.getElementById("answ").innerHTML=z ;
}