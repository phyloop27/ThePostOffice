// Function to create a muser message to count down untill redirect time occurs.

// have to set a constant for the URL home route for JS to work correctly
const homeUrl = 'home';
let seconds = 5;

const countdown = setInterval(function() {
    // telling 'seconds' to minus each time
    seconds -- ;

    // find element 'countdown' which is my div container
    document.getElementById("countdown").textContent = seconds;

    // redirect on the '0' condition
    if (seconds <= 0) {
        clearInterval(countdown);
        window.location.href = homeUrl;
    }
}, 1000);
