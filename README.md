# stepik_final_project

### Task: Run automated test for different languages

👋 Hi!

To run test, You need to:

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
   > $ pytest -v --tb=line --language=en -m need_review
