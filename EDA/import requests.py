import requests
import pandas as pd

url = "https://www.proteomicsdb.org/proteomicsdb/logic/api_v2/api.xsodata/Experiment?$filter=EXPERIMENT_ID lt 2356&$format=json"
response = requests.get(url)

# Verificar código de estado
print(f"Código de estado: {response.status_code}")

# Imprimir el contenido de la respuesta
#print(f"Contenido de la respuesta: {response.text}")

data = response.json()
print(type(data))
df = pd.DataFrame(data)
print(df.columns)

