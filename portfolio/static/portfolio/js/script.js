function loadStyle() {
    const darkModeStat = localStorage.getItem("darkModeStat");
    console.log("Darkmode: " + darkModeStat);

    if (darkModeStat === null) {
        localStorage.setItem("darkModeStat", "0");
    } else {
        if (darkModeStat === "1") {
            setDarkMode();
        } else {
            setLightMode();
        }
    }
}

function setDarkMode() {
    document.getElementById("stylesheet").href = "/static/portfolio/css/style-dark.css";
    document.getElementById("darkModeBTN").textContent = "dark_mode";
    var vid = document.getElementById("myVideo");
    vid.src = "/static/portfolio/images/10mb%20preto.mp4";
}

function setLightMode() {
    document.getElementById("stylesheet").href = "/static/portfolio/css/style-light.css";
    document.getElementById("darkModeBTN").textContent = "light_mode";
    var vid = document.getElementById("myVideo");
    vid.src = "/static/portfolio/images/10mb%20branco.mp4";
}

document.addEventListener("DOMContentLoaded", function () {
    const darkModeButton = document.querySelector('#darkModeBTN');

    darkModeButton.addEventListener('click', function () {
        const darkModeStat = localStorage.getItem("darkModeStat");

        if (darkModeStat === "1") {
            localStorage.setItem("darkModeStat", "0");
            setLightMode();
        } else {
            localStorage.setItem("darkModeStat", "1");
            setDarkMode();
        }
    });
});