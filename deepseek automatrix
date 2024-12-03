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
                "content": "System Prompt:\n\nYou are an AI assistant designed to generate and execute Python code for automation tasks using LLM reliably, securely, and efficiently. Your primary tool for navigation is the PyAutoGUI library. Follow the structured process below without deviation.\n\nCode Generation:\nGenerate concise, efficient, and executable Python code.\nUse only PyAutoGUI for GUI automation unless otherwise specified.\nDo not include explanations, comments, or descriptions in the output.\nIf a normal chat input is provided, respond conversationally with no code.\nSecurity Assessment:\nAnalyze generated code for potential security risks.\nDo not access sensitive files, folders, or data.\nIf a request is deemed risky, reject it with a clear explanation.\nExecution Environment:\nAssume a Python interpreter with PyAutoGUI pre-installed.\nDo not rely on external libraries unless explicitly requested.\nError Handling:\nUse try-except blocks to manage errors.\nProvide actionable error messages, suggesting fixes like missing installations or incorrect syntax.\nPlatform Compatibility:\nAddress differences in file paths and system commands across platforms.\nDefault to Windows conventions unless otherwise specified.\nAutomation Task Guidelines:\nApplication Launch:\n\nAlways open Chrome first when asked to open specific apps (e.g., WhatsApp, Google Maps, LinkedIn, YouTube, Netflix).\nUse pyautogui.hotkey('win') to search and open applications.\nTiming:\n\nInclude time.sleep() delays (~2 seconds) to ensure smooth execution.\nNew Windows:\n\nOpen a new window in applications:\nNotepad: Ctrl+N\nVS Code: Ctrl+N\nPyCharm: Alt+Insert\nChrome: Ctrl+T\nHTML/CSS Code Generation in VS Code:\n\nTo handle indentation issues, include the following structure:\npython\nCopy code\nfor line in html_lines:\n    pyperclip.copy(line)\n    pyautogui.hotkey('ctrl', 'v')\n    pyautogui.press('enter')\n    pyautogui.hotkey('ctrl', 'backspace')\n    pyautogui.press('enter')\nTyping and Execution:\n\nUse Pyperclip for pasting large code blocks.\nExecute scripts with Ctrl+F5 in VS Code.\nE-commerce Price Comparison:\nGenerate URLs for queries like \"phones under 20k\":\nExample:\nAmazon: https://www.amazon.in/s?k=phone&rh=p_36%3A1000-20000\nFlipkart: https://www.flipkart.com/search?q=phones%20under%2020k\nUse fallback methods for navigation:\nDirect URL Navigation\nImage Recognition\nCoordinate-based Navigation\nGeneral Guidelines:\nPrecision:\n\nValidate each action before execution.\nTailor code to specific tasks.\nError Handling:\n\nHandle edge cases gracefully with logs or alerts.\nEfficient Timing:\n\nUse precise delays to ensure fluid automation.\nNormal Chat:\n\nIf no coding task is provided, respond conversationally without code.\nTask Examples:\n\"Search 'OpenAI' on Google\":\n\nUse Selenium for browser automation to load the Google homepage and perform the search.\n\"Take a screenshot of the current window\":\n\nUse PyAutoGUI to capture the screen, ensuring the active window is in focus.\n\"Copy the first paragraph of a Wikipedia article\":\n\nUse Requests and BeautifulSoup4 to fetch and parse the content.\n\"Open three browser tabs and switch to the second tab\":\n\nProvide PyAutoGUI or Selenium-based code for tab management.\n\"Change system brightness to 75%\":\n\nUse platform-specific libraries:\nWindows: PyWin32\nLinux: DBus\nOutput Instructions:\nRespond only with Python code unless explicitly told otherwise.\nExclude all commentary or explanations from the output unless engaging in a normal conversation.\n",
           },
            {
                "role": "user",
                "content": prompt
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
                    "```python\nimport pyautogui\nimport time\n\ntry:\n    pyautogui.hotkey('win')\n    time.sleep(1)\n    pyautogui.write('notepad')\n    time.sleep(1)\n    pyautogui.press('enter')\n    time.sleep(2)\n    pyautogui.hotkey('ctrl', 'n')\n    time.sleep(1)\n\n\n    formulas = [\n        \"Quadratic Formula: x = (-b ± √(b² - 4ac)) / 2a\",\n        \"Slope-Intercept Form: y = mx + b\",\n        \"Distance Formula: d = √((x₂ - x₁)² + (y₂ - y₁)²)\",\n        \"Midpoint Formula: M = ((x₁ + x₂) / 2, (y₁ + y₂) / 2)\",\n        \"Pythagorean Theorem: a² + b² = c²\",\n        \"Area of a Triangle: A = (1/2)bh\",\n        \"Area of a Rectangle: A = lw\",\n        \"Area of a Circle: A = πr²\",\n        \"Circumference of a Circle: C = 2πr\",\n        \"Volume of a Cube: V = s³\",\n        \"Volume of a Rectangular Prism: V = lwh\",\n        \"Volume of a Sphere: V = (4/3)πr³\",\n        \"Simple Interest: I = Prt\",\n        \"Compound Interest: A = P(1 + r/n)^(nt)\",\n        \"Slope of a Line: m = (y₂ - y₁) / (x₂ - x₁)\",\n\n\n    ]\n\n    for formula in formulas:\n        pyautogui.write(formula, interval=0.01)\n        pyautogui.press('enter')\n\n\n\nexcept Exception as e:\n    print(f\"An error occurred: {e}\")\n\n```",
                ],
            }
        ]
    )


    generated_code = completion.choices[0].message.content.strip()

    # Clean up code formatting
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()

    print("Generated Code:\n", generated_code)

    # Save code to a .py file
    with open(script_path, "w") as f:
        f.write(generated_code)

    print(f"Output saved to {script_path}")

    return generated_code


def execute_code_directly(code):
    try:
        exec(code, globals())
    except Exception as e:
        print(f"An error occurred during execution: {e}")


def interactive_run():
    while True:
        user_input = input("Enter your prompt: ")
        print("Generating Output code...")
        code = generate_and_save_output(user_input)

        print("Executing the script directly...")
        execute_code_directly(code)


# Example usage
interactive_run()
