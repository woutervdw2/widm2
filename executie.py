import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
import PIL.Image
from tkinter import font as tkFont
import sys
import os
import pyglet
import vlc
from combine_csv import *
from time import sleep
absolute_pad = os.path.abspath('executie.py')[:-12]
if "Tkinter" not in sys.modules:
    from tkinter import *


def maak_image(PATH, width):

    try:
        img = PIL.Image.open(PATH)
    except:
        logging.error(f"Het bestand {PATH} ontbreekt")
        error_occured = True

    basewidth = width
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

def check_uitslag():
    naam_uitslag = entry1.get().lower()
    video_path_goed = absolute_pad + '\\Executie\\Groen_echte_final.mp4'
    video_path_fout = absolute_pad + '\\Executie\\Rood_1.mp4'
    muziek = pyglet.media.load('afvaller_muziek.mp3')

    if naam_uitslag in deelnemers_dict:
        if deelnemers_dict[naam_uitslag]:
            video_file = video_path_goed
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(video_file)
            player.set_media(Media)
            player.toggle_fullscreen()
            player.play()
            sleep(5)
            while player.is_playing():
                sleep(1)
            player.stop()
            entry1.delete(first=0, last=len(entry1.get()))
        else:
            video_file = video_path_fout
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(video_file)
            player.set_media(Media)
            player.toggle_fullscreen()
            player.play()
            sleep(5)
            while player.is_playing():
                sleep(1)
            speel_muziekje = muziek.play()
            speel_muziekje
    else:
        entry1.delete(first = 0, last = len(entry1.get()))
        entry1.insert(0, 'Niet mogelijk')


def open_uitslag():
    global deelnemers_dict, quiz_nummer
    try:
        quiz_nummer = entry_begin.get()
        df_quiz = combine_csv_from_same_test(quiz_nummer)
    except:
        logging.error(f"De test met het nummer {quiz_nummer} heeft geen csv. Deze test is dus nog niet gemaakt.")
        entry_begin.delete(first=0, last=len(entry1.get()))
        entry_begin.insert(0, 'Invalid')

    deelnemers_dict = import_csv_data(df_quiz)
    root.destroy()
    global root2, Canvas2, full_width, full_height, text_coordx, text_coordy, font, txt
    root2 = Tk()
    root2.attributes('-fullscreen', True)  # make main window full-screen
    root2.update()
    full_width = root2.winfo_width()
    full_height = root2.winfo_height()
    text_coordx, text_coordy = (full_width / 4, full_height / 7)
    font = ('OCR A Extended', 30, 'bold')
    txt = tkFont.Font(family="OCR A Extended", size=30)
    global Canvas2
    Canvas2 = Canvas(root2, bg='black', highlightthickness=0)
    img = maak_image('achtergrond_quiz.jpg', full_width)
    Canvas2.create_image(0, 0, image=img, anchor='nw')
    Canvas2.pack(fill=tk.BOTH, expand=True)
    Canvas2.update()

    naam_invoer_scherm()



def import_csv_data(df : pd.DataFrame):
    aantal_vragen = (len(df.columns) - 4)/2
    deelnemers_dict = {a : True for a in df.index.tolist()}
    print(deelnemers_dict)
    with open(f'jokers_vrijstellingen.txt') as f:
        jokers_vrijstellingen = f.readlines()

    jokers_vrijstellingen = [x.strip() for x in jokers_vrijstellingen]

    for i in range(len(jokers_vrijstellingen)):

        current_persoon = jokers_vrijstellingen[i]

        if current_persoon.endswith('x'):
            current_persoon = current_persoon.rsplit(' ', 1)[0]
            current_persoon = current_persoon.split()[0].strip()
            df.loc[current_persoon, 'vragen_goed'] = aantal_vragen + 1


        elif current_persoon[-1].isdigit():
            aantal_jokers = int(current_persoon[-1])
            current_persoon = current_persoon.rsplit(' ', 1)[0]
            current_persoon = current_persoon.split()[0].strip()
            df.loc[current_persoon, 'vragen_goed'] = df.loc[current_persoon, 'vragen_goed'] + aantal_jokers


            if int(df.loc[current_persoon, 'vragen_goed']) > aantal_vragen:
                df.loc[current_persoon, 'vragen_goed'] = aantal_vragen


    minvalue_vragen_goed = df['vragen_goed'].min()
    if minvalue_vragen_goed <= aantal_vragen:

        df_minste_goed = df[df['vragen_goed'] == minvalue_vragen_goed]


        if len(df_minste_goed) > 1:
            maxvalue_tijd_delta = df_minste_goed['tijd_delta'].max()
            df_traagst = df_minste_goed[df_minste_goed['tijd_delta'] == maxvalue_tijd_delta]
            naam_afvaller = df_traagst.index.tolist()[0]
            deelnemers_dict[naam_afvaller] = False
        else:
            naam_afvaller = df_minste_goed.index.tolist()[0]
            deelnemers_dict[naam_afvaller] = False
    print(naam_afvaller)

    with open(f"jokers_vrijstellingen//jokers_vrijstellingen_{quiz_nummer}.txt", "w") as f:
        with open("jokers_vrijstellingen.txt", "w") as f2:
            f2.truncate(0)
            for naam in jokers_vrijstellingen:
                if naam == naam_afvaller.lower():
                    f.write(f"{naam}\n")
                else:
                    f.write(f"{naam}\n")
                    f2.write(f"{naam}\n")

    return deelnemers_dict

def quiz_invoer_scherm():
    global entry_begin
    entry_begin = tk.Entry(root, font=onze_font)
    button_begin = tk.Button(text='Enter', command=open_uitslag, font=onze_font)
    Canvas1.create_window(full_width / 2, full_height / 2, window=button_begin)
    Canvas1.create_window(full_width / 2, (full_height / 2) - 100, window=entry_begin)
    Canvas1.create_text(text_coordx + 50, text_coordy, text='Wat is het nummer van deze test?', fill='white', font=onze_font, tag='mytag')


onze_font = ('OCR A Extended', 30,'bold')
root=Tk()
root.attributes('-fullscreen', True) # make main window full-screen
root.update()
full_width = root.winfo_width()
full_height= root.winfo_height()
text_coordx, text_coordy = (full_width/4,full_height/7)
font = ('OCR A Extended', 30,'bold')
txt = tkFont.Font(family="OCR A Extended", size=30)

def naam_invoer_scherm():
    global entry1
    entry1 = tk.Entry(root2, font = onze_font)
    button_uitslag = tk.Button(text = 'Enter', command = check_uitslag, font = onze_font)
    Canvas2.create_window(full_width/2,full_height/2, window = button_uitslag)
    Canvas2.create_window(full_width/2, (full_height/2)-100, window=entry1)
    Canvas2.create_text(text_coordx,text_coordy, text = 'Wie moet naar huis?', fill = 'white', font = onze_font, tag='mytag')
    root2.mainloop()

global Canvas1, error_occured
error_occured = False
logging.basicConfig(filename=f"executie_logs\executie_{test_nummer}.log", encoding = "utf-8", filemode="w",
                        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
Canvas1 = Canvas(root, bg='blue', highlightthickness=0)
img = maak_image('achtergrond_quiz.jpg', full_width)
Canvas1.create_image(0,0,image = img, anchor='nw')
Canvas1.pack(fill=tk.BOTH, expand=True)



quiz_invoer_scherm()


root.mainloop()