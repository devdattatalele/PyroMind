import os
import google.generativeai as genai
import pyautogui
import time
import os

# Path to the saved script
script_path = os.path.join(os.getcwd(), "generated_output.py")
genai.configure(api_key="AIzaSyDbseveUEArcDGT3LaZ63HWt1Y-1TMluxY")

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 0.05,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="\nYou are an AI assistant designed to generate and execute Python code for automation tasks using LLM reliably, securely, and efficiently by navigating through the operating system with the help of the PyAutoGUI library. Your responses must adhere to the following structured process:\n\n---\n\n#### **Code Generation:**\n\n1. Generate concise, efficient, and immediately executable Python code.  \n2. Focus on clarity and simplicity while ensuring the code fulfills the user's requirements.  \n3. Avoid unnecessary complexity and use only the required PyAutoGUI library for GUI automation.  \n\n---\n\n#### **Security Assessment:**\n\n1. Analyze the generated code for potential security risks or attempts to access personal folders.  \n2. Do not create or execute code that may compromise system integrity, access sensitive data, or perform malicious actions.  \n3. If a request poses a security risk, reject it with a clear explanation.  \n\n---\n\n#### **Execution Environment:**\n\n1. Assume the execution environment includes a Python interpreter with the PyAutoGUI library pre-installed.  \n2. All code must work within this environment. Do not rely on external libraries or subprocesses.  \n\n---\n\n#### **Error Handling:**\n\n1. Incorporate robust error-handling mechanisms into the code.  \n2. If an error occurs during execution:  \n   - Provide the user with a clear and actionable error message.  \n   - Include suggestions for resolving the issue (e.g., installing missing libraries or correcting syntax errors).  \n\n---\n\n#### **Platform Compatibility:**\n\n1. When generating code involving system interactions, consider potential compatibility issues across different operating systems.  \n2. Provide platform-specific instructions if necessary:  \n   - Example: Handle differences between Windows and macOS for file path conventions.  \n\n---\n\n#### **Automation Task Guidelines:**\n\n1. Use **PyAutoGUI** exclusively for all automation tasks.  \n2. Ensure cross-platform compatibility (e.g., handling differences in file paths for Windows and macOS).  \n3. Include `time.sleep()` delays where necessary to ensure smooth execution and reliability.  \n4. **Rules to follow while generating code:**\n   - Use `pyautogui.hotkey('win')` to open the system search tool to locate and launch applications.  \n   - Assume the requested app is already installed on the system.  \n   - Always open a new tab before searching for a website (e.g., `ctrl+t`).  \n   - Always open a new window for apps:  \n     - **Notepad:** `Ctrl+N`  \n     - **VS Code:** `Ctrl+N`  \n     - **PyCharm:** `Alt+Insert`  \n     - **Chrome:** `Ctrl+t`  \n   - Add a 2-second delay after opening an app or a new window to ensure it loads properly.  \n   - For typing tasks, set `pyautogui.typewrite`'s typing interval to `0.01` for smooth typing.  \n   - Never use or guess coordinates for mouse clicks. Instead, use direct query links to navigate:  \n     - Example: To open Gmail's compose email, use: `https://mail.google.com/mail/u/0/#inbox?compose=new`.  \n     - For website searches, use structured URLs like: `https://www.example.com/search_url`.  \n   - Wait approximately 10 seconds for heavy websites to load before continuing with further steps.  \n\n---\n\n#### **Output Instructions Based on Use Case:**\n\n1. **For coding tasks:**  \n   - If the task involves generating a website, write detailed HTML, CSS, and JavaScript with good design and context. Use multiple files where necessary for clean execution.  \n   - When asked to write code in **VS Code**, follow this flow:  \n     - Use the `pyperclip` library to copy each line of the code and paste it with `pyautogui.hotkey('ctrl', 'v')`.  \n     - Use `pyautogui.press('enter')` and `ctrl+backspace` for indentation corrections.  \n     - Execute the code by pressing `Ctrl+F5`.  \n   - Example for typing code:  \n     ```plaintext\n     import pyautogui\n     import time\n     import pyperclip\n\n     try:\n         html_lines = [\n             # Add HTML code lines here\n         ]\n\n          for line in html_lines:\n        # Copy the line to clipboard\n        pyperclip.copy(line)\n        # Paste the line\n        pyautogui.hotkey('ctrl', 'v')\n        # Press enter for new line\n        pyautogui.press('enter')\n        pyautogui.hotkey('ctrl','backspace')\n        pyautogui.press('enter')\n\n         \n         pyautogui.hotkey('ctrl', 'f5')\n\n     except Exception as e:\n         print(\"Error:\", e)\n     ```\n\n2. **For web searching (e.g., e-commerce comparisons):**  \n   - Core Responsibilities:  \n     - Generate and manage direct search URLs for platforms like Amazon and Flipkart.  \n     - Parse natural language queries such as \"phones under 20k.\"  \n     - Extract price ranges, clean and format search terms, and compare prices on 2-3 platforms.  \n   - Example of URL parsing:  \n     - Input: `\"phones under 20k\"`  \n     - Output URLs:  \n       - `https://www.amazon.in/s?k=phones&rh=p_36%3A1000-20000`  \n       - `https://www.flipkart.com/search?q=phones%20under%2020k`.  \n\n---\n\n#### **General Rules for Responses:**\n\n1. Respond **only** with the required Python code.  \n2. Exclude all explanations, descriptions, or additional commentary.  \n3. Never include Python code fences (e.g., ` ```python `).  \n4. Avoid closing any open tabs or windows unnecessarily.  \n\n--- ",
)
# TODO Make these files available on the local file system
# You may need to update the file paths


chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "create a notepad text  printing all basic algebra formula ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.write('notepad')\n    time.sleep(1)\n    pyautogui.press('enter')\n    time.sleep(2)\n    pyautogui.hotkey('ctrl', 'n')\n    time.sleep(1)\n\n\n    formulas = [\n        \"Quadratic Formula: x = (-b ± √(b² - 4ac)) / 2a\",\n        \"Slope-Intercept Form: y = mx + b\",\n        \"Distance Formula: d = √((x₂ - x₁)² + (y₂ - y₁)²)\",\n        \"Midpoint Formula: M = ((x₁ + x₂) / 2, (y₁ + y₂) / 2)\",\n        \"Pythagorean Theorem: a² + b² = c²\",\n        \"Area of a Triangle: A = (1/2)bh\",\n        \"Area of a Rectangle: A = lw\",\n        \"Area of a Circle: A = πr²\",\n        \"Circumference of a Circle: C = 2πr\",\n        \"Volume of a Cube: V = s³\",\n        \"Volume of a Rectangular Prism: V = lwh\",\n        \"Volume of a Sphere: V = (4/3)πr³\",\n        \"Simple Interest: I = Prt\",\n        \"Compound Interest: A = P(1 + r/n)^(nt)\",\n        \"Slope of a Line: m = (y₂ - y₁) / (x₂ - x₁)\",\n\n\n    ]\n\n    for formula in formulas:\n        pyautogui.write(formula, interval=0.01)\n        pyautogui.press('enter')\n\n\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\n```",
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
        "```python\nimport pyautogui\nimport time\nimport pyperclip\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.write('vscode')\n    time.sleep(1)\n    pyautogui.press('enter')\n    time.sleep(2)\n    pyautogui.hotkey('ctrl', 'n')\n    time.sleep(1)\n\n    html_lines = [\n        '<!DOCTYPE html>',\n        '<html lang=\"en\">',\n        '<head>',\n        '    <meta charset=\"UTF-8\">',\n        '    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">',\n        '    <title>Devdatta Talele Portfolio</title>',\n        '    <style>',\n        '        body {',\n        '            font-family: sans-serif;',\n        '            margin: 0;',\n        '            padding: 0;',\n        '            background-color: #f0f0f0;',\n        '            color: #333;',\n        '        }',\n        '        header {',\n        '            background-color: #333;',\n        '            color: #fff;',\n        '            padding: 20px;',\n        '            text-align: center;',\n        '        }',\n        '        .container {',\n        '            max-width: 800px;',\n        '            margin: 20px auto;',\n        '            padding: 20px;',\n        '            background-color: #fff;',\n        '            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);',\n        '        }',\n        '        h1 {',\n        '            font-size: 2em;',\n        '        }',\n        '        p {',\n        '            line-height: 1.6;',\n        '        }',\n\n        '        .contact-info {',\n        '            margin-top: 20px;',\n        '        }',\n\n        '        .contact-info p {',\n        '            margin-bottom: 10px;',\n        '        }',\n\n\n        '    </style>',\n        '</head>',\n        '<body>',\n        '    <header>',\n        '        <h1>Devdatta Talele</h1>',\n        '        <p>Aspiring Software Engineer</p>',\n        '    </header>',\n        '    <div class=\"container\">',\n        '        <section id=\"about\">',\n        '            <h2>About Me</h2>',\n        '            <p>',\n        '               A passionate and dedicated computer science student pursuing a degree at Vidyalankar Institute of Technology. With a strong foundation in programming languages like Python, Java, and C++, I am eager to contribute my skills and enthusiasm to the world of software development. I thrive on challenges and enjoy collaborating with others to create innovative solutions. My keen interest lies in exploring the realms of Artificial Intelligence, Machine Learning, and Web Development.  ',\n        '            </p>',\n        '        </section>',\n        '       <section class=\"contact-info\">',\n        '            <h2>Contact Information</h2>',\n        '            <p><strong>Email:</strong> taleledevatta@gmail.com</p>',\n        '            <p><strong>Phone:</strong> 1234567890</p>',\n        '        </section>',\n\n        '    </div>',\n        '</body>',\n        '</html>'\n    ]\n\n    for line in html_lines:\n        pyperclip.copy(line)\n        pyautogui.hotkey('ctrl', 'v')\n        pyautogui.press('enter')\n        pyautogui.hotkey('ctrl','backspace')\n        pyautogui.press('enter')\n        time.sleep(0.01)\n\n    pyautogui.hotkey('ctrl', 's')\n    time.sleep(1)\n    pyautogui.write('index.html')\n    time.sleep(0.5)\n    pyautogui.press('enter')\n    time.sleep(2)\n\n\n    pyautogui.hotkey(\"alt\",\"d\")\n    pyautogui.write(r\"file:///C:/Users/acer/OneDrive/Desktop/vs_code_temp/index.html\",interval=0.04)\n\n    pyautogui.press(\"enter\")\n\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\n\n\n```\n\n",
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
    {
      "role": "user",
      "parts": [
        "Compare laptops on different tecomerce websites\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\nimport webbrowser\n\ndef search_amazon(query):\n    base_url = \"https://www.amazon.in/s?k=\"\n    search_url = base_url + query.replace(\" \", \"+\")\n    webbrowser.open(search_url)\n\ndef search_flipkart(query):\n    base_url = \"https://www.flipkart.com/search?q=\"\n    search_url = base_url + query.replace(\" \", \"%20\")  # Encode spaces\n    webbrowser.open(search_url)\n    time.sleep(10)\n\n\ndef search_reliancedigital(query):  \n    base_url = \"https://www.reliancedigital.in/search?q=\"\n    search_url = base_url + query.replace(\" \", \"%20\")  # Encode spaces\n    webbrowser.open(search_url)\n\n\n\n\ntry:\n    product = \"laptops\" \n\n    search_amazon(product)\n    time.sleep(5) # Delay to allow page load (adjust as needed)\n    pyautogui.hotkey(\"ctrl\",\"t\")#open new tab\n    time.sleep(1)\n\n    search_flipkart(product)\n    time.sleep(5)  # Delay\n    pyautogui.hotkey(\"ctrl\",\"t\")#open new tab\n    time.sleep(1)\n\n    search_reliancedigital(product)\n    time.sleep(5) # Delay to allow page load (adjust as needed)\n\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Find phone under 20k on internet",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\nimport webbrowser\n\ndef search_amazon(query):\n    base_url = \"https://www.amazon.in/s?k=\"\n    search_url = base_url + query.replace(\" \", \"+\")  # Correct space encoding\n    webbrowser.open(search_url)\n\ndef search_flipkart(query):\n    base_url = \"https://www.flipkart.com/search?q=\"\n    search_url = base_url + query.replace(\" \", \"%20\")\n    webbrowser.open(search_url)\n\n\n\ntry:\n    product = \"phones under 20000\"  # Keep the original query\n    \n\n    search_amazon(product)\n    time.sleep(10) # Delay\n    pyautogui.hotkey(\"ctrl\",\"t\")#open new tab\n    time.sleep(1)\n    search_flipkart(product)\n    time.sleep(10) # Delay\n\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Write email to principal that i sick",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport pyautogui\nimport time\nimport pyperclip\n\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.write('chrome')\n    time.sleep(1)\n    pyautogui.press('enter')\n    time.sleep(3)  # Wait for Chrome to fully open\n\n    pyautogui.hotkey('ctrl', 't')\n    time.sleep(1)\n\n\n\n    pyautogui.write('https://mail.google.com/mail/u/0/#inbox?compose=new', interval=0.03)\n    pyautogui.press('enter')\n\n    time.sleep(5)\n\n    pyperclip.copy('principal@example.com')\n    pyautogui.hotkey('ctrl', 'v')  # Or pyautogui.typewrite(recipient_email) if you prefer typing\n    pyautogui.press('tab')       # Move to subject line\n\n    time.sleep(1)                # Brief pause before typing the subject\n    pyautogui.write('Absence Due to Illness', interval=0.02)\n    pyautogui.press('tab')       # Move to email body\n\n    time.sleep(1)\n    email_body = f\"\"\"Subject: Absence Due to Illness\n\n\nDear Principal [Principal's Last Name],\n\nI am writing to inform you of my absence from school today, [Date], due to illness. I woke up this morning feeling unwell and do not want to risk spreading any potential illness.\n\nI will check my school email regularly for any assignments or announcements. I apologize for any inconvenience this may cause and expect to return to school tomorrow if I am feeling better.\n\n\nSincerely,\n[Your Name]\n[Your Class/Grade]\"\"\"\n\n\n    pyperclip.copy(email_body)\n    pyautogui.hotkey('ctrl', 'v')  \n    time.sleep(2) \n    pyautogui.hotkey('ctrl', 'enter')  # Send\n\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\n```\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "find petrol pump near me",
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
        pyautogui.typewrite(f'python "{script_path}"\n', interval=0.01)
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
