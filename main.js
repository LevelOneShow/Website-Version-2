// Volta Network Website - Homepage : main.js
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View the README at lic.volta.network for information on usage rights.

// --- Varibles --- \\

// Streamer Icons:
var userImages = null; // This gets replaced on page load.

// --- File Loading --- \\

// onLoad -> JSON
// On page load, it reads JSON data from specific file as passes it to
// toUserJSON.
$.ajax({
  type: "GET",
  url: "http://localhost/Server/output.json",
  dataType: "json",
  success: function(data) {
    toUserJSON(data);
  },
  error: function() {
    // issue : sendErrors();
    console.warn("Couldn\'t find file.")
  }
});

// onLoad -> JSON
// On page load, read JSON data for image locations from specified file
// and writes it to variable 'userImages'.
$.ajax({
  type: "GET",
  url: "http://localhost/imagesBase.json",
  dataType: "json",
  sucess: function(data) {
    // Sets the variable userImages to the data from the file.
    userImages = data;
  },
  error: function() {
    // issue : sendErrors();
    console.warn("Couldn\'t find file.")
  }
})

// --- Functions --- \\

// JSON -> JSON
// Takes JSON object with multiple streamers and outputs stream specific JSON
// objects and passes it to createLinkedImage.
function toUserJSON(json) {
  $.each(json, function(index, value) {
    createLinkedImage(value);
  })
}

// --- jQuery Functions --- \\

// JSON -> DOM
// Takes JSON and creates an image on a page with a tooltip that links to the
// corresposding stream.
function createLinkedImage(json) {
  // JSON data from twitch:
  url = json.url
  name = json.user
  streamTitle = json.title
  // JSON image lookup:
  image = userImages[name]
  // jQuery page appending:
  $("#streamers").append("<span class='streamer_image' title=" + streamTitle + 
  "><h2>" + name + "</h1><a href=" + url + "><img src=" + image + "></a></span>");
}
