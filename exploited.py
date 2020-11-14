import os
import matplotlib
import matplotlib.pyplot as plt
from termcolor import colored
import time
import pygame
pygame.init()

filelist = os.listdir(os.path.dirname(__file__))

counter = 0

wn = pygame.display.set_mode((750, 500))

pygame.display.set_caption("Aoth Compiler")

The_icon = pygame.image.load("8kxAuY-H-uM1Y6z7CY6ojIPFsBRAGFDUbpBdJhqHEr6Fr6DU.png")

pygame.display.set_icon(The_icon)

run = True

arr = []

for file in filelist:
    if file[-5:] == ".aoth":
        arr.append(file)


FONT = pygame.font.Font("freesansbold.ttf", 64)

TheFile = ""

chars2 = []
chars1 = []

vars2 = []
vars1 = []
var1 = []


def draw_buttons():
    global TheFile
    global run
    c = 0
    arr2 = []
    for i in range(len(arr)):
        pygame.draw.rect(wn, (150, 150, 150), (0, 80 + c, 300, 100))
        text0 = FONT.render(arr[i][:-5], True, (0, 0, 0))
        wn.blit(text0, (30, 80 + c + 10))
        arr2.append([0, 80 + c, 300, 80 + c + 100])
        c += 150

        if click[0] == 1:
            if arr2[i][0] <= mouse[0] <= arr2[i][2] and arr2[i][1] <= mouse[1] <= arr2[i][3]:
                TheFile = arr[i]
                run = False


chars3 = []
vars3 = []

while run:
    pygame.time.delay(10)

    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    wn.fill((0, 0, 120))
    draw_buttons()
    pygame.display.update()
pygame.quit()

can_compile = True

can_show_result = False

waiting_to_get_value = False

with_table = False

vars5 = []

vars5_r = []

vars4 = []

vars3_0 = ""

vars3_1 = ""

var1_0 = ""

var1_1 = ""

v_c = 0

v_c2 = 0

vars3s = []

vars3s2 = []

ful = []

clone_vars2 = []

clone_vars3 = []

