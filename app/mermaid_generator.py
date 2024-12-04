# this file is mermaid_generator.py

from groq import Groq
import streamlit as st

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)


# between |  | do not use any " " or ' ' 
# And no brackets to be used also

def mermaid_code(code):
    prompt = f"""
    
    Generate a precise and accurate flowchart of the given code in MERMAID markdown language. 
    the steps of the flowchart should logically correct and should go in flow of the actual execution of the program like main function should be first executed then within it other functions will be called so in this manner the flowchart should go by the flow of the code execution
    
    {code}
    
    Your response should only contain valid mermaid language code,
    whenever text is added to the mermaid box then make sure it goes in Double quotes " " . for example if i want [this is (my text here) abc] to be in a flowchart box then i will write it as  ["this is (my text here) abc"] also the text present like this : |"your text here"| should also be in double quotes all text in each bracket and in each |""| should be in double quotes Strict instructions for this.
    Give the flowchart of the explanation of the code avoid directluy adding the code in the flochart
    STRICT INSTRUCTIONS TO not include any explanations or comments outside of the mermaid code.
    
    ##EXAMPLES##
    
    def binary_search(arr, target):
    left= 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 
    
    below is the mermaid flowchart conversion of the example code:
    
   ```mermaid
    graph TD
        A["Start"] --> B["Initialize left = 0, right = len(arr) - 1"]
        B --> C{"left <= right?"}
        C -->|"Yes"| D["Calculate mid = (left + right) // 2"]
        D --> E{"arr[mid] == target?"}
        E -->|"Yes"| F[Return mid]
        E -->|"No"| G{"arr[mid] < target?"}
        G -->|"Yes (going to right half)"| H["Set left = mid + 1"]
        G -->|"No ((going to left half))"| I["Set right = mid - 1"]
        H --> C
        I --> C
        C -->|"No"| J["Return -1"]
        F --> K["End"]
        J --> K
    ```
    
    After you generate the entire mermaid code read and go through it again at least 10 times to check that:
        1. whenever any character is added to the mermaid box where [] or curly brackets are used for the first time then make sure it goes in Double quotes " " .
        2. everything coming in between | | should be in double quotes " " example |"Hello (abc)"| .
    repeat this process untill all the condition are satisfied.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        # model="llama3-8b-8192",
        model = "llama-3.1-70b-versatile",
    )

    return chat_completion.choices[0].message.content
