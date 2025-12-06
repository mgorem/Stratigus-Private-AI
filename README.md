Images are displayed in the word and pdf files inside the zip folder

User Guide for Stratigus Private AI
Introduction
This guide shows you how to set up and run a Stratigus Custom local AI assistant that can read and analyse any public web page. You do not need to be a programmer. By the end, you will be able to paste a website link into a simple window and get a summary or analysis from your local LM Studio model.
What You Need Before You Start
-	A Windows computer
-	LM Studio installed and working (refer to LM studio documentation on how to install and use it – https://lmstudio.ai/download). Refer to the figure below:
 
-	Python 3.10 or newer (https://www.python.org/downloads/). Refer to the figure below:
 
-	The “stratigus_lmstudio_web_agent” folder (we will send this to you as a zip file through a downloadable link).
Step 1: Download the Agent Package
-	Download the zip file from this link: https://drive.google.com/file/d/1ADThYKH0SG0wF5B1qfN4XL-Bg1IXGtwB/view?usp=sharing : stratigus_lmstudio_web_agent.zip.
-	Save it somewhere easy to find (e.g. Desktop or Documents). Refer to the figure below:
 
-	Right-click it and choose ‘Extract All’. Refer to the figure below:
 
-	You should now see a folder called stratigus_lmstudio_web_agent next to the zipped folder as shown below:
 

Step 2: Open the Folder in PowerShell
-	Open the stratigus_lmstudio_web_agent agent folder. Refer to the figure below:
 
-	Right click any empty space in the folder and from the list choose ‘open with terminal’ as shown below:
 
-	A blue or black window (Powershell) will open. This window is now “inside” the agent folder. Refer to the figure below:
 
Step 3: Run the Setup Script (Automatic Method)
In the black window, copy and paste this command as it is without the brackets: (.\setup_agent.ps1) and press ‘Enter’.
-	A new PowerShell window may open and start installing required components.
-	When it finishes, you will see the screen with the virtual environment open ready again and no error messages as shown below:
 
Step 4: Prepare LM Studio
-	Open LM Studio.
-	Go to the Models section.
-	Download and load any model that supports tools (your IT support person can choose one for you or you can choose the one used in this case: ‘qwen2.5-vl-7b-instruct’). Refer to the figure below:
 
-	Go to Settings (on the right bottom left side of LM Studio)
-	 Ensure Local LLM Service / Local Server is turned ON. Refer to the screenshot below:
 
-	Leave LM Studio open while you use the agent.
Step 5: Start the Web Analysis Agent
-	Go back to the stratigus_lmstudio_web_agent folder if not already there.
-	Click in the address bar and type the word powershell and press ‘Enter’.
-	Inside powershell (the black/blue window), type (.\run_agent.ps1) excluding the brackets and press ‘Enter’.
-	A window will open with this prompt: 
‘User (Please prompt the tool to fetch and summarise a page of your choice or blank + Enter to exit):’. Refer to the screenshot below. It should like this:
 
Example Queries You Can Try:
	Please summarise this page: https://www.python.org
	Analyse the main topics on this page: https://www.bbc.com/news
	Explain this page in simple language: https://example.com/some-article
Output after trying the second prompt is as shown below:
 
Troubleshooting (Common Problems):
-	Python is not recognised → Ask IT to install Python in your device.
-	LM Studio connection error → Make sure Local LLM Service is ON (Step 4).
-	Model error → Change model name in agent.py (handled by IT).
