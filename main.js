// Volta Network Website - Homepage : main.js
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View the README at lic.volta.network for information on usage rights.

// --- Varibles --- \\

// Streamer Icons:
var userImages = null; // This gets replaced on page load.

// Local Storage Information:
localStorage.setItem("crashTimes" , 0); // Tracks number of background crashes.

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
  }
  error: function() {
    checkErrors();
  }
});

// onLoad -> JSON
// On page load, read JSON data for image locations from specified file
// and writes it to variable 'userImages'.
$.ajax({
  type: "GET",
  url: "http://localhost/imageBase.json",
  dataType: "json",
  sucess: function(data) {
    // Sets the variable userImages to the data from the file.
    userImages = data;
  }
  error: function() {
    checkErrors();
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

// -> href, null
// Determines if the user wants to reload the page if there is an error. If the
// error persists, then it asks the user if they want to report the error via email.
function checkErrors() {
  console.error("Something went wrong!"); //Reports to the console that something went wrong.
  if ((localStorage.getItem("crashTimes")) < 3) {
    if (confirm("Something went wrong. Would you like to reload the page?")) {
      location.reload();
    } else {
      return null;
    }
  } else {
    if (confirm("Some is really wrong! Would you like to email the creator of " + 
      "the site with some more information?\nPaste this: Database failed to " + 
      "load three times.")) {
      location.href = "mailto:admin@lvloneshow.com";
    } else {
      return null;
    }
  }
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
