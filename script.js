//
// mobile Nav
let menuHamburger = document.querySelector(".menu_hamburger");
menuHamburger.addEventListener("click", (e) => {
  menuHamburger.classList.toggle("open");

  let mobileNav = document.querySelector(".mobile_nav");
  mobileNav.classList.toggle("showMobileNav");
});

// let a = 0
// let b = 0
// while (a < 3) {
//   a++;
//   b += a;
//   console.log(b);
// }
