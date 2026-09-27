// enhanced to-do app javascript

document.addEventListener('DOMContentLoaded', () => {

    // get element references
    const taskInput = document.getElementById('task-input');
    const addBtn = document.getElementById('add-btn');
    const taskList = document.getElementById('task-list');
    const taskCount = document.getElementById('task-count');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const clearCompleted = document.getElementById('clear-completed');

    // load tasks from localStorage or start with empty array
    let tasks = JSON.parse(localStorage.getItem('my-tasks')) || [];
    let currentFilter = 'all';

    // save tasks to localStorage
    function saveTasks() {
        localStorage.setItem('my-tasks', JSON.stringify(tasks));
    }

    // update the task counter
    function updateCount() {
        const active = tasks.filter(t => !t.completed).length;
        taskCount.textContent = `${active} task${active !== 1 ? 's' : ''} left`;
    }

    // render tasks based on current filter
    function renderTasks() {
        taskList.innerHTML = '';

        // filter tasks based on selection
        let filtered = tasks;
        if (currentFilter === 'active') {
            filtered = tasks.filter(t => !t.completed);
        } else if (currentFilter === 'completed') {
            filtered = tasks.filter(t => t.completed);
        }

        // create list items for each task
        filtered.forEach(task => {
            const li = document.createElement('li');
            li.className = 'task-item' + (task.completed ? ' completed' : '');

            li.innerHTML = `
                <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}>
                <span class="task-text">${task.text}</span>
                <button class="delete-btn">×</button>
            `;

            // toggle completion
            li.querySelector('.task-checkbox').addEventListener('change', () => {
                task.completed = !task.completed;
                saveTasks();
                renderTasks();
                updateCount();
            });

            // delete task
            li.querySelector('.delete-btn').addEventListener('click', () => {
                tasks = tasks.filter(t => t.id !== task.id);
                saveTasks();
                renderTasks();
                updateCount();
            });

            taskList.appendChild(li);
        });

        updateCount();
    }

    // add a new task
    function addTask() {
        const text = taskInput.value.trim();
        if (!text) return;

        // create task object with unique id
        const task = {
            id: Date.now(),
            text: text,
            completed: false
        };

        tasks.push(task);
        saveTasks();
        renderTasks();

        // clear input
        taskInput.value = '';
        taskInput.focus();
    }

    // add task on button click
    addBtn.addEventListener('click', addTask);

    // add task on enter key
    taskInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') addTask();
    });

    // filter button handlers
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // add active class to clicked button
            btn.classList.add('active');
            // update current filter and re-render
            currentFilter = btn.dataset.filter;
            renderTasks();
        });
    });

    // clear completed tasks
    clearCompleted.addEventListener('click', () => {
        tasks = tasks.filter(t => !t.completed);
        saveTasks();
        renderTasks();
    });

    // initial render
    renderTasks();

});