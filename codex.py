import openai

openai.api_key = "YOUR_API_KEY_HERE"

compilePrompt = """#Convert comments into python code. The necessary packages must be imported.

#CMD: Store a random value from 0 to 100 and call it ABC.
import random
ABC = random.randint(0,100)

#CMD: print 'hello world' 3 times
for i in range(0,3):
    print('hello world')

#CMD: print a random number
print(random.random())

#CMD: ask the user for input
input = input("Enter some text:")

    #CMD: Create a python web socket at port 2242 and print the address
    import websocket
    ws = websocket.WebSocket()
    ws.bind(('',2242))
    print(ws.getsockname())

#CMD: Create a UI window with a button using the python 
from ui import Button, View
btn = Button('hello')

def btn_touch(src,*args):
    print("the button was touched")
    
btn.touch = btn_touch
view = View(frame=(0, 0, 100, 220))
btn.center = view.width / 2, view.height/2 
view.add_subview(btn)

# CMD: Create a maximum number of 100
max = 100

# CMD: Repeat forever...
while True:

    # CMD: Store a number between 1 and the maximum number. Call it the answer.
    answer = random.randint(1,max)
    
    # CMD: Increase the maximum number by 20.
    max = max + 20
    
    # CMD: Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
    print("I am thinking of a number between 0 and " + str(max))
    
    # CMD: Repeat 14 times...
    for i in range(0,14):
    
        # CMD: Ask the user for a guess, and Convert it to a number
        guess = int(input("Guess a number:"))
        
        # CMD: If the guess is equal to the answer, congradulate the user and end the loop.
        if guess == answer:
            print("You guessed it!")
            break;
            
        # CMD: Otherwise if the guess is higher or lower than the answer, tell the user.
        elif guess > answer:
            print("Your guess is too high")
        else: 
            print("Your guess is too low")
            
        # CMD: Tell the user how many chances are left.
        print("You have " + str(14 - i) + " chances left")
        
    # CMD: When loop has ended, If user has not guessed the answer, tell the user game over and then exit the game.
    if guess != answer:
        print("Game over")
        exit()
"""
correctionPrompt = """#Correct the tabs and syntax of this document:
Create a maximum number of 100
Repeat forever...
Store a number between 1 and the maximum number. Call it the answer.
Increase the maximum number by 20
Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
Repeat 14 times...
Ask the user for a guess, and Convert it to a number
If the guess is equal to the answer, congradulate the user and end the loop.
Otherwise if the guess is higher or lower than the answer, tell the user.
Tell the user how many chances are left.
If the loop has ended and the user has not guessed the answer, tell the user game over
and then exit the game


#Corrected document:
Create a maximum number of 100

Repeat forever...
    Store a number between 1 and the maximum number. Call it the answer.
    Increase the maximum number by 20.
    Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
    Repeat 14 times...
        Ask the user for a guess, and Convert it to a number
        If the guess is equal to the answer, congradulate the user and end the loop.
        Otherwise if the guess is higher or lower than the answer, tell the user.
        Tell the user how many chances are left.
    When loop has ended, If user has not guessed the answer, tell the user game over and then exit the game.


#Correct the tabs and syntax of this document:
Repeat 10 times under var x
Repeat 10 times under var y
say the x and the y



#Corrected document:
Iterate 10 times with the variable x
    Iterate 10 times with the variable y
        Print the x and y
     
     
        
#Correct the tabs and syntax of this document:
Repeat 100 times under var x
        Repeat 10 times under var y2
say the x and the y2



#Corrected document:
Iterate 10 times with the variable x
    Iterate 100 times with the variable y2
        Print the x and y2



#Correct the tabs and syntax of this document:
iterate 5 times and say hello each time



#Corrected document:
Repeat 5 times
    Say hello



#Correct the tabs and syntax of this document:
Make a UI window
Add a button to that window
Add a text box.

Ask the user for input.
Tell the user happy birthday
If the user enters "ASDF", exit the program.



#Corrected document:
Make a UI window
Add a button to that window
Add a text box.

Ask the user for input.
Tell the user happy birthday
If the user enters "ASDF", exit the program.

#Correct the tabs and syntax of this document:
"""

