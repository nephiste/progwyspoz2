function removeTasks() {
    localStorage.clear();
    displayTasks();
}

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const task = taskInput.value.trim();

    if (task === "") {
        alert("Proszę wpisać nazwę zadania!");
        return;
    }

    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    const newTask = {
        name: task,
        completed: false
    };

    tasks.push(newTask);
    localStorage.setItem("tasks", JSON.stringify(tasks));

    taskInput.value = "";
    displayTasks();
}

function displayTasks() {
    const taskList = document.getElementById("taskList");
    taskList.innerHTML = "";

    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    if (tasks.length === 0) {
        const noTasksMessage = document.createElement("li");
        noTasksMessage.textContent = "Brak zadań do wyświetlenia.";
        taskList.appendChild(noTasksMessage);
        return;
    }

    tasks.forEach(function(task, index) {
        const li = document.createElement("li");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = task.completed;
        checkbox.onclick = function() {
            toggleTaskCompletion(index);
        };

        const taskText = document.createElement("span");
        taskText.textContent = task.name;
        taskText.style.textDecoration = task.completed ? 'line-through' : 'none';

        li.appendChild(checkbox);
        li.appendChild(taskText);
        taskList.appendChild(li);
    });
}

function toggleTaskCompletion(index) {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks[index].completed = !tasks[index].completed;
    localStorage.setItem("tasks", JSON.stringify(tasks));
    displayTasks();
}

window.onload = function() {
    displayTasks();
};
