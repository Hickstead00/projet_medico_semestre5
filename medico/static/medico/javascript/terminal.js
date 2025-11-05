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
                }
                terminal.style.display = "none";
                content.style.display = "block";
            }, 400);
        }
    }

    lines.forEach(line => line.style.display = "none");

    showLine();
});
