all: clean collect clean_data process analyze

clean:
	rm -rf data img

.PHONY: collect data img

collect:
	mkdir -p data/
	python src/html_to_csv.py
	python src/import_requests.py

clean_data: collect
	requirements.txt 
	jupyter nbconvert --execute --to notebook --inplace --ExecutePreprocessor.timeout=-1 notebooks/cleaning.ipynb

process: clean_data 
	jupyter nbconvert --execute --to notebook --inplace --ExecutePreprocessor.timeout=-1 notebooks/transformation.ipynb

analyze: process 
	mkdir -p img/
	jupyter nbconvert --execute --to notebook --inplace --ExecutePreprocessor.timeout=-1 notebooks/exploration.ipynb
