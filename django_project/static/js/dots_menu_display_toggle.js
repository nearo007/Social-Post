const toggleButtons = document.querySelectorAll(".button-dots-menu");

toggleButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        const otherMenus = document.querySelectorAll(".div-dots-menu");
        otherMenus.forEach((menu) => {
            menu.classList.remove("active");
        });

        event.stopPropagation(); // Evita que o clique no botão dispare o evento do document
        
        const parentDiv = button.closest(".post-div"); // Encontra a div pai
        const dotsMenu = parentDiv.querySelector(".div-dots-menu"); // Acha o menu correspondente
        
        // Alterna a classe apenas no menu correspondente
        dotsMenu.classList.toggle("active");
    });
});

document.addEventListener("click", (event) => {
    document.querySelectorAll(".div-dots-menu.active").forEach((menu) => {
        if (!menu.contains(event.target) && !event.target.classList.contains("button-dots-menu")) {
            menu.classList.remove("active");
        }
    });
});
