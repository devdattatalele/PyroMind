import streamlit as st
import os
import time
import pyautogui
import google.generativeai as genai
import pyperclip
import base64

def configure_model():
    genai.configure(api_key="AIzaSyA3-uNY4klQmZ-AJi3eG3kk-zuX2AbrZoU")
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
    return model

# Initialize the model
model = configure_model()

def generate_code(prompt):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [prompt],
            },
        ]
    )

    # Send the prompt and get the response
    response = chat_session.send_message(prompt)
    generated_code = response.text

    # Clean the generated code
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()

    # Save the code to a file
    script_path = os.path.join(os.getcwd(), "generated_output.py")
    with open(script_path, "w") as f:
        f.write(generated_code)

    return generated_code

def run_script():
    try:
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.typewrite('cmd\n', interval=0.1)  # Open command prompt (Windows-specific)
        time.sleep(2)

        # Run the script
        script_path = os.path.join(os.getcwd(), "generated_output.py")
        pyautogui.typewrite(f'python "{script_path}"\n', interval=0.05)

        return "Script execution initiated. Check the terminal for results."

    except Exception as e:
        return f"An error occurred: {e}"

def process_prompt(prompt):
    generated_code = generate_code(prompt)
    execution_message = run_script()
    return generated_code, execution_message


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def copy_to_clipboard(text, button_key):
    if st.button("📋 Copy", key=button_key):
        pyperclip.copy(text)
        st.success("Copied to clipboard!")
# Streamlit UI Design
st.set_page_config(page_icon="https://github.com/devdattatalele/Krya.ai/blob/main/logo.png",page_title="Krya.ai Automation Console", layout="wide")

# Custom CSS for modern look and adjustments
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .terminal {
        color: #00ff00;
        padding: 10px;
        border-radius: 8px;
    }
    .logo {
        display: flex;
        align-items: center;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .logo img {
        width: 60px;
        height: 60px;
        margin-right: 10px;
    }
    .logo h2 {
        color: #007acc;
        margin: 0;
        font-size: 3.5rem;
    }
    .button {
        background-color: #2e2e2e;
        border: 1px solid #007acc;
        border-radius: 5px;
        padding: 0.5rem;
        margin: 0.5rem 0;
        color: #ffffff;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .command-button:hover {
        background-color: #007acc;
        transform: translateX(5px);
    }
    .social-links {
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
        justify-content: center;
    }
    .social-link {
        color: #007acc;
        text-decoration: none;
        padding: 0.5rem;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    .social-link:hover {
        background-color: #007acc;
        color: white;
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 10vh;
    }
    .sample-prompts {
        font-size: 0.9rem; /* Adjust font size */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:
    # Logo and Project Name
    st.markdown("""
        <div class="logo">
            <img src="https://github.com/devdattatalele/Krya.ai/blob/main/logo.png" alt="logo.jpeg"/>
            <h2>Krya AI</h2>
        </div>
    """, unsafe_allow_html=True)

    
    st.markdown("### Sample Prompts-")
    st.markdown("<div class='sample-prompts'>", unsafe_allow_html=True)
    st.code("Generate a portfolio website on VS CODE", language="text")
    st.code("Compare Phones Under 20k on different E-commerce websites", language="text")
    st.code("Type Gmail letter to HR about Leave", language="text")
    st.code("Create a simple website and host it on AWS", language="text")
    st.markdown("</div>", unsafe_allow_html=True)

    # Social Links
    st.markdown("---")
    st.markdown("       Developed by Devdatta Talele")

    st.markdown("""
        <div class="social-links">
            <a href="https://github.com/devdattatalele/krya.ai" target="_blank" class="social-link">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="https://linkedin.com/in/devdatta-talele" target="_blank" class="social-link">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
        </div>
    """, unsafe_allow_html=True)

# Main Content Centered
st.markdown("""
    <div class="main-container">
        <h1>KRYA.AI</h1>
""", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem;'> \
            Automated interactions and code execution on local machine </h3>", unsafe_allow_html=True)
user_input = st.text_input("Enter your command", placeholder="e.g., Open Notepad")
execute_button = st.button("Execute")

st.markdown("</div>", unsafe_allow_html=True)

if execute_button and user_input:
    with st.spinner("Processing your request..."):
        code, execution_status = process_prompt(user_input)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Generated Code")
            st.code(code, language="python")
            copy_to_clipboard(code, "copy_code")
        with col2:
            st.subheader("Execution Status")
            st.text_area("", execution_status, height=400, key="execution_status")
            copy_to_clipboard(execution_status, "copy_status")
