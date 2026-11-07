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

```text

Let's understand each component.
Code	Purpose
import os	Access environment variables
from google import genai	Import Gemini SDK
genai.Client()	Create Gemini API client
api_key	Authenticate with Google
http_options	Configure HTTP request options
timeout=120000	Set timeout to 120 seconds
generate_content()	Send prompt to Gemini
response.text	Read generated answer
try/except	Handle errors

9. Run the Python program
Make sure your virtual environment is activated.

PowerShell:
python gemini_test.py

Expected successful output (example):
Sending request to Gemini...

Gemini response:
AI works by learning patterns from data
and using them to generate predictions
or responses.

10. Errors we encountered and their meanings
This is particularly important for your future troubleshooting.

We encountered three different errors.
Error 1: 404 NOT_FOUND
Model availability issue
This model gemini-2.5-flash is no longer
available to new users.

Reason: The API response said the old model was unavailable to new users.

# Action taken: Changed the model name to gemini-3.8-flash, as suggested by that error.

Error 2: 504 DEADLINE_EXCEEDED
Timeout issue
Deadline expired before operation could complete.


Reason: The API operation did not complete within the allowed time.

Action taken: Increased HTTP timeout from 30 seconds to 120 seconds.
timeout=120000

Error 3: 503 UNAVAILABLE
Temporary service issue
This model is currently experiencing high demand.


Reason: Google reported that the model was experiencing high demand.

Action taken: Wait and retry later. Increasing the timeout does not fix service capacity issues.

11. HTTP status codes – Quick reference
Status code	Meaning	What to check
200	Success	Request completed
400	Bad request	Request parameters
401	Unauthorized	API authentication
403	Forbidden	Permissions
404	Not found	Model availability/name
429	Too many requests	Quota and rate limits
500	Internal server error	Server-side issue
503	Service unavailable	Retry later
504	Gateway timeout	Timeout/network/service

12. How to resume the project next time
You don't need to repeat the installation steps every time.

Just follow these commands:
Your next-session commands

Step 1: Open PowerShell
F:
cd gemini-project


Step 2: Activate environment
.\genai-env\Scripts\Activate.ps1


Step 3: Set API key again
$env:GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"


Step 4: Execute Python program
python gemini_test.py

If you close PowerShell, the temporary environment variable will disappear. Set it again when you start a new session.

To exit your virtual environment:
deactivate

13. Important concepts learned
Concept	What you learned
Python venv	Isolated Python environment
pip	Python package installer
SDK	Tools to communicate with AI models
API key	Authentication credential
API	Communication between applications
Environment variable	Securely separating configuration from code
HTTP timeout	Maximum time allowed for an HTTP request
Exception handling	Handling errors using try/except
HTTP status codes	Understanding API responses

14. Future learning roadmap
Once the Gemini API works, I suggest progressing through these practical exercises:
1. Basic Gemini API
   
   Send different prompts and receive responses.
2. Interactive AI chatbot
   
   Ask questions repeatedly using a Python while loop.
3. Chat history
   
   Maintain previous conversations and context.
4. PDF-based AI chatbot
   
   Upload a PDF and ask questions about its contents.
5. RAG application
   
   Connect your own documents to an AI model.
6. AI Agent
   
   Build an agent that can use tools and perform tasks.
7. AWS deployment
   
   Deploy your AI application using Docker, ECS or EKS.
```
