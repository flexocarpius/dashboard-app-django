function showSnackbar(text) {
    $('#snackbar').html(text);
    $('#snackbar').addClass('show');
    setTimeout(() => {
        $('#snackbar').removeClass('show');
    }, 5000);
}