window.onload = function (){
    start_game();
}


function start_game(){
    
    var output = {'state': 'not started'}
    
    $.ajax({
        url: '/loop',
        type: "POST",
        dataType: 'json',
        data: JSON.stringify(output),
        contentType: 'application/json;charset=UTF-8',
        
        success: function (response) {
            
//            console.log(response); 
            roll(response);

        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });
    return
    
}


function roll(data){
    
    var player_name = data['player_name'];
    console.log(data);
    
    var confirm = window.confirm(`${player_name} turn to roll`);
    if(confirm === true){
        
        $.ajax({
            url: '/roll',
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',

            success: function (response) {
                
//                console.log(response);
                roll_num = response['roll_num'];
                position = response['position'];
                
                var roll_info = `${player_name} rolled ${roll_num} - Now at ${position}`;
                var confirm = window.confirm(roll_info);
                
                choose_action(response);
                

            },
            error: function (error) {
                console.log(`Error ${error}`);
            }
        });   
    }
    
    return
        
}


function choose_action(data){
    
    // Player chooses action relative to game state
    // Defining this needs to be scoped out on server side
    // For now just having players move across board
            
    $.ajax({
        url: '/action',
        type: "POST",
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json;charset=UTF-8',

        success: function (response) {
            
//            console.log(response);
            roll(response);

        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });  
    
    
    return
    
    
    
    
    
}



function modal_window(){
    
//    var parent = document.getElementById('wrapper');
//    
//    modal = document.createElement('div');
//    modal.classList.add('modal');
//    
//    modal_content = document.createElement('div');
//    modal_content.classList.add('modal-content');
//    
//    modal_text = document.createElement('p');
//    modal_text.innerHTML = 'YA BOY FUCKING W MODALS';
//    
//    modal_content.appendChild(modal_text);
//    modal.appendChild(modal_content);
//    parent.appendChild(modal);
    
}