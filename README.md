# sleepy-peak-45718

# run in cmd
py -3 -m venv .venv  

# run in cmd - venv mode
python -m pip install --upgrade pip  
pip install -r requirements.txt  
python manage.py migrate (uncomment sqlite DB settings in 'settings.py' if postgres is not installed)
