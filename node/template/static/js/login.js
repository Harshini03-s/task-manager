document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();

    let email = event.target[0].value;
    let password = event.target[1].value;
    let user = JSON.parse(localStorage.getItem("user"));

    if (user && user.email === email && user.password === password) {
        alert("Login successful!");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid email or password.");
    }
});
