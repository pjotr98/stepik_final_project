# stepik_final_project

👋 Hi! It is an automation demo project.

### Install JDK, python 3 and Allure reports first 👇

#### For Windows:

0. Install JDK and Python3 if not installed yet:

   > https://www.python.org/downloads/
   > 
   > https://www.oracle.com/java/technologies/javase-jdk16-downloads.html

1. Install scoop using PowerShell:

	> $ Set-ExecutionPolicy RemoteSigned -scope CurrentUser

	> $ iwr -useb get.scoop.sh | iex

2. Install Allure from scoop:

	> $ scoop install allure

3. Check Allure version to confirm installation:

	> $ allure --version
   
### Launch demo project
1. Clone 🐑 this repo 

   > $ cd ~/path/to/your/projects/folder/

   > $ git clone https://github.com/pjotr98/stepik_final_project.git

   > $ cd stepik_final_project/

2. Create env
   > $ python3 -m venv venv
   
3. Activate venv
   > $ source venv/bin/activate
   
   Or, for Windows
   
   > $ venv\Scripts\activate.bat
   
4. Install requirement from `requirements.txt` in env
   > $ pip install -r requirements.txt
   
5. Run test
   > $ pytest tests.py -s -v --tb=line --alluredir=allure-results

6. Open Allure report
   > $ allure serve allure-results
