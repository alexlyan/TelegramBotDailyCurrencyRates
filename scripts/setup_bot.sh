cd $1 || exit
test -d venv || python3 -m venv venv
#venv/bin/pip3 install -r requirements/base.txt
bash ./scripts/start_screen.sh tg_bots 'venv/bin/python3 main.py'