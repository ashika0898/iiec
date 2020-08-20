import pyttsx3
import os

pyttsx3.speak("Welcome to windows")


while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	if (("run" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)) and (not("dont" in p) ):
	  os.system("chrome")

	elif (("run" in p) or ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("texteditor" in p)) and (not("dont" in p) ):
	  os.system("notepad")

	elif (("run" in p) or ("open" in p)) and ("skype" in p) and (not("dont" in p) ):
	  os.system("skype")
	
	elif(("run" in p) or ("open" in p)) and ("wps" in p):
	  os.system("ksolaunch")

	elif(("run" in p) or ("open" in p) or ("play" in p)) and (("vlcplayer" in p) or ("mediaplayer" in p) or ("media player" in p) or("vlc player" in p)) and (not("dont" in p) ):
	  os.system("vlc")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("jupyter" in p) or ("notebook" in p)) and (not("dont" in p) ):
	  os.system("jupyter notebook")
	
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("ultraviewer" in p) and (not("dont" in p) ):
	  os.system("UltraViewer_Desktop")
	
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("arduino" in p) and (not("dont" in p) ):
	  os.system("arduino")
	
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("zoom" in p) or ("Zoom" in p)) and (not("dont" in p) ):
	  os.system("Zoom")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("eclipse" in p) and (not("dont" in p) ):
	  os.system("eclipse")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("netbeans" in p) and (not("dont" in p) ):
	  os.system("netbeans64")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("itunes" in p) and (not("dont" in p) ):
	  os.system("iTunes")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("videoeditor" in p) and (not("dont" in p) ):
	  os.system("VideoEditor")
	
	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("acrobat" in p) and (not("dont" in p) ):
	  os.system("AcroRd32")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("explorer" in p)and (not("dont" in p) ):
	  os.system("explorer")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("snippingtool" in p) and (not("dont" in p) ):
	  os.system("SnippingTool")

	elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("prompt" in p) or ("commandprompt" in p)) and (not("dont" in p) ):
	  os.system("cmd")

	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("dont support")


