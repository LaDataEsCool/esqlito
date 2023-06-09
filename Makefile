all: install

install: venv
	: # Activate venv and install invoke inside
	. .venv/bin/activate &&  \
	python3 -m pip install --upgrade pip && \
	pip3 install --upgrade setuptools &&  \
	pip install  invoke && \
	pip install -r requirements.txt

venv:
	: # Create venv if it doesn't exist
	: # test -d venv || virtualenv -p python3 --no-site-packages venv
	python3 -m venv .venv

test:
	: # Run your app here, e.g
	: # determine if we are in venv,
	: # see https://stackoverflow.com/q/1871549
	. .venv/bin/activate && pip -V

	: # Or see @wizurd's answer to exec multiple commands
	. .venv/bin/activate && \
		invoke bot

clean:
	rm -rf .venv
