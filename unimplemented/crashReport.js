// Volta Network Website - Homepage : crashReport.js
// Code by Nick Pleatsikas (nickcp.com)

// Contact admin@lvloneshow.com to report any bugs.
// View the README at lic.volta.network for information on usage rights.

// --- Functions --- \\

// -> [function call]
// Detects the number of errors as set as a sessionStorage key and send either
// 'true' or 'false' to the function userStepIn depending on the num of errors.
function sendErrors() {
  console.error("Something went wrong!"); // Reports to the console that something went wrong.
  sessionStorage.crashTimes = (parseInt(sessionStorage.crashTimes) + 1); // Gets crashTimes var from localstorage.
  
  if (isNaN(sessionStorage.crashTimes)) {
    sessionStorage.setItem("crashTimes", 0);
    userStepIn(false);
  } else if (sessionStorage.crashTimes === null) {
    return null;
  } else if (parseInt(sessionStorage.crashTimes) < 1) {
    userStepIn(false);
  } else {
    userStepIn(true);
  }
}

// bool -> href 
// Gives users the choice to either reload the page (up to 3 times), email the
// developer, or do nothing in the event of an error.
function userStepIn(multiCrash) {
  // Confirm dialog box statements:
  var statement1 = "Whoops! Looks like something went wrong.\nPress \'OK\' to reload the page";
  var statement2 = "Looks like the issue isn't fixing itself.\nPress \'OK\' to email the developer" + 
  " to let them know that there is something wrong.";
  
  if (multiCrash && confirm(statement2)) {
    location.href = "mailto:admin@lvloneshow.com";
  } else if (multiCrash && !(confirm(statement2))) {
    sessionStorage.setItem("crashTimes", null); // Sets the sesion key to 'null' to prevent further dialogs.
  } else if (!(multiCrash) && confirm(statement1)) {
    location.reload();
  } else {
    console.warn("User chose to do nothing.");
  }
}