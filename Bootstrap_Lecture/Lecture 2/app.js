// const navbar = document.querySelector('.navbar');
const html_element = document.querySelector('html');

console.dir(html_element)

localStorage.setItem('themeMode')

html_element.setAttribute("data-bs-theme", "dark")
