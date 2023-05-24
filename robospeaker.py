# importing the required Module
import pyttsx3

# # #
print("ROBO SPEAKER".center(100))
# # #
# Module Commands
Robo=pyttsx3.init()
Robo.setProperty('rate',125)
Robo.say("Good Morning sir I can convert your typed text into speech")
Robo.say("Enter the text which you want convert into speech")
Robo.runAndWait()
# while loop
while True:
    a=input("Enter your text here: ")
    if(a=="end"):
        Robo.say("Program ending")
        Robo.runAndWait()
        break
    Robo.say(a)
    Robo.runAndWait() 



