document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("new").onclick = function() {
        window.location.href = "/staff/create";
        console.log("Button clicked");
    };
}); 

console.log("Script loaded");