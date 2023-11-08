
###### Location of registry files
- Main registry files are located in C:\\Windows\\System32\\config.
- NTuser.dat is the user currently in HKCU and the file is located in %USERPROFILE%.
- There is also a USRclass.dat file located at %USERPROFILE%\\AppData\\Local\\Microsoft\\Windows.

In legacy versions the RegBack directory located within the registry directory contains a back up of the registry files, in newer versions Microsoft has disabled this setting. 

If you wish to re-enable the feature you can modify the following registry key:

```
Path: HKLM\\System\\CurrentControlSet\\Control\\Session Manager\\Configuration Manager\\EnablePeriodicBackup
Type: REG_DWORD
Value: 1
```

###### “LastWrite” Time

- Whenever you modify a registry value, Windows keeps track of the last written time for that particular key/branch. This value is stored as a FILETIME structure and indicates when the Registry Key was last modified. A FILETIME structure contains a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601 (UTC). The LastWrite time is updated whenever a registry key has been created, modified, accessed, or deleted. This data can come handy in timeline analysis.

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32
- The Common Dialog 32 contains the 2 keys LastVisitedPidlMRU and OpenSavePidlMRU for Windows Vista +
- Versions older than Windows Vista utilize LastVisitedPidMRU and OpenSavePidMRU

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSavePidlMRU or HKU\[SID]\Software\Microsoft\Windows\CurrentVersion\Explorer\ ComDlg32\OpenSavePidlMRU
- This key stores the auto-complete information in an open or save window ie. They maintain the information regarding the last opened or saved files.

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\LastVisitedPidlMRU or HKU\[SID]\Software\Microsoft\Windows\CurrentVersion\Explorer\ ComDlg32\LastVisitedPidlMRU
- This key tracks the specific executable used by an application to open the files documented in the OpenSavePidlMRU key. Also each value tracks the directory location for the last file that was accessed by that application. The registry key 

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs
- This registry Key maintains a list of the last ten files that the currently logged on user accessed or executed via Windows Explorer and corresponds to the file listing found in “C:\Users\[Username]\Recent.”

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU
- This registry key contains the list of commands user entered using the Start>Run commands.
- RunMRU (Most Recently Used) registry key has a MRUList value name. The Data associated with the MRUList displays the order of the \*.exe that were ran.

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\TypedPaths
- TypedPaths displays the paths that were manually entered into the Explorer address bar.
	- If path does not exist, it could have be recently deleted.

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist
- User Assist will show us evidence of per-user application execution (GUI programs).
	- Will display when the program was executed and how many times it was executed. The user executing the executables is the one associated with the NTuser.dat file.
- The values within the UserAssist path within are displayed as GUIDs (Globally Unique Identifier)
	- The information inside the GUIDs are ROT13 encoded.

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
- Starts programs on user logon (affects CURRENT USER only)

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce
- Starts programs on user logon (affects CURRENT USER only)

###### HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
- Starts programs on user logon (affects ALL USERS)

###### HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce
- Starts programs on user logon (affects ALL USERS)

###### HKCU\\SOFTWARE\\Microsoft\\Windows\\Shell
- Has subkeys BagMRU and Bags
- Shellbags are set of registry keys which contain details about a user's viewed folder; such as its size, position, and icon. This means that all directory traversal is tracked and maintained in the registry. The Shellbags provide timestamps, contextual information and show the access of directories and other resources, potentially pointing to evidence that one existed.
- Shellbags persist over long period of times.
- Use Shellbags Explorer to parse information
- NTuser.dat and USRclass.dat are both required for forensics.

###### HKLM\\SYSTEM\\CurrentControlSet\\Enum\\USBSTOR
- CurrentControlSet is only displayed on a live system.
- ControlSet<\Number> is displayed on dead system
	- There may be more than one but the value of the sub-key Current within HKLM\\SYSTEM\\Select will display the correct ControlSet to investigate. 
- The device under the key USBSTOR will have a subkey with a string
	- If the string has an & near the end of it then it should be recorded as it indicates that it is a globally unique serial number.
	- If the string has an & at the second character of the string then the manufacturer did not comply with Microsoft's GUID policy. The string is generated only on that system.
###### HKLM\\SYSTEM\\CurrentControlSet\\Enum\\USB
- CurrentControlSet is only displayed on a live system.
- ControlSet<\Number> is displayed on dead system
	- There may be more than one but the value of the sub-key Current within HKLM\\SYSTEM\\Select will display the correct ControlSet to investigate. 
- Vendor Identification (VID) and Product Identification (PID) can be used to find out what type of USB device was connected.
###### HKLM\\SOFTWARE\\Microsoft\\Windows Portable Devices\\Devices
- Find serial # and then look for FriendlyName to obtain the Volume Name of the USB device.
###### HKLM\\SYSTEM\\MountedDevices
- Find serial # to obtain the Drive Letter of the USB device.
- Find serial # to obtain the Volume GUID of the USB device.