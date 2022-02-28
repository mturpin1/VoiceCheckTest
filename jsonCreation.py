import json
import time

controlText = "This is a string"
inputText = input("Enter the string you want to test:   ")
resultArray = []


if str(inputText) == str(controlText):
    resultArray.append("Positive")
    try:
        with open("Result" + time.strftime("%a%d%b%Y\'%H.%M.%S%p\'" + ".json"), 'w') as f:
            json.dump(resultArray, f, indent=2)

    except:
        print("Error creating file")
else:
    resultArray.append("Negative")
    try:
        with open("Result" + time.strftime("%a%d%b%Y\'%H.%M.%S%p\'" + ".json"), 'w') as f:
            json.dump(resultArray, f, indent=2)
    except:
        print("Error creating file")
