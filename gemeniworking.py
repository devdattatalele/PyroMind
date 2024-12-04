import os
import google.generativeai as genai
import pyautogui
import time
import os

# Path to the saved script
script_path = os.path.join(os.getcwd(), "generated_output.py")
genai.configure(api_key="AIzaSyA3-uNY4klQmZ-AJi3eG3kk-zuX2AbrZoU")

# Create the model
generation_config = {
  "temperature": 1.55,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
    system_instruction="System Prompt:\n\n\tYou are an AI assistant designed to generate and execute Python code for automation tasks using LLM reliably, securely, and efficiently by naviagting through os with help of Pyautogui Library. Your responses must adhere to the following structured process:\n\nCode Generation:\n\n\tGenerate concise, efficient, and immediately executable Python code.\n\tFocus on clarity and simplicity while ensuring the code fulfills the user's requirements.\n\tAvoid unnecessary complexity, and use only the required libraries PyAutoGUI for GUI automation.\n\nSecurity Assessment:\n\n\tAnalyze the generated code for potential security risks pr acsess any personal forlder\n\tDo not create or execute code that may compromise system integrity, access sensitive data, or perform malicious actions.\n\tIf a request poses a security risk, reject it with a clear explanation.\nExecution Environment:\n\n\tAssume the execution environment includes a Python interpreter with the PyAutoGUI library pre-installed.\n\tAll code must work within this environment. Do not rely on external libraries or subprocesses.\n\tError Handling:\n\nIncorporate robust error-handling mechanisms into the code.\n\tIf an error occurs during execution:\n\tProvide the user with a clear and actionable error message.\n\tInclude suggestions for resolving the issue (e.g., installation of missing libraries or corrections for syntax errors).\n\nPlatform Compatibility\n\tWhen generating code involving system interactions, consider potential compatibility issues across different operating systems.\n\tProvide platform-specific instructions if necessary (SPECIFY_PLATFORM_DETAILS):\n\te.g., \"Handle differences between Windows and macOS for file path conventions.\"\n\nAutomation Tasks Guidelines:\n\n\tUse PyAutoGUI only for all automation tasks.\n\tEnsure cross-platform compatibility (e.g., handling differences in file paths for Windows and macOS).\n\tInclude time.sleep() delays where necessary to ensure smooth execution and reliability.\n\nRules and flow to be followed while generating output code -\n\t1. create code using Pyautogui to navigatie and do any manual operation which controls computer \n\t2. always include proper time delay apx 2 seconds depending on app to let system open its app.\n\t3. use pyautogui.hotkey('win') to open the system search tool to locate and launch applications.\n\t4. Assume the provided app in prompt is already installed in system.\n\t5. after opening the app make sure to Always open a new window (e.g., Notepad: Ctrl+N, VS Code: Ctrl+N, PyCharm: Alt+Insert, chrome: Ctrl+t) to not disturb previously pre loaded page and also giving a proper time interval upto 2 second to load.\n\t6. For typing a code any app make sure to put the typing interval for pyautogui to 0.01 to ensure smooth typing.\n\t7. Only give CODE AS THE OUTPUT. DO NOT give any explanations, descriptions, or additional commentary. \n       8. do not depend and use locate on screen use tab to navigate\nOutput instructions required depending on use case-\n\t1. for coding -\n\t\t-if you are asked to generate a webstie make sure to write detailed HTML css with good design and colors and Context and you can make multiple file and integrate them together for clean execution\n\t\t-if you are asked to create a code in vscode then use below flow to print the code with help of library pyperclip and press enter, ctrl+backspace,enter in loop while printing the code and at last run the code by pressing ctrl+f5\n\n      here is the example how to type code example-.\n                required output output \"import pyautogui\nimport time\nimport pyperclip\n\ntry:\n    # HTML code with each line as a separate element\n    html_lines = [\n     #Type HTML code here\n    ]\n\n \n    # Type each line with proper indentation\n    for line in html_lines:\n        # Copy the line to clipboard\n        pyperclip.copy(line)\n        # Paste the line\n        pyautogui.hotkey('ctrl', 'v')\n        # Press enter for new line\n        pyautogui.press('enter')\n        pyautogui.hotkey('ctrl','backspace')\n        pyautogui.press('enter')\n\n\n        # Add a small delay to make it look like typing\n        time.sleep(0.1)\n\n\n#run the code\n    pyautogui.hotkey('ctrl,'F5')\n\n\t2. for websearching e-commerce comparision-\n\t\t-Core Responsibilities:\n\n\t\tURL Pattern Management:\n\n\t\t\tGenerate and manage direct search URLs for supported e-commerce platforms\n\t\t\tHandle complex search queries including price ranges, categories, and filters\n\t\t\tsupport URL encoding and parameter formatting\n\n\n\t\tSearch Query Processing:\n\n\t\t\tParse natural language queries (e.g., \"phone under 20k\")\n\t\t\tExtract price ranges and categories\n\t\t\tClean and format search terms for optimal results\n\t\t\tCompare 2-3 websites prices \n\n\n\t\tMulti-Strategy Navigation:\n\n\t\t\tImplement fallback strategies in order of reliability:\n\t\t\t\ta. Direct URL navigation\n\t\t\t\tb. Image recognition-based navigation\n\t\t\t\tc. Coordinate-based navigation\n\t\t\t\td. Tab-based navigation\n\t\t\t\t# Required imports\n\t\timport pyautogui\n\t\timport time\n\t\timport urllib.parse\n\t\t[Additional necessary imports]\n\n\t\t# Class-based implementation\n\t\tclass EcommerceAutomation:\n\t\t    # URL patterns dictionary\n\t\t    # Screen position configurations\n\t\t    # Core methods for search execution\n\t\tBase URL patterns\n\t\tSearch URL formats\n\t\tPrice range URL parameters\n\t\tCategory-specific parameters\n\t\tInput Processing Rules:\n\n\t\tPrice Range Formats:\n\n\t\t\"under Xk\" → 0 to X*1000\n\t\t\"between Xk and Yk\" → X1000 to Y1000\n\t\tSupport for both 'k' and thousand formats\n\n\n\t\tSearch Query Cleaning:\n\n\t\t\tRemove price-related terms\n\t\t\tHandle special characters\n\t\t\tFormat category specifications\n\n\t\texample- \"phones under 20k\" \"output URL should be \"https://www.amazon.in/s?k=phone&rh=p_36%3A1000-20000\" and 'https://www.flipkart.com/search?q=phones%20under%2020k\t\t\t\n\n\nPlatform Compatibility:\n\nAddress any differences between operating systems where relevant.\nDefault paths or conventions should align with Windows systems unless explicitly stated otherwise.\nExecution of Programs in Specified Applications:\n\nWhen the user requests an application, ensure the task is completed within that application.\nAttempt to run programs autonomously using PyAutoGUI navigation where applicable.\nOutput Format:\n\nRespond only with the required Python code.\nExclude all explanations, descriptions, or additional commentary.",
)
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "open notepad and write a code for additionn of two numbers",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)    \n    pyautogui.typewrite('notepad\\n', interval=0.1)\n    time.sleep(1)\n    pyautogui.hotkey('ctrl','n')\n    time.sleep(1)    \n    pyautogui.typewrite('num1 = int(input(\"Enter first number: \"))\\n', interval=0.1)\n    pyautogui.typewrite('num2 = int(input(\"Enter second number: \"))\\n', interval=0.05)\n    pyautogui.typewrite('sum = num1 + num2\\n', interval=0.05)\n    pyautogui.typewrite('print(\"The sum is:\", sum)\\n', interval=0.05)\n    print(\"Successfully typed the addition code in Notepad.\")\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n    if \"pyautogui\" in str(e):\n        print(\"Make sure PyAutoGUI is installed: `pip install pyautogui`\")\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "write a code to open a camera using python using opencv on notepad\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.typewrite('notepad\\n', interval=0.1)  \n    time.sleep(1)  \n    pyautogui.hotkey('ctrl', 'n') \n    time.sleep(1)\n    pyautogui.typewrite('import cv2\\n', interval=0.05)\n    pyautogui.typewrite('cap = cv2.VideoCapture(0)  # 0 represents the default camera\\n', interval=0.05)\n    pyautogui.typewrite('if not cap.isOpened():\\n', interval=0.05)\n    pyautogui.typewrite('    raise IOError(\"Cannot open webcam\")\\n', interval=0.05)\n    pyautogui.typewrite('while(True):\\n', interval=0.05)\n    pyautogui.typewrite('    ret, frame = cap.read()\\n', interval=0.05)    \n    pyautogui.typewrite('    cv2.imshow(\"Webcam Feed\", frame)\\n', interval=0.05)\n    pyautogui.typewrite('    if cv2.waitKey(1) & 0xFF == ord(\"q\"): # Press 'q' to exit\\n', interval=0.05)\n    pyautogui.typewrite('        break\\n', interval=0.05)\n    pyautogui.typewrite('cap.release()\\n', interval=0.05)\n    pyautogui.typewrite('cv2.destroyAllWindows()\\n', interval=0.05)\n\n    print(\"Successfully typed the webcam code in Notepad.\")\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n    if \"pyautogui\" in str(e):\n        print(\"Make sure PyAutoGUI is installed: `pip install pyautogui`\")\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "create a notepad text  printing all basic algebra formula ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.typewrite('notepad\\n', interval=0.1)\n    time.sleep(1)\n    pyautogui.hotkey('ctrl', 'n') # new notepad window\n    time.sleep(1)\n\n    formulas = [\n        \"Quadratic Formula: x = (-b ± √(b² - 4ac)) / 2a\",\n        \"Slope-Intercept Form: y = mx + b\",\n        \"Distance Formula: d = √((x₂ - x₁)² + (y₂ - y₁)²)\",\n        \"Midpoint Formula: M = ((x₁ + x₂) / 2, (y₁ + y₂) / 2)\",\n        \"Pythagorean Theorem: a² + b² = c²\",\n        \"Area of a Triangle : A = base*height/2\",\n\n        \n    ]\n\n    for formula in formulas:\n        pyautogui.typewrite(formula + '\\n', interval=0.05)\n\n    print(\"Successfully typed basic algebra formulas in Notepad.\")\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n    if \"pyautogui\" in str(e):\n        print(\"Make sure PyAutoGUI is installed: `pip install pyautogui`\")\n\n```\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "create a HTML basic code for my portfolio website using following information on vscode and try to run the script to provide output\nName devdatta talele contact number 1234567890 taleledevatta@gmail.com Vidyalankar intusitute of technology ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.typewrite('vscode\\n', interval=0.1)  # Open VS Code\n    time.sleep(2)  #adjust delay as needed, vs code takes time to open\n    pyautogui.hotkey('ctrl', 'n')  # New file in VS Code\n    time.sleep(1)\n\n\n\n    html_code = \"\"\"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Devdatta Talele - Portfolio</title>\n</head>\n<body>\n    <h1>Devdatta Talele</h1>\n    <p>Contact: 1234567890</p>\n    <p>Email: taleledevatta@gmail.com</p>\n    <p>Institute: Vidyalankar Institute of Technology</p>\n\n\n</body>\n</html>\"\"\"\n\n\n\n    pyautogui.typewrite(html_code, interval=0.01)\n    time.sleep(1)\n    pyautogui.hotkey('ctrl', 's') #save\n    time.sleep(1)\n\n    pyautogui.typewrite('index.html', interval = 0.1)\n    pyautogui.press('enter')\n\n    #can't directly see output due to limitations of pyautogui opening programs\n\n    time.sleep(2)\n\n\n\n    print(\n        \"HTML code for the portfolio website has been written to a file named 'index.html' in VS Code. Open the file in a web browser to view it.\")\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n    if \"pyautogui\" in str(e):\n        print(\"Make sure PyAutoGUI is installed: `pip install pyautogui`\")\n```\n\n\n\nThis script will create an `index.html` file in your VS Code and put the HTML code in it. You'll have to manually open this file in your browser to view the output. This is because simulating clicks in pyautogui for something like \"Open in Browser\" can be tricky to do in a consistent way for different browsers. If using VS code \"live preview\", right click the html file in explorer tab then 'Open with live server'. It might ask to chose program (ie: chrome, firefox), select perfered browser from there. If that dosent work simply just right click file in file explorer again and this time 'Copy path'  then paste and enter that path directly in your prefered browser's address bar manually after executing program. If there is no webserver module or liveserver extension for vscode. I recommend you install it if necessary before running. \n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "create a code to perform addition of two numbers in pycharm",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.typewrite('pycharm\\n', interval=0.1)\n    time.sleep(5)   #increased time for loading up pycharm may need more time\n    pyautogui.hotkey('alt','insert')#new file\n    time.sleep(1)\n    \n\n    pyautogui.typewrite('num1 = int(input(\"Enter first number: \"))\\n', interval=0.05)\n    pyautogui.typewrite('num2 = int(input(\"Enter second number: \"))\\n', interval=0.05)\n    pyautogui.typewrite('sum_result = num1 + num2\\n', interval=0.05)\n    pyautogui.typewrite('print(\"The sum is:\", sum_result)\\n', interval=0.05)\n\n    pyautogui.hotkey('ctrl', 'shift', 'f10') #run program hotkey pycharm, if dosent work try 'shift+alt+f10' also 'ctrl+f9'\n    #if that did not work use mouse to run\n    time.sleep(1) #might need to adjust, time taken to ask for input varies by condition\n    pyautogui.typewrite('5',interval=0.05)\n    pyautogui.press('enter')\n    time.sleep(0.5)\n    pyautogui.typewrite('15',interval=0.05)\n    pyautogui.press('enter')\n    time.sleep(1)  # adjust delay as needed to give it time to execute\n\n\n    \n    print(\"Code executed in PyCharm (provided it ran correctly).\")\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n    if \"pyautogui\" in str(e):\n        print(\"Make sure PyAutoGUI is installed: `pip install pyautogui`\")\n\n\n\n```\n",
      ],
    },
  ]
)

def generate_and_save_output(prompt):
    # Start the chat session
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [prompt],
            }
        ]
    )

    # Send the prompt and get the response
    response = chat_session.send_message(prompt)
    generated_code = response.text

    # Remove ```python and ``` markers
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()

    # Print the cleaned response
    print("Generated Code:\n", generated_code)

    # Save the output to a .txt file
    with open("generated_output.py", "w") as f:
        f.write(generated_code)

    print("Output saved to generated_output.py")


def run_generated_script_in_terminal():
    try:
        # Open Terminal
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.typewrite('cmd\n', interval=0.1)  # For Windows
        time.sleep(2)

        # Navigate to the directory and run the script
        script_path = os.path.join(os.getcwd(), "generated_output.py")
        pyautogui.typewrite(f'python "{script_path}"\n', interval=0.05)
        print("Script execution initiated in the terminal.")

    except Exception as e:
        print(f"An error occurred: {e}")
        if "pyautogui" in str(e):
            print("Make sure PyAutoGUI is installed: `pip install pyautogui`")
# Example usage:
user_input = input("Enter your prompt: ")
print("Generating Output code")
generate_and_save_output(user_input)
run_generated_script_in_terminal()
