### Google Gemini SDK – Python Setup & Execution Guide

Project location: F:\gemini-project
Virtual environment: genai-env
Python SDK: google-genai

Model attempted: gemini-3.8-flash (as suggested by the API error; availability needs to be verified)
1. Understand what we are building
Our objective is to connect a Python application to Google's Gemini AI model


# The execution flow:
1. Python application sends a prompt.
2. Gemini SDK communicates with Google's API.
3. Google processes the prompt using its AI model.
4. Gemini returns the generated response.
5. Python displays the response.
2. Create a project directory
We selected the E/F drive instead of C: to keep our project files separate from the Windows system drive.

Open PowerShell:
F:
mkdir gemini-project
cd gemini-project

Expected:Path
----
F:\gemini-project
3. Create a Python virtual environment
Command:
python -m venv genai-env

What is a virtual environment?

Think of it as a separate room for your Python project.

It keeps the libraries and dependencies of this project separate from other Python projects.

Our folder structure:
F:\gemini-project
        |
        |--- genai-env
        |       |
        |       |--- Scripts
        |       |--- Lib
        |       |--- Include
        |
        |--- gemini_test.py


4. Activate the virtual environment
Initially, we encountered this error:
running scripts is disabled on this system

This happened because Windows PowerShell was blocking script execution.

We fixed it using:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Then activated the environment:
.\genai-env\Scripts\Activate.ps1


# Expected output:
(genai-env) PS F:\gemini-project>

Remember: (genai-env) means your virtual environment is active.
# 5. Install Google Gemini SDK
Command:
python -m pip install --upgrade google-genai

What is an SDK?

SDK stands for Software Development Kit.

It provides ready-made Python libraries and functions to communicate with Google's Gemini models.

Verify installation:
python -m pip show google-genai

6. Generate a Gemini API key
We used Google AI Studio.
Open Google AI Studio – Create API KeySteps:
1. Sign in using your Google account.
2. Select Create API Key.
3. Create or select a Google Cloud project as prompted.
4. Copy your API key.
Important: Never share your API key or commit it to GitHub.
7. Understand API key configuration
Initially, we placed the API key directly inside the Python code.

Example:
client = genai.Client(    api_key="YOUR_ACTUAL_API_KEY")

This works, but it is not a good security practice.

We then learned to use an environment variable.

In PowerShell:
$env:GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"

Check whether it is set:
echo $env:GEMINI_API_KEY

The variable is available only in the current PowerShell session unless you configure it persistently.
8. Create the Python program
We created a file called:
gemini_test.py

Command:
python gemini_test.py
