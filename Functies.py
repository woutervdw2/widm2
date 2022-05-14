""""Hier komen alle functies in te staan die we vervolgens in main.py gaan importeren"""
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pyglet
from tkinter import font as tkFont
from playsound import playsound
from Classes import *
import time
import pandas as pd
import os
pd.set_option('display.max_columns', None)
from csv import writer
import random
import textwrap
import logging





absolute_pad = os.path.abspath('executie.py')[:-12]
onze_font = ('OCR A Extended', 30,'bold')
global voltooide_tests, aantal_deelnemers
voltooide_tests = 0


def maak_image(PATH, width):
    img = Image.open(PATH)
    basewidth = width
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

def lees_quiz(txt_file, player):
    """Open de txt file van een quiz en stop de vragen in een dictionary"""
    global aantal_deelnemers

    with open(absolute_pad + '\\test_files' + txt_file + '.txt', 'r', encoding='utf-8') as f:
        lijst_regels = f.readlines()
    
    lijst_regels = [x.strip() for x in lijst_regels]
    vraag_dict = {}
    current_question = 0
    global df_quiz

    df_quiz = pd.DataFrame(columns = ['naam', 'start_time'])
    player.begin_quiz()
    new_row = {'naam' : player.naam, 'start_time' : player.test_tijd_begin}
    df_quiz = df_quiz.append(new_row, ignore_index = True)

    
    for i in range(len(lijst_regels)):

        if lijst_regels[i].endswith('?'):
            current_question += 1
            vraag_dict[current_question] = [lijst_regels[i]]
            
        
        else:
            vraag_dict[current_question].append(lijst_regels[i])
    if os.path.isfile(absolute_pad + '\\losse_csv\\'+ txt_file + "_" + os.getlogin() + '.csv'):
        pass
    else:
        #columns = ['naam', 'start_time', 'vragen_goed']
        #for i in range(1, current_question+1):
        #    columns.extend([str(i)+'_tijd', i])
        df = pd.DataFrame(columns = ['wahe'])
        df.to_csv(absolute_pad + '\\losse_csv\\' + txt_file + "_" + os.getlogin() + '.csv', index = False)

    return vraag_dict


def maak_vraag(vraag_dict : dict, vraag_nummer : int, df_quiz : pd.DataFrame, root):
    """Functie die uit een dictionairy de vraag als string returned en een lijst met alle button objecten
    van de antwoorden"""
    antwoorden_dict = {}
    button_objects = []
    vraag = vraag_dict[vraag_nummer][0]
    MAX_LENGTH = 50
    full_width = root.winfo_width()
    #Breek vragen
    vraag = textwrap.fill(text=vraag, width=MAX_LENGTH)


    string_vraag = str(vraag_nummer) + '_tijd'
    df_quiz[string_vraag] = time.time()
    df_quiz['vragen_goed'] = 0
    vraag_dict[vraag_nummer] = vraag_dict[vraag_nummer][1:]
    random.shuffle(vraag_dict[vraag_nummer])
    for i in range(0, len(vraag_dict[vraag_nummer])):
        if vraag_dict[vraag_nummer][i].startswith('!'):
            button_objects.append(Buttons(text=vraag_dict[vraag_nummer][i][1:], correct=True))
        
        else:
            button_objects.append(Buttons(text=vraag_dict[vraag_nummer][i], correct=False))
            
    return vraag, button_objects

def plaats_vraag(vraag, canvas, text_coordx, text_coordy, root):
    canvas.create_text(50,text_coordy, text = vraag, fill = 'white', font = onze_font, anchor=tk.W, tag='mytag')

    root.update()
    
def plaats_antwoorden(antwoorden, canvas, root, full_height, full_width,text_coordx, text_coordy, button_noklik, button_klik, player, vraagnummer, aantal_vragen,
                      vragen, txt_file):
    """Plaats de lijst met buttonobjecten op het scherm"""
    AFSTAND_TOT_VRAAG = 100
    ysteps = (full_height-text_coordy-AFSTAND_TOT_VRAAG)/7
    txt = tkFont.Font(family="OCR A Extended", size=30)
    global buttons
    buttons = []
    #todo controleer plaats en breek lange antwoorden

    for i in range(len(antwoorden)):
        if len(antwoorden)>3:
            xcoord = 20+i%2*full_width/2
            if i%2 == 0:
                ycoord = text_coordy + AFSTAND_TOT_VRAAG + ysteps * i
            else:
                ycoord = text_coordy + AFSTAND_TOT_VRAAG + ysteps * (i-1)
        else:
            xcoord = 20
            ycoord = text_coordy + AFSTAND_TOT_VRAAG + ysteps * i*2

        text = antwoorden[i].text
        text = textwrap.fill(text, width = 25)
        if antwoorden[i].correct:
            b = tk.Button(canvas, image=button_noklik, relief=FLAT, borderwidth=0, highlightthickness=0, bd=0,
                          command=lambda i=i: Click(i, button_klik,  vraagnummer, aantal_vragen,correct = True, player= player,
                                                    vragen=vragen, Canvas1=canvas, text_coordx=text_coordx,
                                                    text_coordy=text_coordy, root=root,
                                                    full_height=full_height, full_width=full_width,
                                                    button_no=button_noklik,
                                                    button=button_klik, txt_file = txt_file, text=antwoorden[i].text))

        else:
            b = tk.Button(canvas, image=button_noklik, relief=FLAT, borderwidth=0, highlightthickness=0, bd=0,
                          command=lambda i=i: Click(i, button_klik, vraagnummer, aantal_vragen, correct = False, player = player,
                                                    vragen = vragen, Canvas1 = canvas, text_coordx=text_coordx, text_coordy=text_coordy, root=root,
                                                    full_height = full_height, full_width = full_width, button_no = button_noklik,
                                                    button=button_klik, txt_file = txt_file, text=antwoorden[i].text))

        b.place(x=xcoord, y=ycoord)
        root.update()
        #update root he
        button_x1, button_y1 = b.winfo_rootx(), b.winfo_rooty()


        #Verander locatie van antwoord text
        canvas.create_text(button_x1+80, button_y1, text=text, fill='white', font= onze_font,anchor=NW, tags='mytag')
        root.update()
        buttons.append(b)


    return buttons

