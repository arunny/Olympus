# What are Shellbags?

Shellbags are set of registry keys which contain details about a user’s viewed folder; such as its size, position, and icon. This means that all directory traversal is tracked and maintained in the registry.

The shellbags provide timestamps, contextual information, and show the access of directories and other resources, potentially pointing to evidence that once existed. A shellbag entry is created for every newly explored folder.

Analysis of shellbags is useful as it can aid in the creating a broader picture of an investigation, providing indications of activity, acting as a history of what directory items may have since been removed from a system, or even evidence access of removable devices where are no longer attached.

# Where are Shellbags?

Shellbags are located within `NTuser.dat` (Windows XP) or within `UserClass.dat` (Windows 7 and later) hives, under `HKCU` `(HKEY_CURRENT_USER)` _(or_ `_HKCR_` _for Win7+)_

![](https://miro.medium.com/v2/resize:fit:700/1*Ktt4waB4MOyu8ETpuGb5cA.png)

Shellbag locations

The shellbags held in BagMRU follow a similar structure and hierarchy as found within the Explorer, with the numbered folders representing parent/child folders.

![](https://miro.medium.com/v2/resize:fit:700/1*-6zj5FIpfqjrHSpiInLgRA.png)

Registry view of Shell BagMRU

Within these are the shellbags themselves, as well as set of keys which provide information on the shellbags.

![](https://miro.medium.com/v2/resize:fit:586/1*M49mV-aK6eUX3aSahNtjZQ.png)

Shellbag Key data

This data is stored in hex so is difficult to determine the path and other valuable details. To be able to understand the activities of the user, special tools and be used to format and parse the data.

# Key artifacts

Before using a tool to interpret shellbags, an understanding of what artefacts can be found will be very useful.

Shellbag analysis can expose information regarding:

- Folder access

_For example, desktop items, control panel categories/items, drive letter, directories, or even compressed archives_

- Evidence of folder deletion, overwriting, or renaming
- Directory navigation and traversal patterns

_This might also include evidence of remote access (e.g. RDP or VNC), as well as dropping of binaries or access to network resources._

# Shellbag Analysis Tools

Now we know what shellbags are, where they’re located, and what sort of information they can tell us.

From a registry perspective, tools like RegEdit or [RegRipper](https://github.com/keydet89/RegRipper3.0) will help us to find the shellbegs but doesn’t help too much with any information to aid in an investigation.

Shellbags Explorer, however, will help with browsing shellbag data.

## ShellBags Explorer

[Eric Zimmerman’s](https://ericzimmerman.github.io/#!index.md) **Shellbags Explorer** is a really useful tool for exploring shellbags data in GUI or CLI, and is able to provide a visual representation of user’s directory structure, allowing analysis of bags recursively to sort, filter, and manipulate in other ways. **Shellbags Explorer** exposes timestamps, for example, creation, accessed, and interaction, so a timeline can be created.

![](https://miro.medium.com/v2/resize:fit:700/1*-6ZVOGTVeaCyp8mxAm6jDA.png)