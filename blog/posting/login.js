/// <reference path="../typings/jquery/jquery.d.ts"/>
// Level One Show Blog Posting Page : Login Functions
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View README.md at lic.volta.network for information on usage rights.

// --- Functions --- \\

// str, array -> console
// Logs authentication error/data.
function authHandler(error, data) {
  if (error) {
    console.log("Login Failed", error);
  } else {
    console.log("Authenticated succesfully with payload:", data);
  }
}

// --- jQuery Functions --- \\

$(document).ready(function() {
  // Login Click-Handler
  $('#login').click(function() {
    losFirebaseBlog.authWithPassword({
      email: $("#username").val(),
      password: $("#password").val()
    }, authHandler)
    $('#username').val("");
    $('#password').val("");
  });
  // Logout Click-Handler
  $('#logout').click(function() {
    losFirebaseBlog.unauth();
    console.log("The user has sucessfully been logged out.");
  });
});

// GET -> DOM
// Tells the user if they are logged in.
losFirebaseBlog.onAuth(function(authInfo) {
  if (authInfo) {
    $('#logged').text("Status: You are logged in!");
  } else {
    $('#logged').text("Status: You are not logged in.");
  }
});
