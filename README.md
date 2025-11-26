python -m venv venv                # create a virtual environment
source venv/Scripts/activate       # activate it (Git Bash / Linux/Mac)
# or venv\Scripts\activate.bat     # activate in Windows cmd
pip install -r backend/requirements.txt   # install all dependencies

uvicorn main:app --reload --port 3000     # run FastAPI server
