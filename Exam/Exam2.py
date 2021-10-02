def encrypt():
    import string
    plainText = (input("what is your plaintext? ")).lower()
    shift_encrypt = (input("What is your shift? ")).lower()

    dictText = {}
    # tạo ra dict {from a -> b: from 0 -> 25}
    for i in range(26):
        dictText[string.ascii_lowercase[i]] = i

    # get key tương ứng với shift_encrypt user enter.
    key = [dictText.get(i) for i in shift_encrypt]

    cipherText = ""
    i = 0
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + key[i]
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            i += 1
            if i == len(key):
                i -= len(key)
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
    print("Your ciphertext is: ", cipherText, "with a shif of", shift_encrypt)

def decrypt():
    import string         
    encryption = (input("Enter in your encryted code")).lower()
    shift_encrypt = (input("What is your encryption shift? ")).lower()

    dictText = {}
    # tạo ra dict {from a -> b: from 0 -> 25}
    for i in range(26):
        dictText[string.ascii_lowercase[i]] = i

    # get key tương ứng với shift_encrypt user enter.
    key = [dictText.get(i) for i in shift_encrypt]

    cipherText = ''
    i = 0
    for ci in encryption:
        if ci.isalpha():
            stayInAlphabet_de = ord(ci) - key[i]
            if stayInAlphabet_de < ord('a'):
                stayInAlphabet_de += 26
            i += 1
            if i == len(key):
                i -= len(key)
            finalLetter_decrypte = chr(stayInAlphabet_de)
            cipherText += finalLetter_decrypte
    print("Your ciphertext is: ", cipherText, "with negative shift of", shift_encrypt)



from tkinter import*
option = Tk()
option.title = ("Option")
option.geometry("300x300")

myLaber1 = Label(option, text="Hello Guys, How are you today!")
myLaber1.pack()


button1 = Button(option,text="encrypt",command=encrypt)
button1.pack()

button2 = Button(option, text = "decrypt", command = decrypt)
button2.pack()

button3 = Button(option,text="exit",command=exit)
button3.pack()

option.mainloop()