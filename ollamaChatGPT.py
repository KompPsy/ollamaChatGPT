
import datetime
from ollama import Client
from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

ipAddress="192.168.0.14"
port="11434"
apiAddress="api.correlatetechnologies.com"

weburl="https://"+apiAddress+"/"
localurl="http://"+ipAddress+":"+port
host=localurl
#host=weburl
boolState=True

print(" List of Model to Use:")
print("------------------------")
print("\n 1.) aya \n 2.) phi3:14b \n 3.) codeqwen \n 4.) llama3 \n 5.) llava-llama \n 6.) codestral \n")
print("------------------------")

while boolState == True:
    modelOptions=input("\n Select a number a LLM model: \n")

    match modelOptions:
        case "1":
            model="aya"
            boolState=False

        case "2":
            model="phi3:14b"
            boolState=False

        case "3":
            model="codeqwen"
            boolState=False
    
        case "4":
            model="llama3"
            boolState=False

        case "5":
            model="llava-llama"
            boolState=False
        case "6":
            model="codestral"
            boolState=False
        case _:
            print("Invalid Answer")
            boolState=True

clear()

while True:
    #print("--------------------------------------------")
    prompt = input("\n Enter something (type 'exit' or 'quit' to quit): \n")
    if prompt.lower() == "exit" or prompt.lower() == "quit":
        print(f"You entered: {prompt}")
        break
    
    client = Client(host)
    
    stream = client.chat(
      model,
      messages=[{'role': 'user', 'content': prompt}],
      stream=True
    )
    now = datetime.datetime.now()
    print("\n", model.upper(),"Chat Assistant", "(", now.strftime("%Y-%m-%d %H:%M:%S"),") :" )
   # print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")
    for chunk in stream:
      print(chunk['message']['content'], end='', flush=True)
