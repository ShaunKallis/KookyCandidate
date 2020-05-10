var cookies = document.cookie.split('=');
var counter = parseInt(cookies[1]) ;
var body = document.getElementsByTagName("body")[0];


body.onclick = function(){
    if(counter<50){
        console.log(counter);
        counter++;
        document.cookie = 'count='+counter;
        } 
}
