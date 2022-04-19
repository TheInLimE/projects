import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("Help documentation Gui")
window.geometry('690x220')
window.configure(bg='grey10')
btn = tkinter.Label(window, text = "Modded server info")
text1 = tkinter.Label (window, text="MODDED")
text2 = tkinter.Label (window, text=" MAIN SERVER")
text3 = tkinter.Label (window, text="  DISCORD")
text4 = tkinter.Label (window, text="  UNIQUE BOTS")
text5 = tkinter.Label (window, text="    Copyright 2022, TheInLimE, All rights reserved.")
#modded server definitions
def click():
    btn0.configure(text = "                      Ip                      ")
    tkinter.messagebox.showinfo('The modded server ip', 'The modded server ip is51.254.243.85:25577')

def click1():
    btn1.configure(text = "                  Version                 ")
    tkinter.messagebox.showinfo('Modded server version', 'The modded server is in 1.12.2 forge')

def click2():
    btn2.configure(text = "Crossplay, and cracked info")
    tkinter.messagebox.showinfo('Info about crossplay/cracked', 'We unfortunately require you to own mc since no plugin'
                                                                'support and there fore no geyser either')
#Main server defitions
def click3():
    btn3.configure(text = "                      Ip                      ")
    tkinter.messagebox.showinfo('The main server ip', 'The main server domain is mc.theincraft.live for java, and for'
                                                      'bedrock players ip = 176.31.135.122 port = 25589')

def click4():
    btn4.configure(text = "                  Version                 ")
    tkinter.messagebox.showinfo('The main server version', 'The server is hosted on 1.18, but you can join with any '
                                                           'version between 1.8 and 1.18.2')

def click5():
    btn5.configure(text = "Crossplay, and cracked info")
    tkinter.messagebox.showinfo('Crossplay and crack info', 'The Main server allows bedrock/cracked players to join'
                                                            ' aswell')
#Discord definitions
def click6():
    btn6.configure(text = "                   Sans bot                   ")
    tkinter.messagebox.showinfo('Sans bot list of commands', '/mcinfo '
                                                             '/megalovania '
                                                             '/humerus '
                                                             '/fortnite '
                                                             '/sex '
                                                             '/necro '
                                                             '/bone '
                                                             '/suffer '
                                                             '/pickupline '
                                                             '/help '
                                                             '/up-sans '
                                                             '/summon-3d_sans_bossfight '
                                                             '/sexytime '
                                                             '/rps ')

def click7():
    btn7.configure(text = "                  Giga chad                 ")
    tkinter.messagebox.showinfo('Giga chads only command', 'Do /nsfw for some buttons to press for nsfw images')

#Modded server buttons
btn0 = tkinter.Button(window, text = "                      Ip                      ", command = click)

btn1 = tkinter.Button(window, text = "                  Version                 ", command = click1)

btn2 = tkinter.Button(window, text = "Crossplay, and cracked info", command = click2)
#Main server buttons
btn3 = tkinter.Button(window, text = "                      Ip                      ", command = click3)

btn4 = tkinter.Button(window, text = "                  Version                 ", command = click4)

btn5 = tkinter.Button(window, text = "Crossplay, and cracked info", command = click5)
#Discord server buttons
btn6 = tkinter.Button(window, text = "                   Sans bot                   ", command = click6)

btn7 = tkinter.Button(window, text = "                  Giga chad                 ", command = click4)


#fonts
Font0 = ("Arial", 20, "bold")
font1 = ("Arial", 20, "bold")
font2 = ("Arial", 15, "bold")
#Text configuration
text1.configure(font = Font0, foreground="Red2", background="grey10")
text2.configure(font = Font0, foreground="LimeGreen", background="grey10")
text3.configure(font = font1, foreground="RoyalBlue", background="grey10")
text4.configure(font = font2, background="grey10", foreground="RoyalBlue")
text5.configure(foreground="white", background="grey10")
#modded
text1.grid(column=0, row=0)
btn2.grid(column=0, row=1)
btn1.grid(column=0, row=2)
btn0.grid(column=0, row=3)
btn0.configure(bg='grey25')
btn1.configure(bg='grey25')
btn2.configure(bg='grey25')
#main server
text2.grid(column=9, row=0)
btn3.grid(column=9, row=3)
btn4.grid(column=9, row=2)
btn5.grid(column=9, row=1)
btn3.configure(bg='grey25')
btn4.configure(bg='grey25')
btn5.configure(bg='grey25')
#Discord server
text3.grid(column=15, row=0)
text4.grid(column=15, row=1)
btn6.grid(column=15, row=2)
btn7.grid(column=15, row=3)
btn6.configure(bg='grey25')
btn7.configure(bg='grey25')
#misc
text5.grid(column=0, row=40)
window.mainloop()