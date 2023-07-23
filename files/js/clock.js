var hideColon = false;
var separator = ":";

function clock() {
    separator = hideColon ? " " : ":";
    hideColon = hideColon ? false : true;

    var d = new Date();
    hours = String(d.getHours()).padStart(2, "0");
    minutes = String(d.getMinutes()).padStart(2, "0");
    
    var time = hours + separator + minutes;
    document.querySelector("#clock").innerHTML = time;
    
    t = setTimeout(() => {
	clock();
    }, 1000);
}
