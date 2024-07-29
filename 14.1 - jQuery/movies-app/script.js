$(document).ready(function () {
  $("#new-movie").on("click", function () {
    let $title = $("#title").val();
    let $rating = $("#rating").val();
    let $newMovie =
      '<div class="movie"><h2>' +
      $title +
      "</h2>" +
      "<h3>" +
      $rating +
      '</h3><button class="remove">Remove</button></div>';
    $("#entered-movies").append($newMovie);
  });

  $(document).on("click", ".remove", function () {
    $(this).parent(".movie").remove();
  });
});
