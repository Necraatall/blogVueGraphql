# Steps

## prepare environment if not
python3.9 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

## run all
source .venv/bin/activate
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py runserver
### run npm in new terminal
source .venv/bin/activate
npm install
npm run serve



# jede