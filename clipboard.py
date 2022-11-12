#! python3
# Clipboard script

import pyperclip # to get access to clipboard
import sys # to get access to terminal arguments

# dictionary of responses with a key of the keyword of the reply and a value with the full reply
responses = {"reply":"thank you for your message, I really appreciate it.",
"hello":"Hello, is it me you're looking for?",
"goodbye":"Goodbye, it's not me you're looking for."
}

if len(sys.argv) < 2:
    print("Usage: python3 clipboard.py [Keyword] - Copy phrase text" )
    sys.exit()

keyword = sys.argv[1] # first entry of sys.agrv is the filename (clipboard.py) which is index 0, so index 1 is where the terminal/command line arguments are stored

if keyword in responses: # checking to see if the keyword is in the responses dictionary
    pyperclip.copy(responses[keyword]) #  if it is use pyperclip to copy the text to clipboard
    print(f"Text for {keyword} copied to the clipboard.") # notify user it is copied to their clipboard
else:
    print(f"There is no text saved for the keyword '{keyword}'. The keywords currently available are: ") 
    for key in responses:
        print(key) # if the keyword is not in the dictionary print what currently is in the dictionary and ask the user if they would like to add this keyword and a response to the dictionary
    add_new = input("Would you like to add a new response for this keyword? y/n: \n")
    if add_new == "y":
        new_value = input(f"Enter the response you would like to save for {keyword}: \n")
        responses[keyword] = new_value # add new user resonse to dictionary
        print(responses) # print new list of responses with new keyword and response
        # currently once programme terminates the newly entered respones will not be saved in the response and only livs while the programme is running, in future add new way of saving this.


 
