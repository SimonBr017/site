function animateAndRedirect() {
    const section = document.querySelector(".cta");
    if (!section) return;

    section.classList.add("animate-out");

    setTimeout(() => {
        window.location.href = "/contact";
    }, 500);
}