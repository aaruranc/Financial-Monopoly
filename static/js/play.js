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
//            console.log('YERRRRRR');
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
//    console.log(data);
//    
//    console.log('YEEEEEET');
//    
    var confirm = window.confirm(`${player_name} turn to roll`);
    if(confirm === true){
        
        $.ajax({
            url: '/roll',
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',

            success: function (response) {
                
//                console.log('YEEEEEET');
//                console.log(response);
//                roll_num = response['roll_num'];
//                position = response['position'];
//                
//                var roll_info = `${player_name} rolled ${roll_num} - Now at ${position}`;
//                var confirm = window.confirm(roll_info);
//                
//                console.log('YEEEEEET');
                generate_actions(response);
                

            },
            error: function (error) {
                console.log(`Error ${error}`);
            }
        });   
    }
    
    return
        
}


function generate_actions(data){
    
    // Player chooses action relative to game state
    // Defining this needs to be scoped out on server side
    // For now just having players move across board
            
//    console.log('Got HERE');
//    console.log(data)
    
    
    $.ajax({
        url: '/action',
        type: "POST",
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json;charset=UTF-8',

        success: function (response) {
            
//            console.log(response);
            
            make_decision(response);
        
//            roll(response);

        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });  
    
    
    return
    
}


function make_decision(data){

    $.ajax({
        url: '/decision',
        type: "POST",
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json;charset=UTF-8',

        success: function (response) {
            
            console.log(response);
            
//            console.log('SIZZURP')

            roll(response);

        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });  
    


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