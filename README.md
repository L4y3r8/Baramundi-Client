# Baramundi-Client
Fun with local baramundi SOAP-API :-)
 
inter-process communication between Baramundi Management Agent "bma.exe" and  Baramundi Traynotifier Service "BMSTrayNotifier.exe" use an unprotected SOAP-API
 
 API calls were enumerated with:
 
--> capture local traffic

--> rabin2 -z bMACore.dll

--> memory dump

An attacker could indirect communicate with baramundi agents through a website which makes a local post request to 

http://localhost:11001/traynotifierservice

http://localhost:11000/clientagent

In this way an attacker could disable input (disable keyboard and mouse), send notifications, arbritary conent to the "AboutDialog" or shutdown the service. 

Unfortunately i didnt find a way to change relevant client configuration or execute a custom baram. job or something like that :-/ .... 




$> rabin2 -z bMACore.dll:

1875 0x0013c624 0x1013d224  33  34 (.rdata) ascii traynotifierclient:GetContextMenu

1876 0x0013c648 0x1013d248  41  42 (.rdata) ascii traynotifierclient:GetContextMenuResponse

1877 0x0013c674 0x1013d274  29  30 (.rdata) ascii traynotifierclient:KMUnlocked

1878 0x0013c694 0x1013d294  28  29 (.rdata) ascii traynotifierclient:GuiAction

1879 0x0013c6b4 0x1013d2b4  36  37 (.rdata) ascii traynotifierclient:GetLanguageString

1880 0x0013c6dc 0x1013d2dc  44  45 (.rdata) ascii traynotifierclient:GetLanguageStringResponse

1881 0x0013c70c 0x1013d30c  30  31 (.rdata) ascii traynotifierclient:GetResource

1882 0x0013c72c 0x1013d32c  38  39 (.rdata) ascii traynotifierclient:GetResourceResponse

1883 0x0013c754 0x1013d354  27  28 (.rdata) ascii traynotifierclient:AlivePid

1884 0x0013c770 0x1013d370  24  25 (.rdata) ascii traynotifierclient:Alive

1885 0x0013c78c 0x1013d38c  23  24 (.rdata) ascii TrayNotifierClient:void

2417 0x0013f9b4 0x101405b4  31  32 (.rdata) ascii traynotifierservice:VersionInfo

2418 0x0013f9d4 0x101405d4  35  36 (.rdata) ascii traynotifierservice:ShutdownService

2419 0x0013f9f8 0x101405f8  30  31 (.rdata) ascii traynotifierservice:CheckAlive

2420 0x0013fa18 0x10140618  31  32 (.rdata) ascii traynotifierservice:EnableInput

2421 0x0013fa38 0x10140638  32  33 (.rdata) ascii traynotifierservice:DisableInput

2422 0x0013fa5c 0x1014065c  37  38 (.rdata) ascii traynotifierservice:ShowLogfileWindow

2423 0x0013fa84 0x10140684  35  36 (.rdata) ascii traynotifierservice:ShowAboutDialog

2424 0x0013faa8 0x101406a8  45  46 (.rdata) ascii traynotifierservice:RemoveActionTimeoutDialog

2425 0x0013fad8 0x101406d8  43  44 (.rdata) ascii traynotifierservice:ShowActionTimeoutDialog

2426 0x0013fb04 0x10140704  39  40 (.rdata) ascii traynotifierservice:IsInfoWindowShowing

2427 0x0013fb2c 0x1014072c  47  48 (.rdata) ascii traynotifierservice:IsInfoWindowShowingResponse

2428 0x0013fb5c 0x1014075c  40  41 (.rdata) ascii traynotifierservice:RemoveAllInfoWindows

2429 0x0013fb88 0x10140788  36  37 (.rdata) ascii traynotifierservice:RemoveInfoWindow

2430 0x0013fbb0 0x101407b0  34  35 (.rdata) ascii traynotifierservice:ShowInfoWindow

2431 0x0013fbd4 0x101407d4  42  43 (.rdata) ascii traynotifierservice:ShowInfoWindowResponse

2432 0x0013fc00 0x10140800  30  31 (.rdata) ascii traynotifierservice:RemoveIcon

2433 0x0013fc20 0x10140820  30  31 (.rdata) ascii traynotifierservice:SetToolTip

2434 0x0013fc40 0x10140840  31  32 (.rdata) ascii traynotifierservice:AnimateIcon

2435 0x0013fc60 0x10140860  36  37 (.rdata) ascii traynotifierservice:ShowNotification

2436 0x0013fc88 0x10140888  30  31 (.rdata) ascii traynotifierservice:ChangeIcon

2437 0x0013fca8 0x101408a8  27  28 (.rdata) ascii traynotifierservice:AddIcon

2438 0x0013fcc4 0x101408c4  35  36 (.rdata) ascii traynotifierservice:AddIconResponse

2439 0x0013fce8 0x101408e8  24  25 (.rdata) ascii traynotifierservice:void
