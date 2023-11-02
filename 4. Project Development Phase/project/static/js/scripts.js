/*!
* Start Bootstrap - Creative v7.0.7 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

});


function showResult() {
    var resultDiv = document.getElementById("result");
    var resultText = document.getElementById("result-text");

    var predictionText = "{{y}}";

    resultText.textContent = predictionText;
    resultDiv.style.display = "block";
};


function submitForm(event) {
    // Prevent the default form submission behavior
    event.preventDefault(); 

    // Gather form data
    var formData = new FormData(event.target);

    // Send a POST request using AJAX
    fetch('/login', {
        method: 'POST',
        body: formData
    })
        
    // Assuming Flask returns JSON
    .then(response => response.json())  
    .then(data => {
        var resultDiv = document.getElementById("result-text");
        var resultDisplay = document.getElementById("result");

        if (data.y == "bankrupt") {
            resultDiv.textContent = "!! THE COMPANY CAN GO BANKRUPT !!";
        } else if (data.y == "safe") {
            resultDiv.textContent = "!! THE COMPANY IS SAFE !!";
        }

        resultDisplay.style.display = "block";
    })
    .catch(error => {
        console.error('Error:', error);
    });
};


function displayMessage(event) {
    event.preventDefault();

    var name = document.getElementById("name");
    var email = document.getElementById("email");
    var company = document.getElementById("company");
    var message = document.getElementById("message");

    const success = document.getElementById("success");
    const failure = document.getElementById("failure");

    if (name.value != '' && email.value != '' && company.value != '' && message.value != '') {
        success.style.display = 'block';

        setTimeout(() => {
            name.value = '';
            email.value = '';
            company.value = '';
            message.value = '';
        }, 4000);
    }
    else {
        failure.style.display = 'block';
    };

    setTimeout(() => {
        failure.style.display = 'none';
        success.style.display = 'none';
    }, 6000);
};