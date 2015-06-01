// Level One Show Blog Posting Page : Upload functions & Auth Check
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View README.md at lic.volta.network for information on usage rights.

// --- Variables --- \\

// Test Login:

// --- Functions --- \\

// sys -> num
// Gets the number of milliseconds since 01/01/1970.
function getDate() {
  var timeObject = new Date();
  return timeObject.getTime();
}

// DOM [data] -> bool || bool && alert
// Checks to make sure the user has written something in the title and body.
function completePost() {
  var titleVal = $("#title").val();
  var bodyVal = $("#body").val();
  // Make sure that all the values meet the requirements...
  if (titleVal.length > 0 || bodyVal.length > 0) {
    return true
  } if (titleVal.length == 0) {
    return false
    alert("Whoops! It doesn't look like you have a title.");
  } if (bodyVal.length == 0) {
    alert("Whoops! It doesn't look like you have anything written in the post.");
    return false
  } else {
    return false
    alert("Looks like something went wrong! Contact admin@lvloneshow.com for assistance.")
  }
}

// --- jQuery Functions --- \\

// jQuery Main
$(document).ready(function() {
  $('#submit').click(function() {
    if (completePost()) {
      submitWithAuth();
    } else {
      throw new Error("Something went wrong...");
    }
  });
});

// --- Firebase Blog Posting --- \\

// DOM [data] -> POST
// Pushes the data from the blog entry form to Firebase site.
function submitWithAuth() {
  // Security Check.
  var authData = losFirebaseBlog.getAuth();
  if (authData) {
    blogPosts.push({
      title: $('#title').val(),
      body: $('#body').val(),
      date: getDate()
    });
    $('#title').val('');
    $('#body').val('');
  } else {
    alert("You are not authenticated!");
  }
}
