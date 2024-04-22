const form = document.getElementById("form");

const API_KEY = '745c41598fe4760bd586e1009ecedc45';
const UNIT = 'metric';

form.addEventListener("submit", async function (e) {
    e.preventDefault();

    let city_name = document.getElementById("city_name").value;
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&units=${UNIT}&appid=${API_KEY}` // template literals or string literal

    // Parameters Used
    // q = city_name/lahore
    // units = metric
    // appid = API_KEY

    if(city_name == '') {
        alert('Kindly enter a valid city name');
    }
    else {
        // fetch weather data
        let response = await fetch(url);
        let data = await response.json();

        console.log(data);

        get_time(data);

        get_temp(data);

        get_loc(data);

        get_feels_like_temp(data);

        get_humidity(data);

        get_pressure(data);
    }
})


function get_time(data) {
    let months_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    let date_dt = data.dt * 1000;
    let date_time = new Date(date_dt);

    const month_index = date_time.getMonth();
    const month = months_array[month_index];

    const current_date = date_time.getDate();
    const current_hours = date_time.getHours();
    const minutes = date_time.getMinutes();

    // Feb 27, 19:41
    const final_date = `${month} ${current_date}, ${current_hours}:${minutes}`;

    console.log(final_date);

    const date_element = document.getElementById("date");
    date_element.innerHTML = final_date;
}



const get_temp = (data) => {
    const temp_element = document.getElementById("temp");

    temp_element.innerText = `Temp: ${data.main.temp} C`;
}


const get_loc = (data) => {
    const loc_element = document.getElementById("loc");

    loc_element.innerText = `City: ${data.name}, ${data.sys.country}`;
}

const get_feels_like_temp = (data) => {
    const feels_like_element = document.getElementById("feels_like_temp");
    feels_like_element.innerHTML = `Feels Like Temp: ${data.main.feels_like} C`;
}


function get_humidity (data) {
    const humidity_element = document.getElementById("humidity");
    humidity_element.innerText = `Humidity: ${data.main.humidity}%`;
}

function get_pressure(data) {
    const pressure_element = document.getElementById("pressure");
    pressure_element.innerHTML = `Pressure: ${data.main.pressure} Pascal`;
}

// synchronous function
// function getWeather () {
    // some code
// }

// asynchronous function
// async function getWeather () {
    // some code
// }


// asynchronous arrow function
// const getWeather = async () => {
//     // some code
// }