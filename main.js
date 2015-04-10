// Level One Show Blog Posting Page : Main Functions
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View README.md at ... for information on usage rights.

// --- Global Varibles --- \\

// Streamer Icons:
var userImages = {}; // Fill in later.

// --- Functions --- \\

// JSON -> JSON
// Takes JSON object with multiple streamers and outputs stream specific JSON
// objects and passes it to SOMETHING HERE.
function toUserJSON(json) {
  $.each(json, function(index, value) {
    createLinkedImage(value);
  })
}

// --- jQuery Functions --- \\

// onLoad -> JSON
// When the page loads, it reads twitch api data from a specific file.
$.ajax({
  type: "GET",
  url: "http://localhost/Server/output.json",
  dataType: "json",
  success: function(data) {
    toUserJSON(data);
  }
});

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
  $("#streamers").append("<span class='streamer_image' title=" + streamTitle + "><h2>" + name + "</h1><a href=" + url + "><img src=" + image + "></a></span>");
}
