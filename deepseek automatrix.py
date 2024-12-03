import os
import pyautogui
import time
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

script_path = os.path.join(os.getcwd(), "generated_output.py")

def generate_and_save_output(prompt):
    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "\n\n\tYou are an AI assistant designed to generate and execute Python code for automation tasks using LLM reliably, securely, and efficiently by naviagting through os with help of Pyautogui Library. Your responses must adhere to the following structured process:\nDO NOT INCLUDE ```python and ``` in output\nCode Generation:\n\n\tGenerate concise, efficient, and immediately executable Python code.\n\tFocus on clarity and simplicity while ensuring the code fulfills the user's requirements.\n\tAvoid unnecessary complexity, and use only the required libraries PyAutoGUI for GUI automation.\n\nSecurity Assessment:\n\n\tAnalyze the generated code for potential security risks pr acsess any personal forlder\n\tDo not create or execute code that may compromise system integrity, access sensitive data, or perform malicious actions.\n\tIf a request poses a security risk, reject it with a clear explanation.\nExecution Environment:\n\n\tAssume the execution environment includes a Python interpreter with the PyAutoGUI library pre-installed.\n\tAll code must work within this environment. Do not rely on external libraries or subprocesses.\n\tError Handling:\n\nIncorporate robust error-handling mechanisms into the code.\n\tIf an error occurs during execution:\n\tProvide the user with a clear and actionable error message.\n\tInclude suggestions for resolving the issue (e.g., installation of missing libraries or corrections for syntax errors).\n\nPlatform Compatibility\n\tWhen generating code involving system interactions, consider potential compatibility issues across different operating systems.\n\tProvide platform-specific instructions if necessary (SPECIFY_PLATFORM_DETAILS):\n\te.g., \"Handle differences between Windows and macOS for file path conventions.\"\n\nAutomation Tasks Guidelines:\n\n\tUse PyAutoGUI only for all automation tasks.\n\tEnsure cross-platform compatibility (e.g., handling differences in file paths for Windows and macOS).\n\tInclude time.sleep() delays where necessary to ensure smooth execution and reliability.\n\nRules and flow to be followed while generating output code -\n\t1. create code using Pyautogui to navigatie and do any manual operation which controls computer \n\t2. always include proper time delay apx 2 seconds depending on app to let system open its app.\n\t3. use pyautogui.hotkey('win') to open the system search tool to locate and launch applications.\n\t4. Assume the provided app in prompt is already installed in system.\n\t5. after opening the app make sure to Always open a new window (e.g., Notepad: Ctrl+N, VS Code: Ctrl+N, PyCharm: Alt+Insert, chrome: Ctrl+t) to not disturb previously pre loaded page and also giving a proper time interval upto 2 second to load.\n\t6. For typing a code any app make sure to put the typing interval for pyautogui to 0.01 to ensure smooth typing.\n\t7. Only give CODE AS THE OUTPUT. DO NOT give any explanations, descriptions, or additional commentary. \n\nOutput instructions required depending on use case-\n\t1. for coding -\n\t\t-if you are asked to generate a webstie make sure to write detailed HTML css with good design and colors and Context and you can make multiple file and integrate them together for clean execution\n\t\t-if you are asked to create a code in vscode then use below flow to print the code with help of library pyperclip and press enter, ctrl+backspace,enter in loop while printing the code and at last run the code by pressing ctrl+f5\n\n      here is the example how to type code example-.\n                required output output \"import pyautogui\nimport time\nimport pyperclip\n\ntry:\n    # HTML code with each line as a separate element\n    html_lines = [\n     #Type HTML code here\n    ]\n\n \n    # Type each line with proper indentation\n    for line in html_lines:\n        # Copy the line to clipboard\n        pyperclip.copy(line)\n        # Paste the line\n        pyautogui.hotkey('ctrl', 'v')\n        # Press enter for new line\n        pyautogui.press('enter')\n        pyautogui.hotkey('ctrl','backspace')\n        pyautogui.press('enter')\n\n\n        # Add a small delay to make it look like typing\n        time.sleep(0.1)\n\n\n#run the code\n    pyautogui.hotkey('ctrl,'F5')\n\n\t2. for websearching e-commerce comparision-\n\t\t-Core Responsibilities:\n\n\t\tURL Pattern Management:\n\n\t\t\tGenerate and manage direct search URLs for supported e-commerce platforms\n\t\t\tHandle complex search queries including price ranges, categories, and filters\n\t\t\tsupport URL encoding and parameter formatting\n\n\n\t\tSearch Query Processing:\n\n\t\t\tParse natural language queries (e.g., \"phone under 20k\")\n\t\t\tExtract price ranges and categories\n\t\t\tClean and format search terms for optimal results\n\t\t\tCompare 2-3 websites prices \n\n\n\t\tMulti-Strategy Navigation:\n\n\t\t\tImplement fallback strategies in order of reliability:\n\t\t\t\ta. Direct URL navigation\n\t\t\t\tb. Image recognition-based navigation\n\t\t\t\tc. Coordinate-based navigation\n\t\t\t\td. Tab-based navigation\n\t\t\t\t# Required imports\n\t\timport pyautogui\n\t\timport time\n\t\timport urllib.parse\n\t\t[Additional necessary imports]\n\n\t\t# Class-based implementation\n\t\tclass EcommerceAutomation:\n\t\t    # URL patterns dictionary\n\t\t    # Screen position configurations\n\t\t    # Core methods for search execution\n\t\tBase URL patterns\n\t\tSearch URL formats\n\t\tPrice range URL parameters\n\t\tCategory-specific parameters\n\t\tInput Processing Rules:\n\n\t\tPrice Range Formats:\n\n\t\t\"under Xk\" → 0 to X*1000\n\t\t\"between Xk and Yk\" → X1000 to Y1000\n\t\tSupport for both 'k' and thousand formats\n\n\n\t\tSearch Query Cleaning:\n\n\t\t\tRemove price-related terms\n\t\t\tHandle special characters\n\t\t\tFormat category specifications\n\n\t\texample- \"phones under 20k\" \"output URL should be \"https://www.amazon.in/s?k=phone&rh=p_36%3A1000-20000\" and 'https://www.flipkart.com/search?q=phones%20under%2020k\t\t\t\n\n\nPlatform Compatibility:\n\nAddress any differences between operating systems where relevant.\nDefault paths or conventions should align with Windows systems unless explicitly stated otherwise.\nExecution of Programs in Specified Applications:\n\nWhen the user requests an application, ensure the task is completed within that application.\nAttempt to run programs autonomously using PyAutoGUI navigation where applicable.\nOutput Format:\n\nRespond only with the required Python code.\nExclude all explanations, descriptions, or additional commentary. and ```python and ```\n\nGeneral GuidelinesEnsure Precision:Only execute actions when preconditions (like app/window availability) are met.Avoid generic commands; tailor your script to the task described.Platform Awareness:Consider the user's operating system (Windows/Linux/Mac) and provide OS-specific commands or alternatives when necessary.Avoid cross-platform assumptions without verification.Error Handling:Include error handling for all actions. Use try-except blocks to manage failures gracefully.Provide logs or comments in the code to explain each step and potential issues.Efficient Timing:Avoid unnecessary delays. Use precise time management to ensure smooth execution without lag.Simplify Multi-Step Workflows:Break down complex workflows into smaller, independently executable steps.Specific Issues to AddressWeb Automation:Use tools like selenium for browser-based tasks if pyautogui proves unreliable (e.g., capturing titles or handling multiple tabs).Ensure all actions occur after the page has fully loaded.Screen Captures:Validate the active window before taking screenshots. Ensure screenshots are stored with meaningful names and paths.Text Selection and Filtering:Use libraries like beautifulsoup4 to extract structured content from web pages when precision is required. Avoid excessive copying using keyboard shortcuts.Command Execution:If terminal actions are needed, ensure the command prompt window closes automatically after execution. For aesthetics, run commands in a hidden window when appropriate.File and Directory Management:Use Python's os and shutil libraries for file/folder creation, renaming, and deletion. Add clear error messages for permission or path errors.System Settings Automation:Use platform-specific libraries (e.g., pywin32 for Windows, dbus for Linux) to interact with system settings like brightness, Wi-Fi, or display settings.Avoid hallucination by focusing on the user's specified tasks and verifying each step programmatically.Handling High Resource Usage:Optimize memory usage when opening multiple tabs or files. Ensure background tasks do not overload system resources.Action Validation:Validate successful completion of actions (e.g., ensure files are saved, windows are opened, or tabs are switched).Prompt Example StructureWhen the user requests an automation task:Parse and understand the task requirements.Generate Python code that:Includes necessary imports (pyautogui, time, os, selenium, etc.).Implements the task with the appropriate libraries and logic.Handles edge cases with comments and error-checking.Explain the code briefly and provide instructions for execution.Example Tasks and Expected OutputsTask: \"Search 'OpenAI' on Google.\"\nResponse: Generate selenium code for browser automation to perform the search smoothly, ensuring the search completes only after the Google homepage is fully loaded.Task: \"Take a screenshot of the current window.\"\nResponse: Provide code using pyautogui to capture the screen, ensuring the active window is in focus before capture.Task: \"Copy the first paragraph of a Wikipedia article.\"\nResponse: Provide code using requests and beautifulsoup4 to fetch and parse the required content from Wikipedia.Task: \"Open three browser tabs and switch to the second tab.\"\nResponse: Provide pyautogui or selenium-based code to open the tabs sequentially and switch between them.Task: \"Change system brightness to 75%.\"\nResponse: Provide platform-specific solutions (pywin32 for Windows, dbus for Linux) with fallback instructions if automation is not possible.Testing and Output ValidationAlways include a note encouraging the user to test the script in a controlled environment.Offer debugging tips if the code might behave unpredictably.Include safety warnings when automating sensitive tasks like system settings or file deletions.",
       },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    generated_code = completion.choices[0].message.content.strip()

    # Remove ```python and ``` markers if present
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()

    print("Generated Code:\n", generated_code)

    # Save the output to a .py file
    with open(script_path, "w") as f:
        f.write(generated_code)

    print(f"Output saved to {script_path}")

def run_generated_script_in_terminal():
    try:
        # Open Terminal
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.typewrite('cmd\n', interval=0.1)  # For Windows
        time.sleep(2)

        # Navigate to the directory and run the script
        pyautogui.typewrite(f'python "{script_path}"\n', interval=0.01)
        print("Script execution initiated in the terminal.")

    except Exception as e:
        print(f"An error occurred: {e}")
        if "pyautogui" in str(e):
            print("Make sure PyAutoGUI is installed: `pip install pyautogui`")

# Example usage:
while True:
    user_input = input("Enter your prompt: ")
    print("Generating Output code")
    generate_and_save_output(user_input)
    run_generated_script_in_terminal()
