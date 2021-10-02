
# st = "hello world"
# encode = ''
# for i in st:
#     encode_b = 

def encrypt():
    plainText = input("What is your plaintext? ")
    shift = int(input("What is your shift? "))
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            print(stayInAlphabet)
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
            print(stayInAlphabet,"****")
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter

    print ("Your ciphertext is: ", cipherText,"with a shift of",shift)


def decrypte():
    encryption=input("enter in your encrypted code")
    encryption_shift=int(input("enter in your encryption shift"))

    cipherText1 = ""
    for c in encryption:
        if c.isalpha():
            stayInAlphabet1 = ord(c) - encryption_shift
        if stayInAlphabet1 > ord('z'):
            stayInAlphabet1 += 26
        finalLetter1 = chr(stayInAlphabet1)
        cipherText1 += finalLetter1

    print ("Your ciphertext is: ", cipherText1,"with negative shift of",encryption_shift)

from tkinter import *

menu=Tk()
menu.title("menu")
menu.geometry("300x300")
button1= Button(menu,text="encrypt",command=encrypt)
button1.pack()

button2= Button(menu,text="decrypt",command=decrypte)
button2.pack()

button3= Button(menu,text="exit",command=exit)
button3.pack()

menu.mainloop()