if TheFile:
    run_file = open(TheFile, 'r')

    file_lines = run_file.readlines()
    for i in range(len(file_lines)):
        if file_lines[i][: 5] == "vars:":
            vars1 = file_lines[i][5:].strip("\n").split(" ")
            vars1.remove("")
        elif file_lines[i][: 8] == "strings:":
            chars1 = file_lines[i][8:].strip("\n").split(" ")
            chars1.remove("")
        elif file_lines[i][: 5] == "STTV:":
            vars4 = file_lines[i][5:].strip("\n").split(" ")
            vars4.remove("")
            if len(vars4) == 2:
                can_show_result = True
            else:
                can_compile = False
                print(colored("STTV can take only 2 variables.", "red"))
            if (vars4[0] not in vars1) or (vars4[1] not in vars1):
                print(colored("Error!", 'red'))
                can_compile = False
        elif file_lines[i][: 6] == "table:":
            vars5 = file_lines[i][6:].strip("\n").split(" ")
            vars5.remove("")
            with_table = True
        elif file_lines[i][0] == "(" and ")" in file_lines[i]:
            if file_lines[i][1: file_lines[i].find(")")] in vars1:
                vars2 = file_lines[i][file_lines[i].find(":") + 1:].strip("\n").split(" ")
                clone_vars2 = file_lines[i][file_lines[i].find(":") + 1:].strip("\n").split(" ")
                vars2.remove("")
                for v in range(len(vars2)):
                    if vars2[v].isnumeric():
                        vars2[v] = float(vars2[v])
                        clone_vars2[v] = float(vars2[v])
                        if waiting_to_get_value:
                            vars2[0] = vars2[v]
                            waiting_to_get_value = False
                    elif vars2[v] == "in":
                        try:
                            vars2[v] = float(input("$"))
                            clone_vars2[v] = vars2[v]
                            if waiting_to_get_value:
                                vars2[0] = vars2[v]
                                waiting_to_get_value = False
                        except:
                            print(colored("Value Error!", 'red'))
                            can_compile = False
                    elif vars2[v][0] == "-" and vars2[v][1:].isnumeric():
                        vars2[v] = float(vars2[v])
                        clone_vars2[v] = vars2[v]
                        if waiting_to_get_value:
                            vars2[0] = vars2[v]
                            waiting_to_get_value = False
                    elif ("." in vars2[v]) and vars2[v].count(".") == 1 and (vars2[v][:vars2[v].find(".")] + vars2[v][vars2[v].find(".") + 1 :]).isnumeric():
                        vars2[v] = float(vars2[v])
                        clone_vars2[v] = vars2[v]
                        if waiting_to_get_value:
                            vars2[0] = vars2[v]
                            waiting_to_get_value = False
                    elif vars2[v] == "un" and (v == 0 or v == len(vars2) - 1):
                        if v == 0:
                            waiting_to_get_value = True
                            clone_vars2[v] = "---"
                        else:
                            clone_vars2[v] = "---"
                            vars2[v] = vars2[v - 1]
                    else:
                        can_compile = False
                        print(colored("Value Error!", 'red'))
                clone_vars3.append(clone_vars2)
                vars3.append(vars2)
                var1.append(file_lines[i][1: file_lines[i].find(")")])
            elif file_lines[i][1: file_lines[i].find(")")] in chars1:
                chars2 = file_lines[i][file_lines[i].find(":") + 1:].strip("\n").split(" ")
                chars2.remove("")
                vars3.append(chars2)
                var1.append(file_lines[i][1: file_lines[i].find(")")])
            else:
                can_compile = False
                print(colored("Error: There's no " + file_lines[i][1: file_lines[i].find(")")] + " in variables.", 'red'))
    if can_compile:
        if with_table:
            file2 = open("table.py", 'r')
            file2 = file2.read()
            for i in range(len(var1)):
                for j in range(len(vars5)):
                    if vars5[j] == var1[i]:
                        vars5_r.append(vars5[j])
                        for k in range(len(vars3[i])):
                            if (var1[i] in vars1) and (clone_vars3[i][k] != "---"):
                                if vars3[i][k] - int(vars3[i][k]) == 0:
                                    clone_vars3[i][k] = int(vars3[i][k])
                        vars3s.append(clone_vars3[i])
                        
            vars3s2.append(vars5_r)
            for i in range(len(vars3s[0])):
                for j in range(len(vars3s)):
                    ful.append(vars3s[j][i])
                vars3s2.append(ful)
                ful = []
            file3 = file2.replace("pygame.display.set_caption(\"table\")", "pygame.display.set_caption(\"" + TheFile[:-5] + "\")").replace("Table = []", "Table = " + str(vars3s2))
            filex = open('table.py', 'w')
            filex.write(file3)
            filex.close()
            os.system("start table.py")
            time.sleep(10)
            filex = open('table.py', 'w')
            filex.write(file2)
            filex.close()
        if can_show_result:
            for i in range(len(var1)):
                for j in range(len(vars4)):
                    if vars4[j] == var1[i]:
                        if v_c == 0:
                            vars3_0 = vars3[i]
                            var1_0 = var1[i]
                            v_c += 1
                        elif v_c == 1:
                            vars3_1 = vars3[i]
                            var1_1 = var1[i]
                            v_c += 1
            if var1_0 and var1_1:
                matplotlib.rcParams['toolbar'] = 'None'
                fig = plt.figure(0)
                thismanager = plt.get_current_fig_manager()
                thismanager.window.wm_iconbitmap("hnet.com-image.ico")
                fig.canvas.set_window_title(TheFile[:-5])
                plt.plot(vars3_0, vars3_1)
                plt.xlabel(var1_0)
                plt.ylabel(var1_1)
                plt.show()
            else:
                print(colored("Error!", 'red'))
