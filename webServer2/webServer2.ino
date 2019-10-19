// Based on https://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/server-examples.html
//Amirali Omidfar


#include <ESP8266WiFi.h>

const int button1 = 5;     // the number of the pushbutton pin
const int button2 = 4;     // the number of the pushbutton pin
const int button3 = 2;     // the number of the pushbutton pin
const int button4 = 12;     // the number of the pushbutton pin
const int button5 = 13;     // the number of the pushbutton pin


const char* ssid = "lemur";
const char* password = "lemur9473";

WiFiServer server(80);


void setup()
{
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);
  pinMode(button5, INPUT);



  Serial.begin(115200);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  server.begin();
  Serial.printf("Web server started, open %s in a web browser\n", WiFi.localIP().toString().c_str());
}


// prepare a web page to be sent to a client (web browser)
String prepareHtmlPage()
{
  String htmlPage =
    String("HTTP/1.1 200 OK\r\n") +
    "Content-Type: text/html\r\n" +
    "Connection: close\r\n" +  // the connection will be closed after completion of the response
    "Refresh: 0.1\r\n" +  // refresh the page automatically every 2 sec
    "\r\n" +
    "<!DOCTYPE HTML>" +
    "<html>" +
    "Button1 pressed:  " + String(!digitalRead(button1)) + "</br>" +
    "Button2 pressed:  " + String(!digitalRead(button2)) + "</br>" +
    "Button3 pressed:  " + String(!digitalRead(button3)) + "</br>" +
    "Button4 pressed:  " + String(!digitalRead(button4)) + "</br>" +
    "Button5 pressed:  " + String(!digitalRead(button5)) + "</br>" +
    "</html>" +
    "\r\n";
  return htmlPage;
}


void loop()
{
  WiFiClient client = server.available();
  // wait for a client (web browser) to connect
  if (client)
  {
    Serial.println("\n[Client connected]");
    while (client.connected())
    {
      // read line by line what the client (web browser) is requesting
      if (client.available())
      {
        String line = client.readStringUntil('\r');
        Serial.print(line);
        // wait for end of client's request, that is marked with an empty line
        if (line.length() == 1 && line[0] == '\n')
        {
          client.println(prepareHtmlPage());
          break;
        }
      }
    }
    delay(1); // give the web browser time to receive the data

    // close the connection:
    client.stop();
    Serial.println("[Client disonnected]");
  }
}
