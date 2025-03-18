// Пример простого JS кода

document.addEventListener('DOMContentLoaded', () => {
    const demoBtn = document.getElementById('demoBtn');
    if (demoBtn) {
        demoBtn.addEventListener('click', () => {
            alert('Демо-функция: Chatlab стартует!');
        });
    }
});
