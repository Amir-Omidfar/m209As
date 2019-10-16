// Store frame for motion functions
var previousFrame = null;
var paused = false;
var pauseOnGesture = false;

// Setup Leap loop with frame callback function
var controllerOptions = {enableGestures: true};

// to use HMD mode:
controllerOptions.optimizeHMD = true;

Leap.loop(controllerOptions, function(frame) {
  if (paused) {
    return; // Skip this update
  }

  // Display Pointable (finger and tool) object data
  var pointableOutput = document.getElementById("pointableData");
  var fingerCountOutput = document.getElementById("fingerCount");
  var fingerCount="";

  var pointableString = "";
  var extendedFingers = 0;
  if (frame.pointables.length > 0) {
    var fingerTypeMap = ["Thumb", "Index finger", "Middle finger", "Ring finger", "Pinky finger"];
    var boneTypeMap = ["Metacarpal", "Proximal phalanx", "Intermediate phalanx", "Distal phalanx"];
    for (var i = 0; i < frame.pointables.length; i++) {
      var pointable = frame.pointables[i];
      pointableString += "<div style='width:250px; float:left; padding:5px'>";
      pointableString += "Pointable ID: " + pointable.id + "<br />";
      pointableString += "Type: " + fingerTypeMap[pointable.type] + "<br />";
      pointableString += "Extended?: "  + pointable.extended + "<br />";
      if (pointable.extended)
        extendedFingers++;
    pointableString += "</div>"; 
    }
  fingerCount="<div style='width:250px; float:left; padding:5px'>";
  fingerCount += "extendedFingers = " + extendedFingers+ "<br />"+"</div>";  
  }
  else {
    pointableString += "<div>No hand detected! </div>";
    fingerCount = "<div></div>";
  }
  pointableOutput.innerHTML = pointableString;
  fingerCountOutput.innerHTML = fingerCount;

  // Display the corresponding letters for the number of extended fingers 
  var lettersOutput = document.getElementById("letters");
  var letters = "";
  if (fingerCount != "<div></div>")
  {
    letters="<div style='width:250px; float:left; padding:5px'>"
    letters="Select from:"+"<br />";
    var shownLetters = [];
    switch(extendedFingers){
      case 0:
      shownLetters = ["a","b","c","d"];
      case 1:
      shownLetters = ["e","f","g","h"];
      case 2:
      shownLetters = ["i","j","k","l"];
      case 3:
      shownLetters = ["m","n","o","p","q"];
      case 4:
      shownLetters = ["r","s","t","u","v"];
      case 5: 
      shownLetters = ["w","x","v","z"]; 
    }
    letters+=shownLetters+"</div>"
  }
  else
  {
    letters="<div>No letter to display! </div>"
  }
  lettersOutput.innerHTML = letters;
  // Store frame for motion functions
  previousFrame = frame;
})


