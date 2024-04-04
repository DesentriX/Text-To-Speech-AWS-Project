// Add event listener for submit button
document.getElementById('submitBtn').addEventListener('click', function() {
  // gets user input
  var textInput = document.getElementById('textInput').value;
  var voiceSelect = document.getElementById('voices').value;
  
  // Assign values to data object
  var data = {
    text: textInput,
    voice: voiceSelect
  };

  // Send data to backend using Fetch API
  fetch('Your API Endpoint', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    if (response.ok) {
      // Handle successful response
      console.log('Data sent successfully');
      return response.json();
    } else {
      // Handle error response
      console.error('Failed to send data');
      throw new Error('Failed to send data');
    }
  })
  .then(data => {
    // Log the response for debugging
    console.log('Response from Lambda:', data);
    
    // Check if data contains audioUrl
    //tempoarliy unused features; audio player and download audio button from front end.
    if (data && data.audioUrl) {
      // Display audio playback and download options
      document.getElementById('audioPlayer').innerHTML = '<audio controls id="audioPlayer"></audio>';
      document.getElementById('downloadBtn').innerHTML = '<a id="downloadBtn" download="output.mp3" href="">Download Audio File</a>';
      // Set audio source URL
      document.getElementById('audioPlayer').src = data.audioUrl;
      // Set download link URL
      document.getElementById('downloadBtn').href = data.audioUrl;
    } else {
      console.error('Audio URL not found in response');
    }
  })
  .catch(error => {
    // Handle network error
    console.error('Network error:', error);
  });
});

// Event listeners for audio player and download button
document.getElementById('audioPlayer').addEventListener('click', function() {
  // Play the audio
  document.getElementById('audioPlayer').play();
});

document.getElementById('downloadBtn').addEventListener('click', function() {
});
