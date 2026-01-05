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

// Auto-refresh submissions when judging is in progress
function refreshSubmissions() {
    const container = document.getElementById('submissions-container');
    if (!container) return; // Only run on problem detail page

    // Check if there are any running submissions
    const runningSubmissions = document.querySelectorAll('.submission-running');
    if (runningSubmissions.length === 0) {
        // No running submissions, stop polling
        return;
    }

    // Fetch updated submissions
    fetch(window.location.pathname)
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const newDoc = parser.parseFromString(html, 'text/html');
            const newSubmissionsList = newDoc.getElementById('submissions-list');

            if (newSubmissionsList) {
                // Update the submissions list
                const currentList = document.getElementById('submissions-list');
                currentList.innerHTML = newSubmissionsList.innerHTML;

                // Schedule next refresh if still running submissions
                if (document.querySelectorAll('.submission-running').length > 0) {
                    setTimeout(refreshSubmissions, 1000); // Poll every 1 second
                }
            }
        })
        .catch(error => console.error('Error refreshing submissions:', error));
}

// Start polling when page loads if submissions container exists
if (document.getElementById('submissions-container')) {
    setTimeout(refreshSubmissions, 1000);
}