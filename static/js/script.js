/* Sign up form functionality*/

$('#password, #password-repeat').on('keyup', function () {
    if ($('#password').val() == $('#password-repeat').val()) {
        $('#message').html('Matching').css('color', 'green');
    } else
        $('#message').html('Not Matching').css('color', 'red');
});

/**************************** Function to close dropdown menu after selecting section ***********************************/

window.onclick = function () {
    let dropDown = document.getElementById("navbarNavDropdown");
    if (dropDown.classList.contains("show")) {
        dropDown.classList.remove("show");
    }
};

/**************************** Allows Text-Area box for review to resize if a big review ***********************************/

$('textarea').autoResize();