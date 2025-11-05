document.addEventListener('DOMContentLoaded', () => {
    const countdownElement = document.getElementById('countdown');
    const startTime = 5;
    let timeLeft = startTime;

    function updateCountdown() {
        if (timeLeft > 0) {
            countdownElement.textContent = timeLeft;
            timeLeft--;
            setTimeout(updateCountdown, 1000);
        } else {
            window.location.href = '/medico/';
        }
    }

    updateCountdown();
});