# simple file commands
main: 
	py src/main.py

parser: 
	py src/main.py


# run files using server
run:
	poetry run uvicorn src.main:app --log-level debug

bot:
	poetry run uvicorn src.main:app --log-level debug

api: 
	poetry run uvicorn src.api.api:app --reload


production:
	uvicorn src.main:app --host 0.0.0.0 --port 8000


# release-related commands
update:
	poetry update bot-engine

search:
	poetry search bot-engine

clear-cache:
	poetry cache clear pypi --all
