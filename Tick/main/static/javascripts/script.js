//
// mobile Nav
let menuHamburger = document.querySelector(".menu_hamburger");
menuHamburger.addEventListener("click", (e) => {
  menuHamburger.classList.toggle("open");

  let mobileNav = document.querySelector(".mobile_nav");
  mobileNav.classList.toggle("showMobileNav");
});


const setTheme = (theme) => {
  document.documentElement.className = theme;
  localStorage.setItem("theme", theme);
};

const getTheme = () => {
	const theme = localStorage.getItem("theme");
	theme && setTheme(theme);
};

getTheme();