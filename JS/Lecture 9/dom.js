// get element by id

let para = document.getElementById("paragraph")
console.log(para);
console.dir(para);

// para.innerHTML = "<i>This is text</i> using javascript" // renders as html
para.innerText = "<i>This is text</i> using javascript" // renders as normal text


// get element by classname
let headings = document.getElementsByClassName("heading")
console.log(headings)

headings[0].style.color = "Blue";

headings[1].style.backgroundColor = "yellow"

headings[2].style.fontWeight = "lighter"


// get element by tag name
let subheadings = document.getElementsByTagName("h2");
console.log(subheadings);

subheadings[0].innerHTML = "This is new sub heading"


// get element by query

let box = document.querySelector("#box");
box.innerHTML = "<p>This is a paragraph inside a box</p>";
box.style.border = "1px solid black";
box.style.backgroundColor = "lightgreen";


let ptags = document.querySelectorAll(".para");
console.log(ptags);