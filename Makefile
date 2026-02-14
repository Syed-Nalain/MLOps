PYTHON = C:/Users/PIXLAPS/scoop/apps/python/current/python.exe
PIP = $(PYTHON) -m pip

.PHONY: all setup download-data preprocess features train predict evaluate clean

all: evaluate

setup:
	$(PIP) install -r requirements.txt

data/raw/titanic.csv: src/download_data.py
	$(PYTHON) src/download_data.py

download-data: data/raw/titanic.csv

data/processed/train.csv data/processed/test.csv: src/preprocess.py data/raw/titanic.csv
	$(PYTHON) src/preprocess.py

preprocess: data/processed/train.csv

features/train_features.csv features/test_features.csv: src/features.py data/processed/train.csv data/processed/test.csv
	$(PYTHON) src/features.py

features: features/train_features.csv

models/model.pkl: src/train.py features/train_features.csv
	$(PYTHON) src/train.py

train: models/model.pkl

results/predictions.csv: src/predict.py models/model.pkl features/test_features.csv
	$(PYTHON) src/predict.py

predict: results/predictions.csv

results/metrics.txt: src/evaluate.py results/predictions.csv features/test_features.csv
	$(PYTHON) src/evaluate.py

evaluate: results/metrics.txt

clean:
	powershell -Command "if (Test-Path data) { Remove-Item -Recurse -Force data }"
	powershell -Command "if (Test-Path features) { Remove-Item -Recurse -Force features }"
	powershell -Command "if (Test-Path models) { Remove-Item -Recurse -Force models }"
	powershell -Command "if (Test-Path results) { Remove-Item -Recurse -Force results }"
