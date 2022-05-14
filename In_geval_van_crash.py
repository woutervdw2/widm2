import pandas as pd
import sys
import os

arguments = sys.argv[1:]
naam_persoon = arguments[1]
quiz_string = f"losse_csv/quiz_{arguments[0]}_{os.getlogin()}.csv"
df_herstel = pd.read_csv(quiz_string, engine = "python", index_col="naam")
lijst_antwoorden = df_herstel.loc[naam_persoon, 'antwoorden'].split("}")[1:]
with open("tijdelijke_opslag.txt") as backup_file:
    lines = backup_file.read()

print(lines)

# for element in lijst_antwoorden:ds

print(lijst_antwoorden)