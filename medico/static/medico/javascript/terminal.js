document.addEventListener("DOMContentLoaded", () => {
    const lines = document.querySelectorAll("#terminal-sequence .console-line");
    const terminal = document.getElementById("terminal-sequence");
    const content = document.getElementById("blackmarket-content");

    let index = 0;

    function showLine() {
        if (index < lines.length) {
            lines[index].style.display = "block";
            index++;
            setTimeout(showLine, 700); // vitesse (ms)
        } else {
            // Fin → on masque le terminal et affiche le site
            setTimeout(() => {
                terminal.style.display = "none";
                content.style.display = "block";
            }, 400);
        }
    }

    // Masquer toutes les lignes d'abord
    lines.forEach(line => line.style.display = "none");

    // Lancer l'animation
    showLine();
});
