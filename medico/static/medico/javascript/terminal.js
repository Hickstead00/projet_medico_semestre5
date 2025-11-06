document.addEventListener("DOMContentLoaded", () => {
    const lines = document.querySelectorAll("#terminal-sequence .console-line");
    const terminal = document.getElementById("terminal-sequence");
    const content = document.getElementById("blackmarket-content");
    const animationPlayed = sessionStorage.getItem('blackmarket_animation_played');
    
    if (animationPlayed) {
        terminal.style.display = "none";
        content.style.display = "block";
        return;
    }

    let index = 0;

    function showLine() {
        if (index < lines.length) {
            lines[index].style.display = "block";
            index++;
            setTimeout(showLine, 700);
        } else {
setTimeout(() => {
    try {
        sessionStorage.setItem('blackmarket_animation_played', '1');
    } catch (e) {
        console.error("Erreur sessionStorage:", e);
    }
    terminal.style.display = "none";
    
    // Au lieu de content.style.display = "block";
    content.removeAttribute('style');
    // OU forcez avec !important via une classe
    content.classList.add('show-content');
    
    console.log("Content display:", window.getComputedStyle(content).display);
}, 400);
        }
    }

    lines.forEach(line => line.style.display = "none");

    showLine();
});
