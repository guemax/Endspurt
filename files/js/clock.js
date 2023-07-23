var hideColon = false;
var seperator = ":";

function clock() {
    var d = new Date();
    
    seperator = hideColon ? ":" : " ";
    hideColon = hideColon ? false : true;
    
    var time = d.getHours() + seperator + d.getMinutes();
    
    document.querySelector("#clock").innerHTML = time;
    t = setTimeout(() => {
	clock();
    }, 1000);
}
