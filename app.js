var SerialPort = require("serialport").SerialPort;
var serialport = new SerialPort("COM7");
serialport.on('open', function(){
  console.log('Serial Port Opend');
  serialport.on('data', function(data){
      console.log(data[0]);
  });
});


//Source: https://solvemprobler.com/blog/2014/04/12/arduino-and-nodejs-communication-with-serial-ports/