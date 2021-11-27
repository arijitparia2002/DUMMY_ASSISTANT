# for more features -> https://www.geeksforgeeks.org/voice-assistant-using-python/

from email import message
from subprocess import TimeoutExpired
from urllib import request
from weakref import ProxyTypes
import pyttsx3 # text data into speech
import datetime # date and time
import speech_recognition as sr # speech from mic to text
import smtplib #email function
import pywhatkit #PyWhatKit is a Python Library for scheduling and sending WhatsApp messages with various other functions like playing a video on YouTube, Converting an image to ASCII art, Converting a string to an image with Hand Written Characters etc.
# from newsapi import NewsApiClient #news updates
from wikipedia.wikipedia import languages, search # to send email
from secret import senderemail,epwd # our module
from email.message import EmailMessage, Message
import pyautogui  #for whatsapp message press enter to send
import webbrowser as wb #for whatsapp message
from time import sleep, time 
import wikipedia
# from newsapi import NewsApiClient
import clipboard # to read selected text
import os # for opening function
import pyjokes # for jokes
import random # for die and flip coin

engine = pyttsx3.init()

#speak function
def speak(string):
    engine.say(string)
    engine.runAndWait()

#changing voice between male and female
def getvoice(voice):
    voices = engine.getProperty("voices")
    rate = engine.getProperty("rate")
    engine.setProperty("rate",190)
    if voice ==1: # male
        engine.setProperty("voice",voices[0].id)
        speak("hello , this is jarvis")
    if voice ==2: # female
        engine.setProperty("voice", voices[1].id)
        speak("hello , this is friday")

#date time function
def Date_time():
    Time = datetime.datetime.now() #2021-07-02 20:25:55.845019
    speak(f"current date is {Time.day} {Time.month} {Time.year}")
    speak(f"current time is {Time.hour} hour{Time.minute} minutes {Time.second} seconds")

# greeting function - greet us according to time
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning ,sir")
    elif hour >= 12 and hour < 16 :
        speak("good evening ,sir")    
    elif hour >= 16 and hour < 20 :
        speak("good evening ,sir")    
    else :
        speak("good night ,sir")

# wish me function
def wishme():
    speak("welcome back sir !")
    Date_time() #datetime fun call
    greeting() #greeting function call
    speak("jarvis at your service , please let me know how can i help you ?")

# taking command from user as input(typed)
def takeCommandCMD():
    query = input("please let me know how can i help you ?\n")
    return query

# func for taking input though mic we use SpeechRecognition module
def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # 1 second
        audio = r.listen(source) #stores source audio in audio variable
    try :
        print("Recognising...")
        query = r.recognize_google(audio, language="en-IN") #english india
        print(query)
    except Exception as e : #IF it cant listen properly
        print(e)
        print("sorry , can't recognise . Please say that again")
        return "None"
    return query

# send email function
def sendEmail(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587) # setting smtp server with the gmail server and port no. of gmail server is 587
    server.starttls()   #transport layer security(TLS) , with this we can make secure to send this code
    #server.login(gmail id , password)
    #so to make it secure we add credential in another file then import it and use , so that no one can see our password
    server.login(senderemail,epwd)
    email = EmailMessage() 
    email['from'] = senderemail
    email['to'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close() # closes connection with our gmail id 

# Send What's App Messages Function
def sendWhatsmsg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message) #open whatsapp web and types automatically
    sleep(8) #sleep 8 seconds program so that browser open
    pyautogui.press("enter") #press enter to send
    
# google search function
def searchGoogle():
    try:
        speak("what should i search for?")
        search = takeCommandMic()
        wb.open('https://www.google.com/search?q='+search)
        speak("searching")
        sleep(1)
        speak(f"here are result for{search}")
        sleep(7) # go for sleep after searching so that we can read before giving next command
    except Exception as e :
        print (e)
        speak("sorry , can't search please try again")

