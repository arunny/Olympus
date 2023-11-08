#### Filtering Logs with Powershell (Get-WinEvent)

Filter by Event ID: `\*/System/EventID=<\ID>`
Filter by XML Attribute/Name: `\*/EventData/Data[@Name="<XML Attribute/Name>"]`
Filter by Event Data: `\*EventData\Data=<\Data>`

```powershell
Get-WinEvent -Path <Path of Log> -FilterXPath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=4444'


   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
X/X/XXXX H:MM:SS AM              3 Information      Network connection detected:...
```

