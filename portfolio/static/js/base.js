document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

new Typewriter('#typewriter', {
    strings: [' Hello!', ' היי!', ' שלום!', ' 你好!', ' Bună!', ' नमस्ते!', ' こんにちは!', ' 안녕!', ' Hi!',],
    autoStart: true,
    loop: true,
});
new Typewriter('#cursor', {
    strings: [''],
    autoStart: true,
    loop: true,
});
