import os
import glob
import subprocess
import requests

API_URL = "https://ollama.com/api/chat"
HEADERS = {"Authorization": "Bearer " + os.environ["OLLAMA_API_KEY"]}

read_file_tool_schema = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Use this when the user wants read a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the path of the file to read"},
            },
            "required": ["path"]
        }
    }
}

list_files_schema = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "Use this when the user wants to list files in the current working directory by default, or in a named directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the path of the directory on which to list the files."}
            },
            "required": []
        }
    }
}

write_file_tool_schema = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Use this when the user wants write to a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the path of the file to write to path with filename and extension of the file to write. Only .txt"},
                "content": {"type" : "string", "description": "the path of the file to write"}
           },
            "required": ["path", "content"]
        }
    }
}

run_python_schema = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Use this when the user wants to run a python file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the path of the file to run"},
               
           },
            "required": ["path", "content"]
        }
    }
}
def agent(messages):
    tools = [
        read_file_tool_schema, list_files_schema, write_file_tool_schema #,run_python_schema
    ]

    payload = {
     #  "model":"gpt-oss:120b",
      "model":"deepseek-v4.1-flash",
        "messages": messages,
        "stream": False,
        "tools": tools
    }
    
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload,
        timeout=300,
    )
    response.raise_for_status()
    data = response.json()
    message = data["message"]
    return message

import base64
with open ("calculator/images.jpeg", "rb") as f:
     img_b64 = base64.b64encode(f.read()).decode ("utf-8")
    #img_b64 = base64.b64encode(f.read()).decode("utf-8")
tool_called = True
messages = [
     
{ "role": "user", 
    # "content": "write a python code to print all folders in codespaces"
     #"content": "we have some files in the ediscovery folder begining with the subjeect....write a python programme and group similar subjects together"
    #"content": "write a 3 files in the ediscovery folder using the okafodo file as an inspiration"
     #"content": "write a python code to print all folders in codespaces"
     #"content": "scrape cnn.lite and save 100 articles to scrape.txt file"
     #"content": "write a python code to brief laws cases by structuring it by including an introduction, brief facts, procedural history, reasoning of the court and conclusion"
    #"content": "describe the image",
   # "images":[img_b64]
   "content": "what CCPA privacy laws should a business contract have?"
    
     }
]
while tool_called:
    message = agent(messages)
    print(message)
    tool_called = "tool_calls" in message

    if tool_called:
        print("tool called!")
        tool_calls = message["tool_calls"]
        tool_call = tool_calls[0]

        function_name = tool_call["function"]["name"]
        function_arguments = tool_call["function"]["arguments"]

        if function_name == "list_files":
            path = "."
            if "path" in function_arguments:
                path = function_arguments["path"]
            print(f"arguments for list_files: {path}")
            #files = "\n".join(os.listdir(path))
            files = glob.glob(f"{path}/*")
            output = files

        if function_name == "read_file":
            path = function_arguments["path"]
            with open(path, "r") as file:
                file_content = file.read()
            output = file_content

        if function_name == "write_file":
                    path = function_arguments["path"]
                    content=function_arguments["content"]
                    with open(path, "w") as file:
                        file.write(content)
                    output = f"writent to {path} with content: {content}"

       # if function_name == "run_python_schema":
             #path= function_arguments["path"]
             
        # if function_name == "add2":
        #     arg1 = int(function_arguments["arg1"])
        #     arg2 = int(function_arguments["arg2"])
        #     print(f"function_name: {function_name}")
        #     print(f"arg1: {arg1}")
        #     print(f"arg2: {arg2}")
        #     output = arg1 + arg2
        tool_message = {
            "role": "tool",
            "content": f"The output of tool {function_name} is: {output}"
        }
        messages.append(tool_message)
    else:
        ai_message = {
            "role":  message["role"],
            "content": message["content"]
        }
        messages.append(ai_message)

last_message = messages[-1]
import pprint
printer = pprint.pprint
# printer(last_message)

printer(messages)
