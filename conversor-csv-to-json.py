import csv
import json

with open('cadastro.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('cadastro-output.json', 'w') as f:
    json.dump(rows, f)