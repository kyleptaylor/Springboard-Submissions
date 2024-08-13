class BoggleGame {
  constructor() {
    this.word = [];
    this.allWords = [];
    this.gameOver = false;
    this.timerInterval = null;
    this.initEventListeners();
    this.startTimer(60);
  }

  // Initialize event listeners
  initEventListeners() {
    $(document).on("click", ".boggle-letter", (event) =>
      this.handleLetterClick(event)
    );
    $("#submit-word").on("click", () => this.submitWord());
  }

  // Show alert messages
  showAlert(message, length = 5000) {
    let alertContainer = document.getElementById("custom-alert");
    if (!alertContainer) {
      alertContainer = document.createElement("div");
      alertContainer.id = "custom-alert";
      document.body.appendChild(alertContainer);
    }

    alertContainer.innerText = message;
    alertContainer.style.display = "block";

    setTimeout(() => {
      alertContainer.style.display = "none";
    }, length);
  }

  // Handle word submission
  async submitWord() {
    const wordStr = this.word.join("").toLowerCase();
    const currentScore = parseInt($("#current-score").text(), 10);

    if (this.gameOver) {
      try {
        const response = await $.ajax({
          url: "/boggle?restart=true",
          contentType: "application/json",
        });
        this.handleRestart(response);
      } catch (error) {
        console.error("Error:", error);
        this.showAlert("There was an error restarting the game.");
      }
    } else if (this.allWords.indexOf(wordStr) > -1) {
      this.showAlert("You already used that word!");
    } else {
      try {
        const response = await $.ajax({
          url: "/answer",
          method: "POST",
          contentType: "application/json",
          data: JSON.stringify({
            word: wordStr.toUpperCase(),
            words: this.allWords,
            score: currentScore,
          }),
        });
        this.handleResponse(response, currentScore);
      } catch (error) {
        console.error("Error:", error);
        this.showAlert("There was an error submitting the word.");
      }
    }

    // Reset the word array and remove the active class from all letters
    this.word = [];
    $(".boggle-letter").removeClass("active-boggle-letter");
  }

  // Handle server response
  handleResponse(response, currentScore) {
    switch (response.result) {
      case "ok":
        const newScore = currentScore + response.points;
        const word = response.word;

        if (!this.allWords.includes(word)) {
          this.allWords.push(word);
        }

        $("#current-score").text(newScore);
        $("#words").prepend(`<p>${word}</p>`);
        break;

      case "not-on-board":
        this.showAlert(
          "Sorry, the word must be made up of adjacent letters only."
        );
        break;

      default:
        this.showAlert("That word is not in our dictionary!");
        break;
    }
  }

  // Handle board restart
  handleRestart(response) {
    const board = response.board || [];
    const $boggleBox = $(".boggle-box");
    $boggleBox.empty();

    board.forEach((row) => {
      const $rowDiv = $('<div class="boggle-row"></div>');
      row.forEach((letter) => {
        $rowDiv.append(`<span class="boggle-letter">${letter}</span>`);
      });
      $boggleBox.append($rowDiv);
    });

    this.resetGame(); // Reset the game state
  }

  // Handle letter click
  handleLetterClick(event) {
    if (this.gameOver) return;

    const $this = $(event.target);
    const letter = $this.text();

    if ($this.hasClass("active-boggle-letter")) {
      return;
    }

    if (this.word.length >= 10) {
      return;
    }

    this.word.push(letter);
    $this.addClass("active-boggle-letter");
  }

  // Countdown timer
  startTimer(duration) {
    let timer = duration;
    const display = document.querySelector("#current-time");

    this.timerInterval = setInterval(() => {
      const seconds = timer % 60;

      display.textContent = seconds;

      if (--timer < 0) {
        clearInterval(this.timerInterval);
        display.textContent = "0";
        this.gameOver = true;
        $(".boggle-letter").addClass("game-over");
        $("#submit-word").text("Restart Game?");
        this.showAlert("GAME OVER!", 10000);
      }
    }, 1000);
  }

  // Reset game state
  resetGame() {
    this.gameOver = false;
    this.word = [];
    this.allWords = [];
    $(".boggle-letter").removeClass("active-boggle-letter game-over");
    $("#current-score").text("0");
    $("#words").empty();
    $("#submit-word").text("Submit Word");
    this.startTimer(60);
  }
}

// Initialize the game when the window loads
window.onload = () => {
  new BoggleGame();
};
