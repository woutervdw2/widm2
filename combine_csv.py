import logging
import pandas as pd

def combine_csv_from_same_test(test_nummer : int):
    error_occured = False
    logging.basicConfig(filename=f"executie_logs\executie_{test_nummer}.log", encoding = "utf-8", filemode="w",
                        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

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
                df_final = pd.read_csv(f"{path}/quiz_{test_nummer}_{element}.csv")
            except:
                logging.error(f"Het bestand van {element} ontbreekt in de map losse_csv")
                error_occured = True
        else:
            try:
                df_final = df_final.append(pd.read_csv(f"{path}/quiz_{test_nummer}_{element}.csv", index_col="naam"))

            except:
                logging.error(f"Het bestand van {element} ontbreekt in de map losse_csv")
                error_occured = True

    if not error_occured:

        logging.info(f"Alle bestanden zijn geopend en samengevoegd.")

    """"
    Controleer of er mensen zijn die de test twee keer gemaakt hebben.
    """
    twee_keer_test_gemaakt = df_final[df_final.index.duplicated(keep='first')].index.tolist()
    if twee_keer_test_gemaakt:
        mensen_dubbel = ""
        for item in twee_keer_test_gemaakt:
            mensen_dubbel += item + ","
        mensen_dubbel = mensen_dubbel[:-1]
        logging.error(f"De volgende mensen hebben twee keer de test gemaakt: {mensen_dubbel}")
        error_occured = True
    else:
        logging.info(f"Niemand heeft de test twee keer gemaakt.")

    with open(f"jokers_vrijstellingen.txt") as file:
        """"
        Controleer of er mensen zijn die de test gemaakt hebben die niet meer in het spel zitten.
        """
        lines = file.readlines()[1:]
        namen = [s.strip().split(" ", 1)[0] for s in lines]
    ongeldige_mensen = ""
    for naam in namen:
        if naam not in df_final.index.tolist():
            logging.error(f"{naam} zit in het spel maar heeft de test nog niet gemaakt")
            error_occured = True
    for element in df_final.index.tolist():
        if element not in namen:
            ongeldige_mensen += element + ", "
    if ongeldige_mensen:
        logging.error(f"De volgende mensen hebben de test gemaakt terwijl ze uit het spel liggen: {ongeldige_mensen[:-1]}")
        error_occured = True
    else:
        logging.info(f"Alle mensen die de test hebben gemaakt zitten nog in het spel.")
    if not error_occured:
        logging.info(f"De test is gemaakt door iedereen die nog in het spel zit en niemand heeft de test dubbel gemaakt")
        df_final.to_csv(f"totaal_csv\\quiz_{test_nummer}")
    return df_final

