// JavaScript code to create and move multiple minion characters

const battlefield = document.querySelector(".battlefield");

// Function to create a minion character
function createMinion() {
  const minion = document.createElement("div");
  minion.classList.add("character");
  minion.style.left = `${Math.random() * (window.innerWidth - 50)}px`; // Random horizontal position
  battlefield.appendChild(minion);
}

// Create 20 minion charactersconst videoPlayer = document.getElementById('video-player');
const gestureIndicator = document.getElementById("gesture-indicator");

// Function to handle play/pause gesture
function togglePlayPause() {
  if (videoPlayer.paused) {
    videoPlayer.play();
    gestureIndicator.textContent = "Playing";
  } else {
    videoPlayer.pause();
    gestureIndicator.textContent = "Paused";
  }
}

// Function to handle forward gesture
function forward() {
  videoPlayer.currentTime += 10; // Forward by 10 seconds (adjust as needed)
  gestureIndicator.textContent = "Forwarded";
}

// Function to handle backward gesture
function backward() {
  videoPlayer.currentTime -= 10; // Backward by 10 seconds (adjust as needed)
  gestureIndicator.textContent = "Backwarded";
}

// Function to handle next video gesture (for demonstration)
function nextVideo() {
  videoPlayer.src = "next-video.mp4"; // Replace with the next video source
  videoPlayer.load();
  gestureIndicator.textContent = "Next Video";
}

// Gesture recognition (for demonstration, you'd use a hand tracking library or similar)
document.addEventListener("keydown", (event) => {
  if (event.key === "p") {
    // For demonstration, 'p' key simulates a play/pause gesture
    togglePlayPause();
  } else if (event.key === "f") {
    // For demonstration, 'f' key simulates a forward gesture
    forward();
  } else if (event.key === "b") {
    // For demonstration, 'b' key simulates a backward gesture
    backward();
  } else if (event.key === "n") {
    // For demonstration, 'n' key simulates a next video gesture
    nextVideo();
  }
});

// Hide the gesture indicator after a few seconds (adjust as needed)
setTimeout(() => {
  gestureIndicator.textContent = "";
}, 3000);

for (let i = 0; i < 20; i++) {
  createMinion();
}
