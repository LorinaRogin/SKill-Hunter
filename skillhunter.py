import os , requests, re , json
apiKey = "f5c0643e-35ee-4ec1-953d-6d3757e5bc11"
def apiFunction(usersInputObj):
    inputsArray = [{"id": "{input_1}", "label": "Enter your domain", "type": "text"}]
    prompt = "Find free online course certifications and suggest ideas and tips to learn for the domain {input_1}"
    filesData, textData = {}, {}
    for inputObj in inputsArray:
        inputId = inputObj['id']
        if inputObj['type'] == 'text':
            prompt = prompt.replace(inputId, usersInputObj[inputId])
        elif inputObj['type'] == 'file':
            path = usersInputObj[inputId]
            file_name = os.path.basename(path)
            f = open(path, 'rb')
            filesData[inputId] = f

    textData['details'] = json.dumps({'appname': 'skill hunter','prompt': prompt,'documentId': 'no-embd-type','appId' : '66c97db564d827b744a2a1a7' , 'memoryId' : '','apiKey': apiKey})
    response = requests.post('https://apiappstore.guvi.ai/api/output', data=textData, files=filesData)
    output = response.json()
    return output['output']
usersInputObj = {'{input_1}' : input("Enter your domain "),}
output = apiFunction(usersInputObj)
url_regex = r'http://localhost:7000/'
replaced_string = re.sub(url_regex,'https://apiappstore.guvi.ai/' , output)
print(replaced_string)