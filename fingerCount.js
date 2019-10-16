// Store frame for motion functions
var previousFrame = null;
var paused = false;
var pauseOnGesture = false;

// Setup Leap loop with frame callback function
var controllerOptions = {enableGestures: true};

// to use HMD mode:
controllerOptions.optimizeHMD = true;

// letters 
var letters = "";
var shownLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","v","z"];

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
  if (fingerCount != "<div></div>")
  {
    letters="<div style='width:250px; float:left; padding:5px'>"
    letters="Select from:"+"<br />";
    
    
    if (extendedFingers === 0){
      letters+= shownLetters[0]+ " "+shownLetters[1]+ " "+shownLetters[2]+ " "+shownLetters[3]+"</div>";
    }
    else if (extendedFingers === 1)
    {
      letters+= shownLetters[4]+ " "+shownLetters[5]+ " "+shownLetters[6]+ " "+shownLetters[7]+"</div>";
    }
    else if (extendedFingers === 2)
    {
      letters+= shownLetters[8]+ " "+shownLetters[9]+ " "+shownLetters[10]+ " "+shownLetters[11]+"</div>";
    }
    else if (extendedFingers === 3)
    {
      letters+= shownLetters[12]+ " "+shownLetters[13]+ " "+shownLetters[14]+ " "+shownLetters[15]+ " "+shownLetters[16]+"</div>";
    }
    else if (extendedFingers === 4)
    {
      letters+= shownLetters[17]+ " "+shownLetters[18]+ " "+shownLetters[19]+ " "+shownLetters[20]+ " "+shownLetters[21]+"</div>";
    }
    else if (extendedFingers === 5)
    {
      letters+= shownLetters[22]+ " "+shownLetters[23]+ " "+shownLetters[24]+ " "+shownLetters[25]+"</div>";
    }
    else
    {
      letters += "wait</div>";
    }

  }
  else
  {
    letters="<div>No letter to display! </div>";
  }
  lettersOutput.innerHTML = letters;
  // Store frame for motion functions
  previousFrame = frame;
  

})


