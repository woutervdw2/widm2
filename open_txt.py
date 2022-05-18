from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pyglet
from tkinter import font as tkFont
from playsound import playsound
from Functies import *
from Classes import *
import os
import logging
from csv import DictWriter
import pandas


import sys
if "Tkinter" not in sys.modules:
    from tkinter import *
global voltooide_tests
voltooide_tests = 0
pandas
pyglet.font.add_file('OCRAEXT.TTF')


def maak_root():
    global button, button_no, img, root, Canvas1, full_width, full_height, text_coordx, text_coordy
    root = Tk()

    root.attributes('-fullscreen', True)  # make main window full-screen


    root.update()
    full_width = root.winfo_width()
    full_height = root.winfo_height()

    font = ('OCR A Extended', 30, 'bold')
    txt = tkFont.Font(family="OCR A Extended", size=30)


    img = maak_image('achtergrond_quiz.jpg', full_width)
    button_no = maak_image('vingerafdruk_noklik.png', width=60)
    button = maak_image('vingerafdruk_klik.png', width=60)
    """Creëer het canvas"""
    Canvas1 = Canvas(root, bg='blue', highlightthickness=0)

    """Maak de achtergrond"""
    Canvas1.create_image(0, 0, image=img, anchor='nw')

    """Laat het canvas heel het venster innemen"""
    Canvas1.pack(fill=tk.BOTH, expand=True)

    text_coordx, text_coordy = (full_width / 4, full_height / 7 - 100)


def quiz_invoer_scherm():
    try:
        maak_root()
    except:
        pass

    if voltooide_tests == 0:
        global entry_begin
        entry_begin = tk.Entry(root, font=onze_font)
        button_begin = tk.Button(text='Enter', command=open_uitslag, font=onze_font)
        Canvas1.create_window(full_width / 2, full_height / 2, window=button_begin)
        Canvas1.create_window(full_width / 2, (full_height / 2) - 100, window=entry_begin)
        Canvas1.create_text(text_coordx+20, text_coordy, text='Wat is het nummer van deze test?', fill='white', font=onze_font, tag='mytag')
    else:
        open_uitslag()
    root.mainloop()

def test_maker():

    global entry1
    entry1 = tk.Entry(root, font=onze_font)
    button_uitslag = tk.Button(text='Enter', command= doe_test, font=onze_font)
    Canvas1.create_window(full_width / 2, full_height / 2, window=button_uitslag)
    Canvas1.create_window(full_width / 2, (full_height / 2) - 100, window=entry1)
    Canvas1.create_text(text_coordx, text_coordy, text='Wie maakt de test', fill='white', font=onze_font,
                        tag='mytag')
    root.mainloop()


def doe_test():
    with open("tijdelijke_opslag.txt", "w") as filehandle:
        filehandle.truncate(0)
    global speel_muziekje
    try:
        speel_muziekje = muziek.play()
        speel_muziekje
    except:
        logging.error("Muziek niet aanwezig check test_muziek.wav")

    speler = Spelers(naam=entry1.get(), mol=False, in_game=True)
    vragen = lees_quiz(quiz_str, speler)
    aantal_vragen = len(vragen)
    Canvas1.delete('mytag')
    Canvas1.delete(ALL)
    try:
        img = maak_image('achtergrond_quiz.jpg', full_width)
        Canvas1.create_image(0, 0, image=img, anchor='nw')
    except:
        logging.error('Achtergrond image niet aanwezig, check achtergrond_quiz.jpg')
    Canvas1.pack(fill=tk.BOTH, expand=True)
    Canvas1.update()
    nieuwe_vraag(1, aantal_vragen, vragen=vragen, Canvas1=Canvas1, text_coordy=text_coordy,
                 text_coordx=text_coordx, root=root, full_height=full_height, full_width=full_width,
                 button_no=button_no, button=button, player=speler, txt_file=quiz_str)

    root.mainloop()

def open_uitslag():
    try:
        global testnummer
        testnummer = entry_begin.get()
    except:
        pass
    global quiz_str
    quiz_str = '\\quiz_' + testnummer




    logging.basicConfig(filename=f"test_logs/test_{testnummer}.log",
                        encoding="utf-8", filemode="w", level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # root.destroy()


    global root2, Canvas2, full_width, full_height, text_coordx, text_coordy, font, txt
    Canvas1.delete('mytag')
    Canvas1.delete(ALL)

    try:
        img = maak_image('achtergrond_quiz.jpg', full_width)
        Canvas1.create_image(0, 0, image=img, anchor='nw')
        Canvas1.pack(fill=tk.BOTH, expand=True)
    except:
        logging.debug("Achtergrond image is niet in folder, check of achtergrond image aanwezig is test file")


    test_maker()
    root.mainloop()

def main():
    global voltooide_tests, aantal_deelnemers, muziek

    muziek = pyglet.media.load('test_muziek.wav')

    with open('jokers_vrijstellingen.txt', 'r') as f:
        aantal_deelnemers = len(f.readlines()) - 1


    while voltooide_tests < aantal_deelnemers:
        quiz_invoer_scherm()
        speel_muziekje.next_source()
        voltooide_tests += 1


while __name__ == '__main__':
    main()









