// method 1 using general function 
// console.log(click)

click.addEventListener('click' , function() {
    alert("Hellow World")
} )

// method  2

let click_function = document.getElementById('click-function')
click_function.addEventListener('click-function', display)
 function display (){
    alert("Helloew World Function ")
 }
// method 3
 function sayhello(){
    alert("Hello World")
 }

// on mouse over and mouse out
// function over(){
//     document.write ("Mouse Over");
// }
// function out(){
//     document.write ("Mouse Out");
// }

function bigImg(x){
    x.style.height = "64px";
    x.style.width = "64px";
}

function normalImg(x){
    x.style.height = "32px";
    x.style.width = "32px";
}

// onfocus event
function fun(x){
   x.style.background = "blue";
}

// on blur
function myfunction() {
    let x = document.getElementById("lname");
    x.value = x.value.toUpperCase();
}
// on contextmenu
// Prevent default context menu:
// const div = document.getElementById("div1")
// div.addEventListener("contextmenu",(e) => {e.preventDefault()});

// Show hidden content:
function myfun() {
    const div = document.getElementById("div2");
    div.style.visibility = "visible";
}
// onsubmit
function submit_function() {
    alert("This name was submitted")
}

// AddEventlistner
document.getElementById("mybtn").addEventListener("click", displayDate);
function displayDate() {
    document.getElementById("ptag").innerHTML = Date ();
}

// multiple events use to the same button(element) 
var y = document.getElementById("btn");
y.addEventListener("click", myfunction1);
y.addEventListener("click",secondfunction);

function myfunction1() {
    alert("hellow first click")
}
function secondfunction() {
    alert("thank you click on second time");
}

// on double click event
function double() {
    document.getElementById("dbl_click").innerHTML += "Hellow Double click";
}