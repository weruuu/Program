var c_id = "AAA"
var c_hp = 100
var c_mp = 200
var c_storage = 50
var map = [["map0-1","map0-2","null","null","null","null"],
            ["map2-1","map2-2","null","null","null","null"]];
var current_map = 0

function Init(){
    document.getElementById("ID").innerText = c_id;
    document.getElementById("HP").innerText = c_hp;
    document.getElementById("MP").innerText = c_mp;
    document.getElementById("Storage").innerText = c_storage;
    for (i=0;i<6;i++) {
        document.getElementById("map" + current_map + "-" + (i+1)).innerText = map[current_map][i];
    }
}

function Lastmap(){
    var lastmap = document.getElementById("lastmap");
    lastmap.onclick = function(){
        console.log('click')
        if(current_map>0){
            current_map -= 1;
            for (i=0;i<6;i++) {
                document.getElementById("map" + current_map + "-" + (i+1)).innerText = map[current_map][i];
            }
        }
        else{
            alert('now is 1!')
        }
    }


}

function Lastmap(){
    document.getElementById("map0-1").innerText = map[0];
    document.getElementById("map0-2").innerText = map[1];
    document.getElementById("map0-3").innerText = map[2];
    document.getElementById("map0-4").innerText = map[3];
    document.getElementById("map0-5").innerText = map[4];
    document.getElementById("map0-6").innerText = map[5];
}