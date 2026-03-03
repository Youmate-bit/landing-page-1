window.moveSlider = function(value, id) {
    const beforeImg = document.getElementById('before-img-' + id);
    const sliderLine = document.getElementById('slider-line-' + id);
    if (beforeImg && sliderLine) {
        beforeImg.style.width = value + '%';
        sliderLine.style.left = value + '%';
    }
};

document.addEventListener('mousemove', (e) => {
    const heroImg = document.querySelector('header img');
    if (heroImg) {
        const x = (window.innerWidth / 2 - e.pageX) / 60;
        const y = (window.innerHeight / 2 - e.pageY) / 60;
        heroImg.style.transform = `translate(${x}px, ${y}px) scale(1.05)`;
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const email = document.querySelector('input[name="email"]');
    if (email) {
        email.addEventListener('input', function() {
            const isValid = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/.test(this.value);
            this.style.border = isValid ? "2px solid #22c55e" : "2px solid #ec4899";
        });
    }
});
