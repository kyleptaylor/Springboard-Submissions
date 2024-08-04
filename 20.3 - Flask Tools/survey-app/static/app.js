document.addEventListener("DOMContentLoaded", () => {
  const closeButton = document.getElementById("close-flashes");
  const flashBox = document.getElementById("flashes");

  closeButton.addEventListener("click", () => {
    flashBox.style.display = "none";
  });
});
