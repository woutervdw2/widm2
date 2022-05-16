import pandas as pd
import sys
import os

#in_geval_van_crash.py 'testnummer' 'naam'
arguments = sys.argv[1:]

naam_persoon = arguments[1]
quiz_string = f"losse_csv/quiz_{arguments[0]}_{os.getlogin()}.csv"
df_herstel = pd.read_csv(quiz_string, engine = "python", index_col="naam", encoding='latin-1')

#Lijst met opgeslagen antwoorden
lijst_antwoorden = df_herstel.loc[naam_persoon, 'antwoorden'].split("}")[1:]
lijst_bool_antwoorden = df_herstel.loc[naam_persoon, 'bool_antwoorden'].split("}")[1:]


#Ingevulde antwoorden voor crash
with open("tijdelijke_opslag.txt") as backup_file:
    lines = backup_file.readlines()

tijdelijke_antwoorden_txt = lines[0].split('}')[1:]
tijdelijke_antwoorden_bool = lines[1].split('}')[1:]
tussentijd = lines[2]

#schoon alle strings beetje op
tijdelijke_antwoorden_txt = [antwoord.strip() for antwoord in tijdelijke_antwoorden_txt]
tijdelijke_antwoorden_bool = [bool.strip() for bool in tijdelijke_antwoorden_bool]


#Zet tijdelijke antwoorden in opgeslagen antwoorden
lijst_antwoorden[:len(tijdelijke_antwoorden_txt)] = tijdelijke_antwoorden_txt
lijst_bool_antwoorden[:len(tijdelijke_antwoorden_bool)] = tijdelijke_antwoorden_bool
nr_antwoorden_goed = lijst_bool_antwoorden.count('True')

#Update tijd door tijd van gecrashede test bij tijd delta op te tellen en dan te verminderen met opgeslagen tijd
vraag_nummer = len(lijst_antwoorden)
nieuwe_tijd =  df_herstel.loc[naam_persoon, 'tijd_delta'] + float(tussentijd) - df_herstel.loc[naam_persoon, f'{vraag_nummer}_tijd']

#Update csv met nieuwe waardes
df_herstel.loc[naam_persoon, 'antwoorden'] = "}".join(lijst_antwoorden)
df_herstel.loc[naam_persoon, 'bool_antwoorden'] = '}'.join(lijst_bool_antwoorden)
df_herstel.loc[naam_persoon, 'vragen_goed'] = nr_antwoorden_goed

#Nu doen we opgeslagen tijd in csv+tijd voordat test crashede.
# Dus gaan ervan uit dat bij de nieuwe poging de maker gelijk doorklikt naar vraag waar die gebleven was
df_herstel.loc[naam_persoon, 'tijd_delta'] = nieuwe_tijd

df_herstel.to_csv(quiz_string)

