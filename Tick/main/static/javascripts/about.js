let menuHamburger = document.querySelector(".menu_hamburger");
menuHamburger.addEventListener("click", (e) => {
  menuHamburger.classList.toggle("open");

  let mobileNav = document.querySelector(".mobile_nav");
  mobileNav.classList.toggle("showMobileNav");
});

const Darkmode = document.getElementById("darkmode");
const Darkmode2 = document.querySelector(".dark-mode");
Darkmode.onclick = function () {
  document.body.classList.toggle("dark-mode");
  if (document.body.classList.contains("dark-mode")) {
    Darkmode.style.color = "white";
  } else {
    Darkmode.style.color = "black";
  }
};
Darkmode2.onclick = function () {
  document.body.classList.toggle("dark-mode");
  if (document.body.classList.contains("dark-mode")) {
    Darkmode.style.color = "white";
  } else {
    Darkmode.style.color = "black";
  }
};
