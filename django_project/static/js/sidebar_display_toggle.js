const sidebar = document.querySelector(".div-header-sidebar");
const toggleButton = document.querySelector(".button-user-profile")

toggleButton.addEventListener("click", (event) => {
    sidebar.classList.add("active");
    event.stopPropagation();
})

document.addEventListener("click", (event) => {
    if (!sidebar.contains(event.target) && event.target !== toggleButton) {
        sidebar.classList.remove("active");
    }
})