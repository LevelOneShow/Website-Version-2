/* global Firebase */
// Level One Show Blog Posting Page : Editor viewing functionss
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View README.md at lic.volta.network for information on usage rights.

// --- Variables --- \\

// Reference to location of Firebase.
var losFirebaseBlog = new Firebase("https://losblog.firebaseio.com/");

// Reference to location of blog posts on Firebase.
var blogPosts = losFirebaseBlog.child("blogPosts");

// --- Functions --- \\

// num -> str
// Takes the number of milliseonds since 01/01/1970 and converts it to a readable
// date format by generating date strings based on locale.
function convertDate(num) {
  return (new Date(num).toLocaleDateString());
}

// --- Firebase Post Retrieval Functions --- \\

// GET -> DOM [state]
// Gets blog posts from Firebase.
blogPosts.on("child_added", function(snapshot) {
  partialPost(snapshot.val(), snapshot.key());
});

// JSON, STR -> DOM [state]
// Gets posts from Firbase and posts it to the page, but only included 20 characters from the body.
function partialPost(jsonblogcontent, FID) {
  var title = (jsonblogcontent["title"]).substring(0,21);
  var partialbody = jsonblogcontent["body"]
  var date = convertDate(jsonblogcontent["date"]);
  $("#partialPosts").append($("<div><h3>" + title + "</h3><p>" + partialbody + "...</p><p>" + date + "</p></div>").attr("blogID", FID));
}
