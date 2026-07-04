#Basic script for parsing JSON and identifying basic errors
#imports
import json, re

try:
    jsInput  = input("Enter/Paste Raw JSON: ") #Retreieves User Input (returned JSON)
    jsInput = jsInput.replace("'", '"') #Unifies all quotation marks
    jsInput = re.sub(r",(\s*[}\]])", r"\1", jsInput) #Regex for trailing commas (removes/cleans)
    try:
        jsObject = json.loads(jsInput) #Loads JSON
        print("\nFormatted JSON: \n")
        print(json.dumps(jsObject, indent=4, ensure_ascii=False)) #Displays formatted JSON

    except json.JSONDecodeError as e: #On Error (JSON parsing-related)
        print(f"\n{e}")

        #Prints the code for parsing error and idenifies location with caret character
        start = max(0, e.pos - 50)
        end = min(len(jsInput), e.pos + 50)

        print("\nJSON Error: ")
        print(jsInput[start:end])
        print(" " * (e.pos - start) + "^")

except e: #Catch All for any other error
    print(e)