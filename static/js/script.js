/* Sign up form functionality*/

$('#password, #password-repeat').on('keyup', function () {
    if ($('#password').val() == $('#password-repeat').val()) {
        $('#message').html('Matching').css('color', 'green');
    } else
        $('#message').html('Not Matching').css('color', 'red');
});