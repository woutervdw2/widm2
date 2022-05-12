import logging
import pandas as pd

def combine_csv_from_same_test(test_nummer : int):
    logging.basicConfig(filename="combine_csv.log", encoding = "utf-8", filemode="w", level=logging.DEBUG)

    with open("loginnamen.txt") as file:
        """"
        Open het bestand waar de inlognamen van alle laptops staan
        waar de tests op gemaakt zijn.
        """
        inlognamen = file.readlines()
        inlognamen = [s.strip() for s in inlognamen]
        inlognamen = list(filter(lambda item: item, inlognamen))
    path = "losse_csv"
    for index, element in enumerate(inlognamen):
        """"
        Open de csv's die bij een test hoort van alle verschillende computers.
        De resulterende dataframe heet df_final.
        """
        if index == 0:
            try:
                df_final = pd.read_csv(f"{path}/quiz_{test_nummer}_{element}.csv", index_col="naam")
            except:
                logging.error(f"Het bestand van {element} ontbreekt")
        else:
            try:
                df_final = df_final.append(pd.read_csv(f"{path}/quiz_{test_nummer}_{element}.csv", index_col="naam"))

            except:
                logging.error(f"Het bestand van {element} ontbreekt")

    """"
    Controleer of er mensen zijn die de test twee keer gemaakt hebben.
    """
    twee_keer_test_gemaakt = df_final[df_final.index.duplicated(keep='first')].index.tolist()
    if twee_keer_test_gemaakt:
        mensen_dubbel = ""
        for item in twee_keer_test_gemaakt:
            mensen_dubbel += item + ","
        mensen_dubbel = mensen_dubbel[:-1]
        logging.info(f"De volgende mensen hebben twee keer de test gemaakt: {mensen_dubbel}")

    with open(f"jokers_vrijstellingen.txt") as file:
        """"
        Controleer of er mensen zijn die de test gemaakt hebben die niet meer in het spel zitten.
        """
        lines = file.readlines()[1:]
        namen = [s.strip().split(" ", 1)[0] for s in lines]
    ongeldige_mensen = ""

    for element in df_final.index.tolist():
        if element not in namen:
            ongeldige_mensen += element + ","
    if ongeldige_mensen:
        logging.info(f"De volgende mensen hebben de test gemaakt terwijl ze uit het spel liggen: {ongeldige_mensen[:-1]}")

    return df_final

df_final = combine_csv_from_same_test(1)
print(df_final)