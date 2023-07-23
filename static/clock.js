function clock() {
    var d = new Date();
    document.querySelector("#clock").innerHTML = d.toLocaleTimeString("de-DE");
    t = setTimeout(() => {
	clock();
    }, 500);
}
