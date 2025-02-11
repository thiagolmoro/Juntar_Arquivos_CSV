# pip install pandas

import pandas as pd
import os

# Lista de arquivos CSV (coloque os nomes ou caminhos dos seus arquivos aqui)
arquivos_csv = [
    "bots_arrojado - 2.csv",
    "bots_arrojado-2024-12-04 - 2.csv",
    "bots_arrojado-2024-12-14 - 2.csv",
    "bots-2024-11-28 - 2.csv",
    "bots-2024-11-30 - 2.csv",
    "bots-2024-12-02 - 2.csv",
    "bots-2024-12-03 - 2.csv"
]

# Verifica se todos os arquivos existem
for arquivo in arquivos_csv:
    if not os.path.exists(arquivo):
        print(f"Arquivo não encontrado: {arquivo}")
        exit()

# Lê e combina todos os arquivos CSV
dataframes = [pd.read_csv(arquivo) for arquivo in arquivos_csv]

# Combina todos os DataFrames em um único
arquivo_unico = pd.concat(dataframes, ignore_index=True)

# Ordena o DataFrame pelos campos "DataFinal" e "Simu"
arquivo_unico = arquivo_unico.sort_values(by=["DataFinal", "Simu"])

# Remove duplicatas no campo "Simu", mantendo apenas o registro mais recente
arquivo_unico = arquivo_unico.drop_duplicates(subset="Simu", keep="last")

# Salva o arquivo combinado, ordenado e sem duplicatas
arquivo_unico.to_csv("arquivo_unico.csv", index=False)

print("Os arquivos foram unidos, ordenados e as duplicatas foram tratadas no arquivo_unico.csv!")
