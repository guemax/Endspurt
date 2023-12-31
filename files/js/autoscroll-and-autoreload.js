function bottomOfPageReached() {
    return (
	window.innerHeight + Math.round(window.pageYOffset)
    ) >= document.body.offsetHeight;
}

function scrollUp() {
    window.scrollTo(0, 0);
}

function scrollDown() {
    window.scrollBy(0, scroll_speed_in_px);
}

var reloadScheduled = false;

function autoScroll() {
    if (bottomOfPageReached()) {
	setTimeout(() => {
	    scrollUp();
	    if (reloadScheduled) {
		reloadScheduled = false;
		console.info("Unschedule automatic reloading of page.");
		// Timeout is necessary, otherwise browser will
		// think we haven't scrolled up yet and stay at
		// the bottom of the page forever.
		var t = setTimeout(() => {
		    location.reload();
		}, 500);
	    }
	    autoScroll();
	}, 2000);
    } else {
	scrollDown();
	setTimeout(() => {
	    autoScroll();
	}, scroll_update_timeout_in_ms);
    }
}

function automaticReload() {
    setTimeout(() => {
	console.info("Automatic reloading of page scheduled.");
	reloadScheduled = true;
	automaticReload();
    }, reload_timeout_in_ms);
}
