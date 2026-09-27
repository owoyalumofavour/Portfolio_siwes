document.addEventListener('DOMContentLoaded', function () {

    // get all the elements
    var themeToggle = document.getElementById('theme-toggle');
    var loadProjectsBtn = document.getElementById('load-projects');
    var projectList = document.getElementById('project-list');

    // dark mode toggle
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            document.body.classList.toggle('dark');
            
            if (document.body.classList.contains('dark')) {
                themeToggle.textContent = 'Toggle Light Mode';
            } else {
                themeToggle.textContent = 'Toggle Dark Mode';
            }
        });
    }

    // project list toggle
    if (loadProjectsBtn && projectList) {
        loadProjectsBtn.addEventListener('click', function () {
            projectList.classList.toggle('visible');
            
            if (projectList.classList.contains('visible')) {
                loadProjectsBtn.textContent = 'Hide Projects';
            } else {
                loadProjectsBtn.textContent = 'Load Projects';
            }
        });
    }

});