let form = document.getElementById('form')
form.addEventListener('submit',function(e){
    // input validation
    // first_name validation
    
    let first_name = document.getElementById('first_name').value
    let first_name_error = document.getElementById('first_name_error')

    if (first_name == ''){
        first_name_error.innerText = 'First Name is required'
        e.preventDefault()
    } else {
        first_name_error.innerText = ''
    }
   
    let last_name = document.getElementById('last_name').value
    let last_name_error = document.getElementById('last_name_error')

    if( last_name == ''){
        last_name_error.innerText = 'Last Name is required.'
        e.preventDefault()
    }else{
        last_name_error.innerText = ''
    }

    // age validation

    let age = document.getElementById('age').value
    let age_error = document.getElementById('age_error')
    console.log(age)

    if( age <13 || age>65 ){
        console.log('age error')
        age_error.innerText = 'Age should be between 13 - 65'
        e.preventDefault()
    } else {
        age_error.innerText = ''
    }

    // phone validation
    let phone_number = document.getElementById('phone_number').value
    let phone_number_error = document.getElementById('phone_number_error')
    if (phone_number.length != 11){
        phone_number_error.innerText = 'Phone NUmber should be of 11 digit'
        e.preventDefault()
    }else {
        phone_number_error.innerText = ''
    }
    
    // email validation
    let email = document.getElementById('email').value
    let email_error = document.getElementById('email_error')

    if ( !email.includes('@') || !email.includes('.')){
        email_error.innerText = 'Kindly enter the proper email'
        e.preventDefault()
    }else {
            email_error.innerText = ''
    }

     
    // password validation
    let password = document.getElementById('password').value
    let password_error = document.getElementById('password_error')

    if (password.length < 8 ){
        password_error.innerText = 'Password should be of 8 characters'
        e.preventDefault()
    }else {
            password_error.innerText = ''
    }
   
    // confirm password

    let confirm_password = document.getElementById('confirm_password').value
    let confirm_password_error = document.getElementById('confirm_password_error')

    if (confirm_password == '' || password != confirm_password ){
        confirm_password_error.innerText = 'Password does not match'
        e.preventDefault()
    }else {
        confirm_password_error.innerText = ''
    }
    
    console.log('Form is submitted')
})

let fresher = document.getElementById('fresher')
let experienced = document.getElementById('experienced')

let education_details_div = document.getElementById('experience_div')

fresher.addEventListener('click' , function() {
    education_details_div.style.display = 'block'
    experience_div.style.display = 'none'
})

experienced.addEventListener('click' , function() {
    education_details_div.style.display = 'block'
    experience_div.style.display = 'none'
})