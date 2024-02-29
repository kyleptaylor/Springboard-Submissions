$(document).ready(function() {
    $('#new-movie').on("click", function() {
        let title = $('#title').val();
        let rating = $('#rating').val();  
        $('#entered-movies').append('<div>' + title + rating + '</div>')
    });
});