codeCorrection = """#Fix this python code:
import random

# CMD: Create a maximum number of 100
max = 100
# CMD: Repeat forever...
while True:
    # CMD: Store a number between 1 and the maximum number. Call it the answer.
    answer = random.randint(1,max)
    # CMD: Increase the maximum number by 20.
    max = max + 20
    # CMD: Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
    print("I am thinking of a number between 0 and " + str(max))
    # CMD: Repeat 14 times...
    for i in range(0,14):
        # CMD: Ask the user for a guess, and Convert it to a number
        guess = int(input("Guess a number:"))
        # CMD: If the guess is equal to the answer, congradulate the user and end the loop.
        if guess == answer:
            print("You guessed it!")
            break;
        # CMD: Otherwise if the guess is higher or lower than the answer, tell the user.
        elif guess > answer:
            print("Your guess is too high")
        else: 
            print("Your guess is too low")
        # CMD: Tell the user how many chances are left.
        print("You have " + str(14 - i) + " chances left")
    # CMD: When loop has ended, If user has not guessed the answer, tell the user game over and then exit the game.
    if guess != answer:
        print("Game over")
        exit()



#Fixed Code:
import random

max = 100.
while True:
    answer = random.randint(1,max)
    max = max + 20
    print("I am thinking of a number between 0 and " + str(max))
    for i in range(0,14):
        guess = int(input("Guess a number:"))
        if guess == answer:
            print("You guessed it!")
            break;
        elif guess > answer:
            print("Your guess is too high")
        else: 
            print("Your guess is too low")
        print("You have " + str(14 - i) + " chances left")
    if guess != answer:
        print("Game over")
        exit()
        
        
        
#Fix this python code:
 with open(filename+".nl", 'r') as file:
        for line in tqdm (file):
line = line.replace("\n", "").replace("\r", "").replace("\"", "'")
        #CMD: Strip the line
        if line.strip() == "":
            fileStr += "\n"
            #CMD: Otherwise, the original line, equals the line, and add the line so fileStr
            otherwise:
                origLine = line;
                line = "\n"+__getStartingTabs(line)+"# CMD: " + line.strip()+"\n";
                fileStr += line;
                response = null
                for i in range(0,5):
                    response = codex.completeDavinci(
                        prompt=fileStr,
                        temperature=0.0,
                        frequency_penalty=1.0,
                        presence_penalty=1.4,
                        stop=["#""]
                    )
#CMD: If the response is not empty, add the last response to the fileStr and end the loop
if(not response.strip() == ''):
    fileStr += response
    break;
                    else:
                        println("Line: \""+origLine.strip()+"\" hasn't produced any code: ("+str(i)+"\\5)...")
                        
 
                        
#Fixed code:
 with open(filename+".nl", 'r') as file:
        for line in tqdm(file):
            line = line.replace("\n", "").replace("\r", "").replace("\"", "'")
            if line.strip() == "":
                fileStr += "\n"
            else:
                origLine = line
                line = "\n"+__getStartingTabs(line)+"# CMD: " + line.strip()+"\n"
                fileStr += line
                response = ''
                for i in range(0,5):
                    response = codex.completeDavinci(
                        prompt=fileStr,
                        temperature=0.0,
                        frequency_penalty=1.0,
                        presence_penalty=1.4,
                        stop=["#"]
                    )
                    if(not response.strip() == ''):
                        fileStr += response
                        break
                    else:
                        print("Line: \""+origLine.strip()+"\" hasn't produced any code: ("+str(i)+"\\5)...")
                     
                     
                     
                        
#Fix this python code:
"""

def __getText(response):
    return response['choices'][0]["text"]

def completeDavinci(prompt="",temperature=0.2,max_tokens=1000,frequency_penalty=0.2,presence_penalty=0.3,stop=[]):
    return __getText(openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop
    ))

def completeCushman(prompt="",temperature=0.2,max_tokens=1000,frequency_penalty=0.2,presence_penalty=0.3,stop=[]):
    return __getText(openai.Completion.create(
        engine="cushman-codex",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop
    ))

def correctTabs(filename,savePath):
    print("Correcting:",filename+"...")
    if not filename.endswith(".nl"):
        return
    with open(filename, 'r') as file:
        lines = file.read().replace("\r", "\n")

        newDoc = ''
        for i in range(0, 10):
            newDoc = completeDavinci(
                prompt=correctionPrompt + lines + "\n#Corrected document:",
                temperature=0.2,
                max_tokens=2000,
                frequency_penalty=0.1,
                presence_penalty=1.0,
                stop=["#"]
            )
            if (not newDoc.strip() == ''):
                break
            else:
                print("Correction hasn't produced any code: (" + str(i) + "\\10)...")

        with open(savePath, 'w') as file2:
            file2.write(newDoc.replace("#",""))

def fixPythonCode(filename,savePath):
    print("Correcting code for:",filename+"...")
    if not filename.endswith(".py"):
        return
    with open(filename, 'r') as file:
        lines = file.read().replace("\r", "\n")

        newDoc = ''
        for i in range(0, 10):
            newDoc = completeDavinci(
                prompt=correctionPrompt + lines + "\n\n#Fixed code:",
                temperature=0.2,
                max_tokens=3000,
                frequency_penalty=0.1,
                presence_penalty=1.0,
                stop=["#Fix this python code:"]
            )
            if (not newDoc.strip() == ''):
                break
            else:
                print("Correction hasn't produced any code: (" + str(i) + "\\10)...")

        with open(savePath, 'w') as file2:
            file2.write(newDoc)