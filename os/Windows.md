# Windows commands

## Stash command history

```Shell
rm $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

<a name="profile"></a>
## Create Powershell profile

```powershell
# Create new profile
New-Item $profile -force -itemtype file
# Edit profile
notepad $profile
# Reload profile
. $profile
```

## Install curl

- Download [latest version](https://curl.haxx.se/windows/).
- Remove curl alias by editing $profile (needs [PowerShell profile](#profile))

```powershell
notepad $profile
# Add following line
# Remove-item alias:curl
```
