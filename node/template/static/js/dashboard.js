document.addEventListener("DOMContentLoaded", function () {
    let taskList = document.getElementById("task-list");
    let addTaskButton = document.getElementById("add-task");

    function loadTasks() {
        let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        taskList.innerHTML = "";
        tasks.forEach((task, index) => {
            let li = document.createElement("li");
            li.innerHTML = `${task.title} <span>${task.status}</span>`;
            taskList.appendChild(li);
        });
    }

    addTaskButton.addEventListener("click", function () {
        let taskTitle = prompt("Enter Task Title:");
        if (taskTitle) {
            let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
            tasks.push({ title: taskTitle, status: "Pending" });
            localStorage.setItem("tasks", JSON.stringify(tasks));
            loadTasks();
        }
    });

    loadTasks();
});