#news updates function
def News():
    newsapi = NewsApiClient(api_key= "075cb3895a664ca0a97ef80212e360c9") # first it connect to our api key, which we got from news api site
    speak("what topic you need the news about ?")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                    language= 'en',
                                    page_size= 5)# this will give top5 news about bitcoin
    newsdata = data['articles'] # stored in newsdata variable 
    for x,y in enumerate(newsdata): # for loop to give update one by one
        print(f'{x} {y["description"]}')
        speak((f'{x} {y["description"]}'))
    speak("that's it for now , i will update you in some time")

# function to read selected text - clipboard module
def text2speech():
    text = clipboard.paste() #copies selected text to text
    print(text)
    speak(text)

# function to flip  a coin
def flip_coin():
    speak("ok sir flipping a coin")
    lis = ['Tails' , 'Heads']
    rand = random.choice(lis)
    print(f"You got : {rand}")
    speak(f"i flipped a coin and you got {rand}")

# function to roll a die
def roll_die():
    speak("ok sir rolling a die")
    lis = [1,2,3,4,5,6]
    rand = random.choice(lis)
    print(f"You got : {rand}")
    speak(f"i rolled a die and you got {rand}")

def run_jarvis():
    #pass
    
    #wishme()
    while True:
        #query = takeCommandCMD().lower() #so that if user type in capital it become lower
        query = takeCommandMic().lower() #so that if user type in capital it become lower
        wake_word1 = "jarvis"
        wake_word2 = "friday"
        if wake_word1 in query or wake_word2 in query: # respond only if it find wake word
            if "date" in query:
                Date_time()

            elif "time" in query:
                Date_time()

            elif "friday" in query: #switching to friday
                speak("ok sir, switching to friday")
                getvoice(2) # female voice

            elif "offline" in query:
                speak("ok sir ,going offline")
                quit() #built in function to quit

            elif  "mail" in query:
                email_list = {
                    "vaibhav" : "vaibhavverma2426@gmail.com",
                    "ayush" : "ayushmahala2@gmail.com",
                    "suyash" : "ssuyash708@gmail.com",
                    "amit" : "amitaich336@gmail.com"
                } #can add more name and there email id
                try :
                    speak("to whome you want to send the mail ")
                    name = takeCommandMic().lower()
                    receiver = email_list[name]
                    speak("what is the subject of the mail?")
                    subject = takeCommandMic()
                    speak("what should i say")
                    content = takeCommandMic()
                    speak(f"do you want me to send email to {name} subject of the mail is {subject} , conent is {content}")
                    permission = takeCommandMic().lower()
                    if "yes" in permission or "ok" in permission:
                        sendEmail(receiver,subject,content)
                        speak("email has been sent")
                    else :
                        speak("ok sir, not sending message")
                except Exception as e:
                    print(e)
                    speak("unable to send the email")
            
            elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "C:\\Users\\ariji\\Music\\songs"
                songs = os.listdir(music_dir)
                print(songs)   
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif "wikipedia" in query: #wikipedia
                try :
                    speak("searching...")
                    query = query.replace("wikipedia","") #replacing with empty string
                    result = wikipedia.summary(query,sentences = 4) # read 4 sentences
                    print(result)
                    speak(result)
                except Exception as e:
                    print(e)
                    speak("unable to search , please try again")

            elif "google" in query:
                searchGoogle()
            
            elif "youtube" in query:
                speak("what should i search for you on you tube sir")
                topic = takeCommandMic() 
                speak("playing video")
                pywhatkit.playonyt(topic) #open and play video on yt (1st suggested video)

            elif "news" in query:
                News()

            elif "read" in query:
                text2speech()

            elif "open chrome" in query: #can add n numbers of software as well as folders
                path = 'C:\Program Files\Google\Chrome\Application\chrome'
                speak("opening chrome")
                os.startfile(path)
                sleep(5) 


            elif "joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "remember" in query: # remember in remember.txt file
                speak("what should i remember?")
                data = takeCommandMic()
                speak(f"you said to remember that {data} , should i remember this?")
                permission = takeCommandMic().lower()
                if "yes" or "ok" in permission:
                    file = open("remember.txt" , "w")
                    speak("Ok sir , remembering")
                    file.write(data)
                    file.close()
                else:
                    speak("OK sir not remembering")

            elif "remind me" in query:
                file = open("remember.txt" , 'r')
                text = file.read()
                print(text)
                speak(text)
                file.close()

            elif "sleep" in query and "minutes" in query: # like sleep for 5 minutes (not minute)
                try:
                    lis = query.split()
                    pos = lis.index("minutes") # ith index of minutes
                    value = lis[pos-1] # before second value
                    value = int(value)
                    sleep_time = 60 * value #minutes
                    speak(f"ok sir going on sleep for {value} minutes")
                    sleep(sleep_time)
                except Exception as e :
                    print(e)
                    speak("please try again")    


            elif "flip" in query:
                flip_coin()   
            
            elif "roll" in query:
                roll_die()   

            elif "game" in query:
                # speak("which game you want to play?")
                # choice = takeCommandMic().lower()
                speak("starting snake , water , gun game")
                speak("let's see who will win")
                won = 0
                lose = 0    
                while True:
                    try:
                        rand = random.randint(1,3)
                        if rand ==1:
                            comp = 'snake'
                        if rand ==2:
                            comp = 'water'
                        if rand ==3:
                            comp = 'gun'
                        speak("what you want to chose")
                        choice = takeCommandMic().lower()
                        if choice =="snake":
                            if comp == "water":
                                print(f"you won , i opted for {comp}")
                                speak(f"you won , i opted for {comp}")
                                won +=1
                            elif comp == "gun":
                                print(f"you lose , i opted for {comp}")
                                speak(f"you lose , i opted for {comp}")
                                lose +=1
                            else :
                                print(f"oh that's tie , i opted for {comp}")
                                speak(f"oh that's tie , i opted for {comp}")

                        elif choice =="water":
                            if comp == "snake":
                                print(f"you lose , i opted for {comp}")
                                speak(f"you lose , i opted for {comp}")
                                lose +=1
                            elif comp == "gun":
                                print(f"you won , i opted for {comp}")
                                speak(f"you won , i opted for {comp}")
                                won +=1
                            else :
                                print(f"oh that's tie , i opted for {comp}")
                                speak(f"oh that's tie , i opted for {comp}")
                    
                        elif choice =="gun":
                            if comp == "snake":
                                print(f"you won , i opted for {comp}")
                                speak(f"you won , i opted for {comp}")
                                won +=1
                            elif comp == "water":
                                print(f"you lose , i opted for {comp}")
                                speak(f"you lose , i opted for {comp}")
                                lose +=1
                            else :
                                print(f"oh that's tie , i opted for {comp}")
                                speak(f"oh that's tie , i opted for {comp}")
                        elif "exit" in choice or "close" in choice:
                            speak("ok sir quiting game")
                            break
                        else :
                            print("please say clearly")
                            speak("please say clearly")
                    except Exception as e :
                        print(e)
                        speak("please say that again")

                print(f"You won {won} times")
                speak(f"You won {won} times")
                print(f"You lose {lose} times")
                speak(f"You lose {lose} times")
                print("Thanks for playing")
                speak("Thanks for playing")


            elif "whatsapp"  in query:
                user_name = {

                    "ayush": "+91 89551 21622",
                    "arijit": "+91 6290 260 865"
                }
                try :
                    speak("to whome you want to send whats app message?")
                    name = takeCommandMic().lower()
                    phone_no = user_name[name]
                    speak("what is the message?")
                    message = takeCommandMic()
                    speak(f"your message is : {message} , do you want me to send this message to {name}")
                    permission = takeCommandMic().lower()
                    if "yes" in permission or "ok" in permission:
                        sendWhatsmsg(phone_no,message)
                        speak("message has been sent")
                    else :
                        speak("ok sir, not sending message")
                except Exception as e:
                    print(e)
                    speak("unable to send the message")

            else :
                speak("Sorry i can't process , please try something else")

        else:
            print("Missing sleep word")
            print(query.split())