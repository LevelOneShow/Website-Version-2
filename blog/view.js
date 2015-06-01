// Level One Show Blog View Page
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View README.md at ... for information on usage rights.

// --- Functions --- \\

// num -> str
// Takes the number of milliseonds since 01/01/1970 and converts it to a readable
// date format by generating date strings based on locale.
function convertDate(num) {
  return (new Date(num).toLocaleDateString());
}

// --- jQuery Functions --- \\

// GET -> DOM
// Gets the number of blog posts.
blogPosts.once("value", function(snapshot) {
  if (snapshot.numChildren() == 1) {
    $("#numPosts").append("<p><strong>There is 1 Post.</strong></p>");
  } else {
    $("#numPosts").append("<p><strong>There are " + snapshot.numChildren() + " Posts.</strong></p>");
  }
});

// JSON, STR -> DOM
// Converts the JSON data stored in Firebase to DOM that goes on the site.
function JSONToBlog(jsonblogcontent, FID) {
  title = jsonblogcontent["title"]
  body = jsonblogcontent["body"]
  date = convertDate(jsonblogcontent["date"]);
  $("#blogPosts").append($("<div><h1>" + title + "</h1><p>" + body + "</p><p>" + date + "</p><hr></div>").attr("blogID", FID));
}
