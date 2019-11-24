//Team: Amirali Omidfar, Hannaneh Hojaiji
//Sources: https://canvasjs.com/html5-javascript-dynamic-chart/    
//         https://canvasjs.com/docs/charts/basics-of-creating-html5-chart/updating-chart-options/
//         https://healeycodes.com/javascript/python/beginners/webdev/2019/04/11/talking-between-languages.html
//This code is for this html part of code 

///<div id="chartContainer" style="width:100%; height:280px"></div>  
///<button id="addDataPoint">Add Data Point</button>  
///<button id="updateDataPoint">Update Data Point</button>  


var response = JSON.parse(data);
console.log("The json acc is " + response.A); //prints accelerometer
console.log("The json Vel is " + response.V); //prints velocity
console.log("The json D is " + response.D); //prints distance

window.onload = function () {

var dps = []; // dataPoints
var chart = new CanvasJS.Chart("chartContainer", {
	title :{
		text: "Dynamic Data"
	},
	axisY: {
		includeZero: false
	},      
	data: [{
		type: "line",
		dataPoints: dps
	}]
});

var xVal = 0;
var yVal = 100; 
var updateInterval = 1000;
var dataLength = 20; // number of dataPoints visible at any point

var updateChart = function (count) {

	count = count || 1;

	for (var j = 0; j < count; j++) {
		time.setTime(time.getTime()+ updateInterval);
		yVal = response.V.x;
		dps.push({
			x: xVal,
			y: yVal
		});
		xVal++;
	}

	if (dps.length > dataLength) {
		dps.shift();
	}

	chart.render();
};

updateChart(dataLength);
setInterval(function(){updateChart()}, updateInterval);

}
