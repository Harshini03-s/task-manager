document.getElementById("signup-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form from refreshing the page

    let username = event.target[0].value;
    let email = event.target[1].value;
    let password = event.target[2].value;

    if (username && email && password) {
        localStorage.setItem("user", JSON.stringify({ username, email, password }));
        alert("Signup successful! You can now login.");
        window.location.href = "login.html";
    } else {
        alert("Please fill in all fields.");
    }
});
