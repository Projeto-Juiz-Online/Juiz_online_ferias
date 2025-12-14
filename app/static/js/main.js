document.addEventListener("DOMContentLoaded", function() {
    var alerts = document.querySelectorAll(".alert");

    alerts.forEach(function(alert) {
        setTimeout(function() {

            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 3000); // 3000 ms = 3 segundos
    });
});

// Função para alternar o tema
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute("data-theme");
    const icon = document.getElementById("theme-icon");

    if (currentTheme === "light") {
        html.setAttribute("data-theme", "dark");
        localStorage.setItem("theme", "dark");
        icon.innerHTML = "🌙"; 
    } else {
        html.setAttribute("data-theme", "light");
        localStorage.setItem("theme", "light");
        icon.innerHTML = "☀️"; 
    }
}

(function() {
    const savedTheme = localStorage.getItem("theme") || "dark";
    document.documentElement.setAttribute("data-theme", savedTheme);
})();