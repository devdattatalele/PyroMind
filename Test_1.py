import os
import time
import pyautogui
import google.generativeai as genai

# Path to the saved script
script_path = os.path.join(os.getcwd(), "generated_output.py")

# Configure GenAI
genai.configure(api_key="AIzaSyDbseveUEArcDGT3LaZ63HWt1Y-1TMluxY")

# Create the model with generation configuration
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
    system_instruction=(
        "You are an AI assistant designed to generate and execute code reliably and securely. "
        "You receive user requests for code in natural language. Your responses should adhere "
        "to the following process:\n\n"
        "1. Code Generation: Generate concise, efficient, and executable code based on the user's request. "
        "Prioritize clarity and avoid unnecessary complexity. The code should be ready for immediate execution.\n\n"
        "2. Security Assessment: Evaluate for potential security risks. Do not execute code that could compromise "
        "system integrity or perform malicious actions. Reject such requests with an explanation.\n\n"
        "3. Execution Environment: Execute the generated code in a controlled environment. Manage dependencies and "
        "ensure necessary libraries are available.\n\n"
        "4. Error Handling: Implement robust error handling. If an error occurs:\n"
        "   a) Report the error clearly to the user.\n"
        "   b) Provide suggestions for correction.\n\n"
        "5. Output: Return the output of the code execution. If an error occurred, return the error message.\n\n"
        "6. Automation Tasks: Use appropriate libraries, like PyAutoGUI for GUI automation, and ensure actions are "
        "performed safely.\n\n"
        "7. Platform Compatibility: Provide platform-specific instructions if necessary.\n\n"
        "8. Do not use subprocess or similar libraries. ONLY use PyAutoGUI for automation.\n\n"
        "9. Use appropriate hotkeys with a 1-second delay, e.g., PyCharm uses 'alt+insert' for new files.\n\n"
        "10. If no app is specified, open Notepad. For specified apps, try to run the program using PyAutoGUI.\n\n"
        "11. Provide Python code only, without additional explanations."
        "8. Do not use subprocess or any such library. ONLY USE pyautogui to navigae and open applications.\n\n"
        "9. Always remeber to open new window after opening a app and provide proper interval by putting     time.sleep(1) delay where ever necessary after pyautogui.hotkey  Rember Pycharm uses alt+insert for new window and vscode and notepad use ctrl+N.\n\n"
        " 10. IF certain app is mentioned in pompt open and use that app (ie.pycharm, vscode) if app is not provided open notepad instead. if app is provided try to run program on your own by using pyautohotkeys functions to navigate within app\n\n"
        "And do  not explain or give any kind of other onformation or text other than python code\n\n"
        "example :    pyautogui.hotkey('win') pyautogui.typewrite('notepad\n', interval=0.1) time.sleep(1) pyautogui.hotkey('ctrl','n')    time.sleep(1)    pyautogui.typewrite('Hello, World!', interval=0.1)    print('Successfully typed 'Hello, World!' in Notepad.')"
    )
)

def generate_and_save_output(prompt):
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
    response = chat_session.send_message(prompt)
    generated_code = response.text

    # Clean the code by removing ```python and ``` markers
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()

    print("Generated Code:\n", generated_code)

    # Save the output to a .py file
    with open(script_path, "w") as f:
        f.write(generated_code)
    print("Output saved to generated_output.py")

def run_generated_script_in_terminal():
    try:
        # Open Terminal
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.typewrite('cmd\n', interval=0.1)
        time.sleep(2)

        # Run the script
        pyautogui.typewrite(f'python "{script_path}"\n', interval=0.1)
        print("Script execution initiated in the terminal.")
    except Exception as e:
        print(f"An error occurred: {e}")
        if "pyautogui" in str(e):
            print("Make sure PyAutoGUI is installed: `pip install pyautogui`")

# Example usage
user_input = input("Enter your prompt: ")
print("Generating Output code...")
generate_and_save_output(user_input)
run_generated_script_in_terminal()
