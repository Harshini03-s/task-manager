document.addEventListener("DOMContentLoaded", function () {
    let statusList = document.getElementById("status-list");

    function loadStatuses() {
        let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        statusList.innerHTML = "";
        tasks.forEach((task) => {
            let li = document.createElement("li");
            li.innerHTML = `${task.title} - <strong>${task.status}</strong>`;
            statusList.appendChild(li);
        });
    }

    loadStatuses();
});
