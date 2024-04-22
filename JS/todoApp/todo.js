let form = document.getElementById('form')
// get todo from local storage

let current_todo = localStorage.getItem('todo_list')
let  todo_list = document.getElementById('todo_list')
todo_list.innerHTML = current_todo
// console.log(current_todo)

form.addEventListener('submit', function(e){
    e.preventDefault()

    // get new todo value from input
    let new_todo_item = document.getElementById('todo').value
    if (new_todo_item == ''){
        alert('Enter the valid task. ')
    }else {
        // create new li element
        let new_li = document.createElement('li')
        new_li.innerHTML ='<span>'+new_todo_item+'</span> <button  type = "button" id="delete_btn">X</button>'

      // apend li in ul tag 

     let todo_list = document.getElementById('todo_list')
     todo_list.append(new_li)

     // save list in local storage 
       

     add_todo()
     li_events()
    }  

})

function li_events(){
    // get all li for loop
    let lis = document.querySelectorAll('li')
    for(li in lis){

        let list = lis[li]

        list.children[0].addEventListener('click', function(){
            // this classlist marked
            this.classlist.add('marked')
            add_todo()
        })

        list.children[1].addEventListener('click',function(){
            list.remove()
            add_todo()
        })
    }
}

function add_todo(){
    //save list in local storage
    let list = document.getElementById('todo_list').innerHTML
    localStorage.setItem('todo_list',list)
}

li_events()