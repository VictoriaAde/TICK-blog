//
// mobile Nav
let menuHamburger = document.querySelector(".menu_hamburger");
menuHamburger.addEventListener("click", (e) => {
	menuHamburger.classList.toggle("open");

	let mobileNav = document.querySelector(".mobile_nav");
	mobileNav.classList.toggle("showMobileNav");
});

const setTheme = (theme) => {
	document.querySelector("body").className = theme;
	localStorage.setItem("theme", theme);
};

const getTheme = () => {
	const theme = localStorage.getItem("theme");
	theme && setTheme(theme);
};

getTheme();

// Form validation
const form = document.querySelector("form");
const userName = document.getElementById("display-name");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm-pwd");
const errorMsg = document.getElementsByClassName("error-msg");

const isEmailValid = (email) => {
	const re =
		/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(email);
};
const isPasswordSecure = (password) => {
	const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&.*])(?=.{8,})");
	return re.test(password);
};

form.addEventListener("submit", (e) => {
	const userNameValue = userName.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const confirmPasswordValue = confirmPassword.value.trim();

	// prevent the form from submitting
	if (userNameValue === "" || emailValue === "" || passwordValue === "" || confirmPasswordValue === "") {
		e.preventDefault();
	} else {
		console.log("works");
	}
	// validate the form
	checkInput();
});

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const errorMsg = formControl.querySelector(".error-msg");
	errorMsg.innerText = message;
	formControl.classList.add("error");
	formControl.classList.remove("success");
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	const errorMsg = formControl.querySelector(".error-msg");
	errorMsg.innerText = "";
	formControl.classList.add("success");
	formControl.classList.remove("error");
}

function checkInput() {
	const userNameValue = userName.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const confirmPasswordValue = confirmPassword.value.trim();

	if (userNameValue === "") {
		setErrorFor(userName, "Please enter your name");
	} else {
		setSuccessFor(userName);
	}

	if (emailValue === "") {
		setErrorFor(email, "Please enter your email");
	} else if (!isEmailValid(emailValue)) {
		setErrorFor(email, "Please enter a valid email");
	} else {
		setSuccessFor(email);
	}
	if (passwordValue.length < 8) {
		setErrorFor(password, "Password must be at least 8 characters");
	} else if (passwordValue === "") {
		setErrorFor(password, "Please enter your password");
	} else if (!isPasswordSecure(passwordValue)) {
		setErrorFor(
			password,
			"Password not secure enough. Include at least 1 lowercase character, 1 uppercase character, 1 number, and 1 special character"
		);
	} else {
		setSuccessFor(password);
	}

	if (confirmPasswordValue === "") {
		setErrorFor(confirmPassword, "Please enter your password");
	} else if (passwordValue !== confirmPasswordValue) {
		setErrorFor(confirmPassword, "Passwords do not match");
	} else {
		setSuccessFor(confirmPassword);
	}
}

const debounce = (fn, delay = 500) => {
	let timeoutId;
	return (...args) => {
		// cancel the previous timer
		if (timeoutId) {
			clearTimeout(timeoutId);
		}
		// setup a new timer
		timeoutId = setTimeout(() => {
			fn.apply(null, args);
		}, delay);
	};
};

form.addEventListener(
	"input",
	debounce(function (e) {
		switch (e.target.id) {
			case "display-name":
				checkInput();
				break;
			case "email":
				checkInput();
				break;
			case "password":
				checkInput();
				break;
			case "confirm-pwd":
				checkInput();
				break;
		}
	})
);

function showPwd() {
	let eye = document.getElementById("eye");
	let x = document.getElementById("password");
	if (x.type === "password") {
		x.type = "text";
		eye.src = "images/hide-pwd.svg";
	} else {
		x.type = "password";
		eye.src = "images/show-pwd.svg";
	}
}
