Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c yt_download.bat"
oShell.Run strArgs, 0, false