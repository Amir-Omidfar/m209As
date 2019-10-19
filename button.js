//Hananneh Hojaiji

var five = require("johnny-five");



board = new five.Board();

board.on("ready", function() {

  // Create a new `button` hardware instance.
  // This example allows the button module to
  // create a completely default instance
  var button1 = new five.Button(2);
  var button2 = new five.Button(3);
  var button3 = new five.Button(4);
  var button4 = new five.Button(5);
  var button5 = new five.Button(6);

  // Inject the `button` hardware into
  // the Repl instance's context;
  // allows direct command line access
 // board.repl.inject({
 //   button: button
  //});

  // Button Event API

  // "down" the button is pressed
  button1.on("down", function() {
    console.log("1down");
  });

  // "hold" the button is pressed for specified time.
  //        defaults to 500ms (1/2 second)
  //        set
  button1.on("hold", function() {
    console.log("1hold");
  });

  // "up" the button is released
  button1.on("up", function() {
    console.log("1up");
  });
  
  
  button2.on("down", function() {
    console.log("2down");
  });

  // "hold" the button is pressed for specified time.
  //        defaults to 500ms (1/2 second)
  //        set
  button2.on("hold", function() {
    console.log("2hold");
  });

  // "up" the button is released
  button2.on("up", function() {
    console.log("2up");
  });
  
  button3.on("down", function() {
    console.log("3down");
  });

  // "hold" the button is pressed for specified time.
  //        defaults to 500ms (1/2 second)
  //        set
  button3.on("hold", function() {
    console.log("3hold");
  });

  // "up" the button is released
  button3.on("up", function() {
    console.log("3up");
  });
  button4.on("down", function() {
    console.log("4down");
  });

  // "hold" the button is pressed for specified time.
  //        defaults to 500ms (1/2 second)
  //        set
  button4.on("hold", function() {
    console.log("4hold");
  });

  // "up" the button is released
  button4.on("up", function() {
    console.log("4up");
  });
  button5.on("down", function() {
    console.log("5down");
  });

  // "hold" the button is pressed for specified time.
  //        defaults to 500ms (1/2 second)
  //        set
  button5.on("hold", function() {
    console.log("5hold");
  });

  // "up" the button is released
  button5.on("up", function() {
    console.log("5up");
  });
});


//Derived from:http://johnny-five.io/api/button/