alert("Whats Going ON?Q!?!?@>E");
var counter = 0;
var body = document.getElementsByTagName("body")[0];
var count = document.getElementById("count");

body.onclick = function(){
    counter++
    count.innerHTML = counter;
}
