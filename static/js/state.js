window.onload = function (){
    load_state();
}

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function isEmpty(obj) {
  return Object.keys(obj).length === 0;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


function load_state(){
    

    $.ajax({
        url: '/state',
        type: "POST",
        dataType: 'json',
        data: JSON.stringify({}),
        contentType: 'application/json;charset=UTF-8',
        
        success: function (response) {            
            console.log(response);
            populate(response);

        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });
    return
    
}



async function populate(data){
   
    var parent = document.getElementById('wrapper');
    
//    while (parent.firstChild) {
//        parent.removeChild(parent.lastChild);
//    }
    
    for (i in data['players']){
    
        var temp = document.getElementById(`Player${i}`);
        if (temp){
            temp.remove()     
        }
        
        let div = document.createElement('div');
        div.id = `Player${i}`;
        parent.appendChild(div);
    
        let h2 = document.createElement('h2');
        h2.innerHTML = data['players'][i]['name'];
        div.append(h2);
        
//        console.log(data['players'][i]);
        
        const attributes = ['capital', 'orbit', 'position'];
        for (j in attributes){
            
            attribute = attributes[j];
            val = data['players'][i][attribute];
            let p = document.createElement('p');
            p.name = attribute;
            p.innerHTML = `${capitalize(attribute)}: ${val}`;
            div.append(p);
        };
        
        let p = document.createElement('p');
        p.name = 'monopoly';
        
        let mply = data['players'][i]['monopoly']
        if (isEmpty(mply)){
            p.innerHTML = 'Monopoly: None';
        }
        else{
            
            // List Monopolies
            console.log('YEET')
            p.innerHTML = data['players'][i]['monopoly'];
            
        };
        
        div.append(p);    
//        parent.appendChild(document.createElement('br'));
    
    }
    
    let secs = 1
    await sleep(secs * 1000)
    load_state()
    
//    parent.appendChild(form);
//    
//    var child = document.getElementById('player_form');
    
    
    return
    
}