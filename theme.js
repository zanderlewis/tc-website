document.addEventListener('DOMContentLoaded', function () {
    var body = document.body;
    var links = document.querySelectorAll('a');
    var header = document.querySelector('header');
    var nav = document.querySelector('nav');
    var footer = document.querySelector('footer');
    var themeToggle = document.getElementById('theme-toggle');
    var details = document.querySelectorAll('details');
    var summary = document.querySelectorAll('summary');

    // Function to check if a cookie exists
    function checkCookie(name) {
        return document.cookie.split(';').some((item) => item.trim().startsWith(name + '='));
    }

    // Load theme from cookie
    var theme = document.cookie.replace(/(?:(?:^|.*;\s*)theme\s*\=\s*([^;]*).*$)|^.*$/, "$1");

    // If the cookie does not exist, create it
    if (!checkCookie('theme')) {
        var date = new Date();
        date.setFullYear(date.getFullYear() + 1); // 1 year from now
        document.cookie = 'theme=;expires=' + date.toUTCString() + ';path=/';
    }

    if (theme === 'mode') {
        body.classList.add('mode');
        links.forEach(function(link) {
            link.classList.add('mode');
        });
        header.classList.add('mode');
        nav.classList.add('mode');
        footer.classList.add('mode');
        themeToggle.classList.add('mode');
        details.forEach(function(detail) {
            detail.classList.add('mode');
        });
        summary.forEach(function(sum) {
            sum.classList.add('mode');
        });
        themeToggle.textContent = '🌙';
    } else {
        themeToggle.textContent = '☀️';
    }

    themeToggle.addEventListener('click', function () {
        body.classList.toggle('mode');
        links.forEach(function(link) {
            link.classList.toggle('mode');
        });
        header.classList.toggle('mode');
        nav.classList.toggle('mode');
        footer.classList.toggle('mode');
        themeToggle.classList.toggle('mode');
        details.forEach(function(detail) {
            detail.classList.toggle('mode');
        });
        summary.forEach(function(sum) {
            sum.classList.toggle('mode');
        });

        // Save theme to cookie
        var date = new Date();
        date.setFullYear(date.getFullYear() + 1); // 1 year from now
        document.cookie = 'theme=' + (body.classList.contains('mode') ? 'mode' : '') + ';expires=' + date.toUTCString() + ';path=/';

        this.textContent = body.classList.contains('mode') ? '🌙' : '☀️';
    });
});