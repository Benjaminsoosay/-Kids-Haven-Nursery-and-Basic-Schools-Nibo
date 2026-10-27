// Automatically update the footer year
document.addEventListener("DOMContentLoaded", function() {
    var yearSpan = document.getElementById("currentYear");
    if (yearSpan) {
        yearSpan.innerText = new Date().getFullYear();
    }
});