var hideColon = false;
var seperator = ":";

function clock() {
    seperator = hideColon ? " " : ":";
    hideColon = hideColon ? false : true;

    var d = new Date();
    hours = String(d.getHours()).padStart(2, "0");
    minutes = String(d.getMinutes()).padStart(2, "0");
    
    var time = hours + seperator + minutes;
    document.querySelector("#clock").innerHTML = time;
    
    t = setTimeout(() => {
	clock();
    }, 1000);
}
