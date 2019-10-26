//Amirali Omidfar, Hananeh Hojaiji, Haisong Lin
//Based on some examples in the given Github 
// https://github.com/leapmotion/leapjs
// For more information please refer to : 
/*!                                                              
 * LeapJS v0.6.4                                                  
 * http://github.com/leapmotion/leapjs/                                        
 *                                                                             
 * Copyright 2013 LeapMotion, Inc. and other contributors                      
 * Released under the Apache-2.0 license                                     
 * http://github.com/leapmotion/leapjs/blob/master/LICENSE.txt                 
 */


var counter=0;
var previousFrame = null;
var paused = false;
var pauseOnGesture = false
var upCounter=0;
var downCounter=0;
var leftCounter=0;
var inputChar='*'

document.onkeydown = function(event) {
        switch (event.keyCode) {
           case 37:
                //alert('Left key pressed');
                leftCounter++;
              break;
           case 38:
                //alert('Up key pressed');
                upCounter++;
                console.log("Up:")
                console.log(upCounter);
              break;
           case 39:
                //alert('Right key pressed');
              break;
           case 40:
                downCounter++;
                console.log("Down:")
                console.log(downCounter);
              break;
        }
    }




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

  /*
  var handfingerCount=[];

  var handOutput = document.getElementById("handData");
  var handString ="";
  for (var i = 0; i < frame.hands.length; i++) {
      var hand = frame.hands[i];
      var extendedFingers = 0;
      for(var f = 0; f < hand.fingers.length; f++){
        var finger = hand.fingers[f];
        if(finger.extended) 
          {
            extendedFingers++;
          }
      }
      handfingerCount[i]=extendedFingers;
      handString+= "<div style='width:250px; float:left; padding:5px'>";
      handString+="hand ID: " + hand.id + "<br />";
      handString+="extendedFingers: " +  extendedFingers+ "<br />"+"</div>";

    }
    handOutput.innerHTML=handString;
    */




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

  //var lettersOutput = document.getElementById("letters");
  if (fingerCount != "<div></div>")
  {
    //letters="<div style='width:250px; float:left; padding:5px'>"
    //letters="Select from:"+"<br />";
    
    
    if (extendedFingers == 0){

      //letters+= shownLetters[0]+ " "+shownLetters[1]+ " "+shownLetters[2]+ " "+shownLetters[3]+"</div>";
      
      document.getElementById("b1").innerText = "a";
      document.getElementById("b2").innerText = "b";
      document.getElementById("b3").innerText = "c";
      document.getElementById("b4").innerText = "d";
      document.getElementById("b5").innerText = "space";

      document.getElementById("img").src="finger 0.png";
      

      if(upCounter==1){
        if (downCounter==1)
        {
          inputChar='a'
          //document.getElementById("result").innerHTML=inputChar;
        }
        if (downCounter==2)
        {
          inputChar='b'
          //document.getElementById("result").innerHTML=inputChar;
        }
        if (downCounter==3)
        {
          inputChar='c'
          //document.getElementById("result").innerHTML=inputChar;
        }
        if (downCounter==4)
        {
          inputChar='d'
          //document.getElementById("result").innerHTML=inputChar;
        }
        if (downCounter ==5)
        {
          inputChar=' '
          //document.getElementById("result").innerHTML=inputChar;
        }
        if (downCounter == 5)
          document.getElementById("result").innerHTML="tab";
        else
        document.getElementById("result").innerHTML=inputChar;

      }
      else if (upCounter == 2)
      {
        var text = document.getElementById('input')
          var l= text.value.length
          if (text.value[l-1] != inputChar)
            {
              text.value += inputChar;
            }
          downCounter=0;
          upCounter=0;
      }        
    }
    else if (extendedFingers == 1)
    {
      //letters+= shownLetters[4]+ " "+shownLetters[5]+ " "+shownLetters[6]+ " "+shownLetters[7]+"</div>";
      document.getElementById("b1").innerText = "e";
      document.getElementById("b2").innerText = "f";
      document.getElementById("b3").innerText = "g";
      document.getElementById("b4").innerText = "h";
      document.getElementById("b5").innerText = "back sapce";

      document.getElementById("img").src="finger 1.png";

      if(upCounter==1){
        if (downCounter==1)
        {
          inputChar='e'
        }
        if (downCounter==2)
        {
          inputChar='f'
        }
        if (downCounter==3)
        {
          inputChar='g'
        }
        if (downCounter==4)
        {
          inputChar='h'
        }
        if (downCounter ==5)
        {
          inputChar=' '
        }   
        if (downCounter == 5)
          document.getElementById("result").innerHTML="Del";
        else
        document.getElementById("result").innerHTML=inputChar;
      }
      else if (upCounter == 2)
      {
        var text = document.getElementById('input')
        var l= text.value.length
        if (downCounter != 5)
        {
          if (text.value[l-1] != inputChar)
            {
              text.value += inputChar;
            }
        }
        else
        {
          var newText=text.value.substring(0, text.value.length - 1);
          text.value=newText;
        }
          
          downCounter=0;
          upCounter=0;
      }
        
    }
    else if (extendedFingers === 2)
    {
      //letters+= shownLetters[8]+ " "+shownLetters[9]+ " "+shownLetters[10]+ " "+shownLetters[11]+"</div>";
      document.getElementById("b1").innerText = "i";
      document.getElementById("b2").innerText = "j";
      document.getElementById("b3").innerText = "k";
      document.getElementById("b4").innerText = "l";
      document.getElementById("b5").innerText = ".";

      document.getElementById("img").src="finger 2.png";


      if(upCounter==1){
        if (downCounter==1)
        {
          inputChar='i'
        }
        if (downCounter==2)
        {
          inputChar='j'
        }
        if (downCounter==3)
        {
          inputChar='k'
        }
        if (downCounter==4)
        {
          inputChar='l'
        }
        if (downCounter ==5)
        {
          inputChar='.'
        }   
        document.getElementById("result").innerHTML=inputChar;
      }
      else if (upCounter == 2)
      {
        var text = document.getElementById('input')
          var l= text.value.length
          if (text.value[l-1] != inputChar)
            {
              text.value += inputChar;
            }
          downCounter=0;
          upCounter=0;
      }

      
    }
    else if (extendedFingers === 3)
    {
      //letters+= shownLetters[12]+ " "+shownLetters[13]+ " "+shownLetters[14]+ " "+shownLetters[15]+ " "+shownLetters[16]+"</div>";
      document.getElementById("b1").innerText = "m";
      document.getElementById("b2").innerText = "n";
      document.getElementById("b3").innerText = "o";
      document.getElementById("b4").innerText = "p";
      document.getElementById("b5").innerText = "q";

      document.getElementById("img").src="finger 3.png";

      if(upCounter==1){
        if (downCounter==1)
        {
          inputChar='m'
        }
        if (downCounter==2)
        {
          inputChar='n'
        }
        if (downCounter==3)
        {
          inputChar='o'
        }
        if (downCounter==4)
        {
          inputChar='p'
        }
        if (downCounter ==5)
        {
          inputChar='q'
        }   
        document.getElementById("result").innerHTML=inputChar;
      }
      else if (upCounter == 2)
      {
        var text = document.getElementById('input')
          var l= text.value.length
          if (text.value[l-1] != inputChar)
            {
              text.value += inputChar;
            }
          downCounter=0;
          upCounter=0;
      }

      
    }
    else if (extendedFingers === 4)
    {
      //letters+= shownLetters[17]+ " "+shownLetters[18]+ " "+shownLetters[19]+ " "+shownLetters[20]+ " "+shownLetters[21]+"</div>";
      document.getElementById("b1").innerText = "r";
      document.getElementById("b2").innerText = "s";
      document.getElementById("b3").innerText = "t";
      document.getElementById("b4").innerText = "u";
      document.getElementById("b5").innerText = "v";

      document.getElementById("img").src="finger 4.png";

      if(upCounter==1){
        if (downCounter==1)
        {
          inputChar='r'
        }
        if (downCounter==2)
        {
          inputChar='s'
        }
        if (downCounter==3)
        {
          inputChar='t'
        }
        if (downCounter==4)
        {
          inputChar='u'
        }
        if (downCounter ==5)
        {
          inputChar='v'
        }  
        document.getElementById("result").innerHTML=inputChar; 
      }
      else if (upCounter == 2)
      {
        var text = document.getElementById('input')
          var l= text.value.length
          if (text.value[l-1] != inputChar)
            {
              text.value += inputChar;
            }
          downCounter=0;
          upCounter=0;
      }
    }
    else if (extendedFingers === 5)
    {
      //letters+= shownLetters[22]+ " "+shownLetters[23]+ " "+shownLetters[24]+ " "+shownLetters[25]+"</div>";
      document.getElementById("b1").innerText = "w";
      document.getElementById("b2").innerText = "x";
      document.getElementById("b3").innerText = "y";
      document.getElementById("b4").innerText = "z";
      document.getElementById("b5").innerText = ",";

      document.getElementById("img").src="finger 5.png";

      if(upCounter==1){
        if (downCounter==1)
        {
          inputChar='w'
        }
        if (downCounter==2)
        {
          inputChar='x'
        }
        if (downCounter==3)
        {
          inputChar='y'
        }
        if (downCounter==4)
        {
          inputChar='z'
        }
        if (downCounter ==5)
        {
          inputChar=','
        } 
        document.getElementById("result").innerHTML=inputChar;  
      }
      else if (upCounter == 2)
      {
        var text = document.getElementById('input')
          var l= text.value.length
          if (text.value[l-1] != inputChar)
            {
              text.value += inputChar;
            }
          downCounter=0;
          upCounter=0;
      }

      
    }
    else
    {
      //letters += "wait</div>";
    }

  }
  else
  {
    
    //letters="<div>No letter to display! </div>";
    document.getElementById("b1").innerText = "";
    document.getElementById("b2").innerText = "";
    document.getElementById("b3").innerText = "";
    document.getElementById("b4").innerText = "";
    document.getElementById("b5").innerText = "";
    document.getElementById("img").src="default.png";
    
  }
  //lettersOutput.innerHTML = letters;
  // Store frame for motion functions
  previousFrame = frame;
  //counter++;
  
})


function myFunction() {
  var x = document.getElementById("img").src;
  document.getElementById("demo").innerHTML = x;
}











