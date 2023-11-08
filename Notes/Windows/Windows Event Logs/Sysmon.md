#### Deployment through GPO: 
---
1. __Preparing the distribution point to push the packages__:
	1. Copy the Agent Package on to the Active Directory machine.
	2. On Active Directory, navigate to the location where the Agent package was copied and creat a read only share that can be accessible by all the end-machines.
		1. Right click and open the properties window of "Agent package folder", change to `Sharing` tab and click on `Advanced Sharing`.
		2. Within the `Advanced Sharing` window, check the option `Share this Folder` and provide the share name -> click on `Permissions` underneath the comments section which opens up a new window for setting permissions for the share, set the access permission to `READ ONLY` for Everyone and apply the changes.
		3. This share folder should only be accessible by all end users via the share path like `\\<\AD-Hostname>` with Read-Only access.
2. __Create a Group Policy Object (GPO) to deploy the package:__
	1. Open `Group Policy Management` console from a machine that has access to Active Directory with run or with GUI.
		1. Open `Group Policy Managment` with run dialog.
			1. {Windows Key} + R to open the Run dialog.
			2. Type `gpmc.msc` and click ok.
		2. Open `Group Policy Management` with GUI.
			1. Go to `Start`.
			2. Search for `Administrative Tools`.
			3. Click on `Group Policy Management`.
	1. In the `Group Policy Management` console screen, select the OU you would like to link the new GPO to and create a new GPO while linking it. For example to link the GPO at the domain level.
		1. Expand the `Forest`.
		2. Expand the `Domains OU`
		3. Right click on the <\Domain Name>
		4. Click on the `Create a GPO in this domain, and link it here...` menu item.
				![[Pasted image 20231107175648.png]]
		5. In the new GPO screen, type in the name of your GPO. Then click ok.
		6. Click on the newly created `Group Policy Object`.
		7. Click on the `Details` tab in the right window pain.
		8. Click the `GPO Status` drop down list.
		9. Select the `User configuration settings disabled` menu item. Click Ok.
				![[Pasted image 20231107180016.png]]
		10. In the `Group Policy Management Console Screen`, select the newly created GPO and edit the policy settings.
		11. Right click on the newly created GPO.
		12. Click on "Edit" in the menu list.
		13. We will now create a new Scheduled Task. If you use Immediate Task, it will not show up on Task Scheduler and will run/delete itself after applying itself.
			1. Click the `Computer Configuration` menu item.
			2. Click the `Preferences` menu item. 
			3. Click the `Control Panel Settings` menu item. 
			4. Right click on the `Scheduled Tasks` menu item.
			5. Click on the new menu item.
			6. Click on the `Scheduled Task (At least Windows 7)**”
		14. General Tab.
			1. Select `replace` in the `Action` drop down list
			2. Type a name for this Task in the “**Name**” field. In this case we will type <\TASKNAME>.
			3. Select the `Change User or Group…` button.
			4. Type `System` in the `Enter the object name to select` field
			5. Press the `Check Names` button. Click the “**Ok**” button.
			6. Check the `Run whether user is logged on or not` radio button.
			7. Check the `Run with highest privileges` check box.
			8. Check the `Hidden`check box.
			9. Select `Windows® 7, Windows Server ™ 2008R2` in the `Configure for` drop down list.
			10. Select the `Triggers` Tab. Click on the New… button.
		15. Triggers Tab.
			1. Select `At task creation/modification` in the `Begin the task` drop down list.
			2. Check the `Stop task if it runs longer than` and Select `1 hour` from the drop down list.
			3. Check the `Activate` check box. Leave the default item, which should be the current time.
			4. Check the `Enabled` check box. Click the “**Ok**” button
			5. Select the “**Actions**” tab
		16.  Action Tab.
			1. In the (**New Task (At least Windows 7) Properties**) screen, update the Actions settings for the new Task.
			2. Click on the “**New…**” button.
			3. Select “**Start a program**” in the “**Action**” drop down list.
			4. Type the below path and program name in the “**Program/Script**” field. For this instance we are running.
				1. `C:\Windows\System32\cmd.exe`
			5. Type the below arguments in the “**Add arguments(optional)**” field. Note the path below is the path to your Network Share where the Deploy script is located. For this instance, it’s a UNC on <\ADComputerName>. 
				1. `/c \\<\AD-ComputerName>\<Path>\<\Script File>` 
				2. Click the “**Ok**” button.
		17. Create another Action Task.
			1. Click on new... button.
			2. Select `Start a program` in the `Action` drop down list.
			3. Type the below path and program name in the `Program/Script` field. For this instance, we are running
				1. `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
			4. Type the below arguments in the `Add arguments(optional)` field. Note: We are creating a log file and identifying every time the job is ran.
				1. ` -c $('Processed Job {0} as of {1}' -f '<TASKNAME>', $(Get-Date)) | Out-File -FilePath $('{0}\{1}_GPO_Status.log' -f $Env:TEMP, '<GPO NAME>') -Force`
				2. **Note:** <\TASKNAME> is the name of the Scheduled Job we defined earlier.
				3. **Note:** <\GPO Name> is the name of the GPO we defined earlier. Make sure this is the name of your GPO so the logging make sense. Click Ok.
		18. Create 3rd and final Action Task.
			1. 1. Click on the “**New…**” button
			2. Select `Start a program` in the “**Action**” drop down list
			3. Type the below path and program name in the `Program/Script` field. For this instance, we are running
				1. `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
			4. Type the below arguments in the `Add arguments(optional)` field. Note: We are removing the Scheduled job once it is triggered. This way when GPO runs again it will kick off the same script.
				1. `-c start -FilePath 'schtasks.exe' -ArgumentList '/Delete /TN "SysMonDeployment" /F`
				2. **Note:** <\TASKNAME> is the name of the Scheduled Job we defined earlier. If you change the name of the Scheduled job please change it here or the task will not be deleted. Click the “**Ok**” button
			5. Select the “**Settings**” tab
		19. Settings Tab.
			1. · In the `(New Task (At least Windows 7) Properties**) screen, update the Settings configuration.
			2. Check the `Allow task to be run on demand` check box.
			3. Check the `Run task as soon as possible after a scheduled start is missed` check box.
			4. Check the `Stop the task it if runs longer than` check box and select `1 hour` from the drop down list.
			5. Check the `If the running task does not end when requested, force it to stop` check box
			6. Select `Do not start a new instance` from the `If the task is already running, then the following rule applies` drop down list. Click on the “**Ok**” button
2. Test Deployment via GPO:
	1. Manually push and test the GPO on one of the end-machine which should eventually deploy Agent Package as per the schedule task configured earlier.
		1. Logon to a specific end-machine, launch a command prompt.
		2. Run `gpupdate /force` to force a Group Policy update.
		3. Successful execution of `gpupdate /force` command should pull the respective group policies from the AD, and the deployment tasks for Sysmon should be available in the Task Scheduler on end-machine.
		4. Upon successful execution of respective tasks, you should see following services Sysmon (or) Sysmon64 installed and actively running on the end-machine.

### Confirm Immediate Task was successful
---
- To confirm that an Immediate Task ran, you have to dig through each client's Windows Event Log Information about an individual GPP application is stored in the Group Policy Operational Log, located under Applications and Services in the Event Viewer. Look for `Event ID 4016`, which will notify you when the applicable Group Policy was detected.
#### Confirm Scheduled Task ran
--- 
- To determine if the task actually ran, check the Task Scheduler Operational Log in the Event Viewer folder. This log will have a series of Event IDs, including `Event ID 106 (registering the task)`, `Event ID 107 (triggering the task)` and `Event ID 141 (deleting the registration)`.