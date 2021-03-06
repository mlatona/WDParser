#!/usr/bin/python
###
# WD-Clientraw-Parse
#
# A basic parser for the clientraw.txt file generated by the Weather Display
# weather center monitoring application.
#
# Fetches a file from a URL, parses it and spits out various bits of information.
# 
# @author Marcus Povey <marcus@marcus-povey.co.uk>
# @copyright Marcus Povey 2013
# @link http://www.marcus-povey.co.uk
# 
# Copyright (c) 2013 Marcus Povey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###

import getopt
import urllib
import sys

def usage():
	print("WD-Clientraw-Parse v1.0 By Marcus Povey <marcus@marcus-povey.co.uk>");
	print
	print("Usage: python wd-parse.py -u http://www.example.com/path/to/clientraw.txt [-o \"formatted list of output\"]")
	print
	print("Format string similar to 'Wind speed: {{option}}, Temperature: {{option}}'")
	print
	print("Where 'option' is one of the keys to return:")
	print("1	Wind: Speed - Average - Current	(Knots)")
	print("2	Wind: Speed - Current	(Knots)")
	print("3	Wind: Dir - Current		(Compass heading)")
	print("4	Temp: Outside - Current	(Celsius)")
	print("5	Humidity: Outside - Current	(Percent)")
	print("6	Baro: Current	(hPa)")
	print("7	Rain: Today - Current total	(Millimeters)")
	print("8	Rain: Total for Month	(Millimeters)")
	print("9	Rain: Total for Season	(Millimeters)")
	print("10	Rain: Rain Rate - Current	(Millimeters)")
	print("11	Rain: Rain Rate - Max	(Millimeters)")
	print("12	Temp: Indoor - Current	(Celsius)")
	print("13	Humidity: Indoor - Current	(Percentage)")
	print("14	Soil: Temperature	(Celsius)")
	print("15	Forecast Icon	(Icon)")
	print("16	Temp: Extra Sensor (Celsius)")
	print("17	Humidity: Extra Sensor (Percent)")
	print("18	Extra: Extra Sensor (Number)")
	print("19	Rain: Total for Yesterday	(Millimeters)")
	print("20	Temp: Extra Sensor 1	(Celsius - Optional)")
	print("21	Temp: Extra Sensor 2	(Celsius - Optional)")
	print("22	Temp: Extra Sensor 3	(Celsius - Optional)")
	print("23	Temp: Extra Sensor 4	(Celsius - Optional)")
	print("24	Temp: Extra Sensor 5	(Celsius - Optional)")
	print("25	Temp: Extra Sensor 6	(Celsius - Optional)")
	print("26	Humidity: Extra Sensor 1	(Percent - Optional)")
	print("27	Humidity: Extra Sensor 2	(Percent - Optional)")
	print("28	Humidity: Extra Sensor 3	(Percent - Optional)")
	print("29	Date/Time: Time - Hour	(Time - 24hr clock)")
	print("30	Date/Time: Time - Minute 	(Time - 24hr clock)")
	print("31	Date/Time: Time - Seconds	(Time - 24hr clock)")
	print("32	Station Name	(Label)")
	print("33	Lightning: Strikes - in Total	(Number)")
	print("34	Solar: Current reading (0% - 100%)	(Number)")
	print("35	Date/Time: Date - Day	(Time)")
	print("36	Date/Time: Date - Mth	(Time)")
	print("37	Battery: battery 1	(Percent - Optional)")
	print("38	Battery: battery 2	(Percent - Optional)")
	print("39	Battery: battery 3	(Percent - Optional)")
	print("40	Battery: battery 4	(Percent - Optional)")
	print("41	Battery: battery 5	(Percent - Optional)")
	print("42	Battery: battery 6	(Percent - Optional)")
	print("43	Battery: battery 7	(Percent - Optional)")
	print("44	Feelslike: Windchill - Current	(Celsius)")
	print("45	Feelslike: Humidex - Current	(Celsius)")
	print("46	Temp: Outside - Today - Max	(Celsius)")
	print("47	Temp: Outside - Today - Min	(Celsius)")
	print("48	Forecast: Icon Type	(Icon)")
	print("49	Forecast: Weather Description	(Label)")
	print("50	Baro: Trend	(hPa)")
	print("51	Wind: Speed - Hour 01	(Knots)")
	print("52	Wind: Speed - Hour 02	(Knots)")
	print("53	Wind: Speed - Hour 03	(Knots)")
	print("54	Wind: Speed - Hour 04	(Knots)")
	print("55	Wind: Speed - Hour 05	(Knots)")
	print("56	Wind: Speed - Hour 06	(Knots)")
	print("57	Wind: Speed - Hour 07	(Knots)")
	print("58	Wind: Speed - Hour 08	(Knots)")
	print("59	Wind: Speed - Hour 09	(Knots)")
	print("60	Wind: Speed - Hour 10	(Knots)")
	print("61	Wind: Speed - Hour 11	(Knots)")
	print("62	Wind: Speed - Hour 12	(Knots)")
	print("63	Wind: Speed - Hour 13	(Knots)")
	print("64	Wind: Speed - Hour 14	(Knots)")
	print("65	Wind: Speed - Hour 15	(Knots)")
	print("66	Wind: Speed - Hour 16	(Knots)")
	print("67	Wind: Speed - Hour 17	(Knots)")
	print("68	Wind: Speed - Hour 18	(Knots)")
	print("69	Wind: Speed - Hour 19	(Knots)")
	print("70	Wind: Speed - Hour 20	(Knots)")
	print("71	Wind: Speed - Gust - Max	(Knots)")
	print("72	Dewpoint: - Current	(Celsius)")
	print("73	Forecast: Cloud Height	(Feet)")
	print("74	Date/Time: Date (WD format)	(Label - WD: M/D/Y or D/M/Y)")
	print("75	Feelslike: Humidex - Max	(Celsius")
	print("76	Feelslike: Humidex - Min	(Celsius)")
	print("77	Feelslike: Windchill - Max	(Celsius)")
	print("78	Feelslike: Windchill - Min	(Celsius)")
	print("79	UV: Current reading (0-16 index)	(Number)")
	print("80	Wind: 60 Minutes ago (Knots)")
	print("81	Wind: 54 Minutes ago (Knots)")
	print("82	Wind: 48 Minutes ago (Knots)")
	print("83	Wind: 42 Minutes ago (Knots)")
	print("84	Wind: 36 Minutes ago (Knots)")
	print("85	Wind: 30 Minutes ago (Knots)")
	print("86	Wind: 24 Minutes ago (Knots)")
	print("87	Wind: 18 Minutes ago (Knots)")
	print("88	Wind: 12 Minutes ago (Knots)")
	print("89	Wind: 06 Minutes ago (Knots)")
	print("90	Temp: Outside - 60 Minutes ago	(Celsius)")
	print("91	Temp: Outside - 54 Minutes ago	(Celsius)")
	print("92	Temp: Outside - 48 Minutes ago	(Celsius)")
	print("93	Temp: Outside - 42 Minutes ago	(Celsius)")
	print("94	Temp: Outside - 36 Minutes ago	(Celsius)")
	print("95	Temp: Outside - 30 Minutes ago	(Celsius)")
	print("96	Temp: Outside - 24 Minutes ago	(Celsius)")
	print("97	Temp: Outside - 18 Minutes ago	(Celsius)")
	print("98	Temp: Outside - 12 Minutes ago	(Celsius)")
	print("99	Temp: Outside - 06 Minutes ago	(Celsius)")
	print("100	Rain: 60 Minutes ago (Millimeters)")
	print("101	Rain: 54 Minutes ago (Millimeters)")
	print("102	Rain: 48 Minutes ago (Millimeters)")
	print("103	Rain: 42 Minutes ago (Millimeters)")
	print("104	Rain: 36 Minutes ago (Millimeters)")
	print("105	Rain: 30 Minutes ago (Millimeters)")
	print("106	Rain: 24 Minutes ago (Millimeters)")
	print("107	Rain: 18 Minutes ago (Millimeters)")
	print("108	Rain: 12 Minutes ago (Millimeters)")
	print("109	Rain: 06 Minutes ago (Millimeters)")
	print("110	Feelslike: Heat Index - Max	(Celsius)")
	print("111	Feelslike: Heat Index - Min	(Celsius)")
	print("112	Feelslike: Heat Index - Current	(Celsius)")
	print("113	Wind: Speed - Avarage - Max	(Knots)")
	print("114	Lightning: Strikes - in last Min (Number)")
	print("115	Lightning: Last Strike - Hour (Time)")
	print("116	Lightning: Last Strike - Min (Time)")
	print("117	Wind: Dir - Average	(Compass heading)")
	print("118	Lightning: Last Strike - Distance (Nexstorm) (Number)")
	print("119	Lightning: Last Strike - Bearing (Nexstorm)	(Compass heading)")
	print("120	Temp: Extra Sensor 7	(Celsius - Optional)")
	print("121	Temp: Extra Sensor 8	(Celsius - Optional)")
	print("122	Humidity: Extra Sensor 4	(Percent - Optional)")
	print("123	Humidity: Extra Sensor 5	(Percent -Optional)")
	print("124	Humidity: Extra Sensor 6	(Percent - Optional)")
	print("125	Humidity: Extra Sensor 7	(Percent - Optional)")
	print("126	Humidity: Extra Sensor 8	(Percent - Optional)")
	print("127	Solar: VP Solar W/sqM (0 - 1800 W/sqM)	(Number)")
	print("128	Temp: Indoor - Max	(Celsius)")
	print("129	Temp: Indoor - Min	(Celsius)")
	print("130	Feelslike: Apparent Temp - Current	(Celsius)")
	print("131	Baro: Max	(hPa)")
	print("132	Baro: Min	(hPa)")
	print("133	Wind: Gust - Max (Knots)")
	print("134	Wind: Gust - Max - in last Hour (Time)")
	print("135	Wind: Gust - Max Today (Time)")
	print("136	Feelslike: Apparent Temp - Max	(Celsius)")
	print("137	Feelslike: Apparent Temp - Min	(Celsius)")
	print("138	Dewpoint: - Max	(Celsius)")
	print("139	Dewpoint: - Min	(Celsius)")
	print("140	Wind: Gust - Max - in last Minute	(Knots)")
	print("141	Date/Time: Date - Year	(Time)")
	print("142	THSWS:	(Celsius - If enabled in WD)")
	print("143	Temp: Outside - Current - Trend	(Boolean)")
	print("144	Humidity: Outside - Trend	(Boolean)")
	print("145	Feelslike: Humidex - Trend	(Boolean)")
	print("146	Wind: Dir - 60 Minutes ago	(Compass heading)")
	print("147	Wind: Dir - 54 Minutes ago	(Compass heading)")
	print("148	Wind: Dir - 48 Minutes ago	(Compass heading)")
	print("149	Wind: Dir - 42 Minutes ago	(Compass heading)")
	print("150	Wind: Dir - 36 Minutes ago	(Compass heading)")
	print("151	Wind: Dir - 30 Minutes ago	(Compass heading)")
	print("152	Wind: Dir - 24 Minutes ago	(Compass heading)")
	print("153	Wind: Dir - 18 Minutes ago	(Compass heading)")
	print("154	Wind: Dir - 12 Minutes ago	(Compass heading)")
	print("155	Wind: Dir - 06 Minutes ago	(Compass heading)")
	print("156	Leaf: Wetness (0-15)	(Number - Optional)")
	print("157	Soil: Moisture (0-200 centibars)	(Number - Optional)")
	print("158	Wind: Speed - Average - 10 Minute	(Knots)")
	print("159	Temp: Wetbulb Temperature	(Celsius)")
	print("160	:GPS: Latitude (-ve for South)	(Number)")
	print("161	:GPS: Longitude (-ve for East)	(Number)")
	print("162	Rain: Today - 9am reset total	(Millimeters)")
	print("163	Humidity: Outside - Max	(Percent)")
	print("164	Humidity: Outside - Min	(Percent)")
	print("165	Rain: Today - Midnight reset total	(Millimeters)")
	print("166	Feelslike: Windchill - Min - Time	(Time)")

def main():
	
	url = None
	format = "{{32}} at {{29}}:{{30}}.{{31}}, {{35}}/{{36}}/{{141}}: Wind: {{3}} deg at {{2}} knots (gusts: {{133}} knots), Pressure: {{6}} hPa"

	try:
		opts, args = getopt.getopt(sys.argv[1:], "u:o:h", ["help"])
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit()

	for o, a in opts:
		if o == "-u":
			url = a
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o == "-o":
			format = a
		else:
			usage()
			sys.exit()
			
	if url == None or format == None:
		usage()
		sys.exit()

	response = urllib.urlopen(url)
	data = response.read()
	
	bits = data.split(' ')
	n = 0;
	for item in bits:
		trim = item.strip()
		format = format.replace('{{' + str(n) + '}}', trim)
		n = n+1
		
	print format
	
if __name__ == "__main__":
    #main()