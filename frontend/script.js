async function loadTasks() {
    const response = await fetch("http://localhost:8000/tasks");
    const tasks = await response.json();

    displayTasks(tasks);
}


function displayTasks(tasks) {

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    tasks.forEach(task => {

        const taskItem = document.createElement("div");
        taskItem.className = "task";

        const taskText = document.createElement("span");
        taskText.className = "task-text";
        taskText.textContent = task.title;

        if (task.completed) {
            taskText.style.textDecoration = "line-through";
        }

        const completeButton = document.createElement("button");

        completeButton.textContent =
            task.completed ? "Completed" : "Complete";

        completeButton.onclick = async function () {

            await fetch(
                `http://localhost:8000/tasks/${task.id}/complete`,
                {
                    method: "PUT"
                }
            );

            loadTasks();
        };


        const deleteButton = document.createElement("button");

        deleteButton.textContent = "Delete";
        deleteButton.className = "delete-button";

        deleteButton.onclick = async function () {

            await fetch(
                `http://127.0.0.1:8000/tasks/${task.id}`,
                {
                    method: "DELETE"
                }
            );

            loadTasks();
        };


        taskItem.appendChild(taskText);
        taskItem.appendChild(completeButton);
        taskItem.appendChild(deleteButton);

        taskList.appendChild(taskItem);
    });
}


async function addTask() {

    const input = document.getElementById("taskInput");

    const title = input.value.trim();

    if (title === "") {
        return;
    }

    await fetch("http://127.0.0.1:8000/tasks", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title: title
        })
    });

    input.value = "";

    loadTasks();
}


loadTasks();