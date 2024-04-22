let anchor = document.getElementById("link");
console.log(anchor);

// Get Attribute method
let href_attribute = anchor.getAttribute("href");
console.log(href_attribute);

let target_att = anchor.getAttribute("target");
console.log(target_att);

let id_att = anchor.getAttribute("id");
console.log(id_att);

anchor.setAttribute("href", "https://bing.com");

href_attribute = anchor.getAttribute("href");
console.log(href_attribute);

anchor.innerHTML = "Go to Bing";


anchor.setAttribute("class", "link");

anchor.classList.remove("link");

// anchor.classList.add("border");

function toggleBorder () {
    anchor.classList.toggle("border");
}

toggleBorder();
toggleBorder();
toggleBorder();

let container = document.querySelector(".container");

console.log(container);

// creating a p element
let p_element = document.createElement('p');

p_element.innerText = "This is a paragraph inside container";

console.log(p_element);

// container.append(p_element); // linking p element to container div element


// creating a u element (underlined text)
let u_element = document.createElement("u");
u_element.innerText = "This is an underlined text";

container.append(p_element, u_element); // linking elements to container


let box_element = document.createElement("div");
console.log(box_element)

box_element.classList.add("box");

// to add element as first child
container.prepend(box_element);

// to remove elements
anchor.remove();
u_element.remove();
box_element.remove();
container.append(box_element);


// Data Set
let data_container = document.querySelector("#data_container");
console.log(data_container);

let email = data_container.dataset.email;
let first_name = data_container.dataset.firstname;
let last_name = data_container.dataset.lastname;

console.log(email);
console.log(first_name, last_name);

data_container.dataset.subject = "JavaScript";

data_container.dataset.firstname = "Malik"

console.dir(data_container["dataset"]);