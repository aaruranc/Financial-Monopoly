function player_form(){
    
    var num_players = parseInt(document.getElementById('num_players').value);
    var parent = document.getElementById('wrapper');
    var child = document.getElementById('player_form');
    
    var action = child.action;
    parent.removeChild(child);
    
    form = document.createElement('form');
    form.id = 'player_form'
    parent.appendChild(form);
    
    for (let i = 0; i < num_players; i++) {
        label = document.createElement('label');
        label.for = `Player${i}`;
        label.innerHTML = `Player${i}`;
        form.appendChild(label);
        
        input = document.createElement('input');
        input.type = 'text';
        input.id = `Player${i}`;
        input.name = `${i}`;
        
        var player_value;
        if (i == 0){
            player_value = 'Dalio';    
        } else if (i == 1){
            player_value = 'Soros';
        }
        
        input.value = player_value;
        form.appendChild(input);
        form.appendChild(document.createElement("br"));
    }
    
    submit = document.createElement('input');
    submit.type = 'submit';
    submit.value = 'Submit';
    form.appendChild(submit);
    form.action = action;
    form.method = 'post';
//
//    console.log(form)
    
    return
}