def Click(index, button_klik,  vraagnummer, aantal_vragen, correct, player, vragen, Canvas1, text_coordx, text_coordy, root, full_height, full_width, button_no, button, txt_file, text):
    verander_img(index, button_klik, root)
    Click2(vraagnummer, aantal_vragen, correct, player, vragen, Canvas1, text_coordx, text_coordy, root, full_height, full_width, button_no, button, txt_file, text)

def verander_img(index, button_klik, root):
    img = button_klik
    buttons[index].configure(image=img)
    root.update()

def Click2(vraagnummer, aantal_vragen, correct, player, vragen, Canvas1, text_coordx, text_coordy, root, full_height, full_width, button_no, button, txt_file, text):
    string_vraag = str(vraagnummer) + '_tijd'
    if correct:
        player.vraag_goed()
        player.add_bool_antwoord(str(1))
    else:
        player.add_bool_antwoord(str(0))
    df_quiz[string_vraag] = time.time() - df_quiz.loc[df_quiz.index[0], string_vraag]
    player.add_antwoord(text)

    df_quiz[str(vraagnummer)] = correct
    sound_klik = pyglet.media.load('sound_klik.mp3', streaming=False)
    sound_klik.play()
    sound_klik_duration = sound_klik.duration
    time.sleep(sound_klik_duration)
    for item in buttons:
        item.destroy()

    Canvas1.delete('mytag')
    nieuwe_vraag(vraagnummer+1, aantal_vragen, vragen, Canvas1, text_coordy, text_coordx, root, full_height, full_width, button_no, button, player, txt_file)


def nieuwe_vraag(vraagnummer, aantal_vragen, vragen, Canvas1, text_coordy, text_coordx, root, full_height, full_width, button_no, button, player, txt_file):
    #from open_txt import quiz_str as txt_file
    if vraagnummer <= aantal_vragen:
        vraag_1, antwoorden_1 = maak_vraag(vragen, vraagnummer, df_quiz, root)

        plaats_vraag(vraag_1, Canvas1, text_coordx, text_coordy, root)
        buttons = plaats_antwoorden(antwoorden_1, Canvas1, root, full_height, full_width, text_coordx, text_coordy, button_no, button,
                                    player, vraagnummer, aantal_vragen, vragen, txt_file)
        with open("tijdelijke_opslag.txt", "w") as filehandle:
            filehandle.truncate(0)
            filehandle.write(player.bool_antwoorden)
        with open("tijdelijke_opslag_tijd.txt", "w") as filehandle2:
            filehandle2.truncate(0)
            filehandle2.write(str(player.tussen_tijd_berekenen()))
    else:
        df_quiz['antwoorden'] = ""
        df_quiz.loc[0,'antwoorden'] = player.antwoorden
        logging.info(f"{player.naam} is klaar met de quiz, voeg toe aan csv")
        csv_naampje = absolute_pad + '\\losse_csv' + txt_file + "_"+  os.getlogin() + '.csv'
        df_quiz['eind_time'] = time.time()
        df_quiz['tijd_delta'] = df_quiz.loc[df_quiz.index[0], 'eind_time'] - df_quiz.loc[df_quiz.index[0], 'start_time']
        df_quiz['vragen_goed'] = player.vragen_goed
        player.eind_quiz()
        player.total_tijd()
        df = pd.read_csv(csv_naampje)
        if len(df.columns) == 1:
            df = pd.DataFrame(columns = df_quiz.columns)
            df.to_csv(csv_naampje, index = False, encoding = "utf-8")

        list_quiz = df_quiz.values.tolist()[0]

        with open(csv_naampje, 'a', newline='', encoding= "utf-8") as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list_quiz)
            f_object.close()
        root.destroy()















