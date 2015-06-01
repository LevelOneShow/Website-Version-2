// Level One Show Blog Posting Page : Main Functions
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View README.md at ... for information on usage rights.

// --- Variables --- \\

// Reference to location of Firebase.
var losFirebaseBlog = new Firebase("https://losblog.firebaseio.com/");

// Reference to location of blog posts on Firebase.
var blogPosts = losFirebaseBlog.child("blogPosts");

// --- Firebase Post Retrieval Functions --- \\

// GET -> DOM [state]
// Gets blog posts from Firebase.
blogPosts.on("child_added", function(snapshot) {
  JSONToBlog(snapshot.val(), snapshot.key());
});

// GET -> DOM [state]
// If a blog post is removed from Firebase, remove the corresponding blog post
// with given ID from the page.
blogPosts.on("child_removed", function(snapshot) {
  $("div").filter(function() {
    return $(this).attr("blogID") === snapshot.key()
  }).remove();
});

// GET -> DOM [state]
// If a blogPost's contents are updated, change it's contents.
blogPosts.on("child_changed", function(snapshot) {
  $("div").filter(function() {
    return $(this).attr("blogID") === snapshot.key()
  }).replaceWith(JSONToBlog(snapshot.val(), snapshot.key()));
});
