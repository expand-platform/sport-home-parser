main: 
	py src/main.py

parser: 
	py src/main.py

api: 
	uvicorn src.api.api:app --reload
