import random

sibenice = []
slovnik = []
counter = 0
hint_counter = 0

def list_of_words():    #loads words from a .txt document
    with open('slova.txt', encoding='utf-8') as soubor:
        for radek in soubor:
            radek = radek.rstrip()
            slovnik.append(radek)
    return slovnik

def sibenice_loading(): #loads pictures of sibenice, returning list of pictures
    with open('sibenice.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()
    temp = obsah.split("------------------")
    return temp

sibenice = sibenice_loading()   #turning list of pictures into a global list

list_of_words()     

def random_word():  #returning random word from a list of words
    i = random.randrange(1, len(slovnik))
    slovo = slovnik[i - 1]
    return slovo

word = random_word()

def word_len(word):
    list = []
    for letter in word:
        list.append('_')
    return list

unknown_word = word_len(word)

def guessing_the_word(letter):
    a = 0
    for i in word:
        a += 1
        if i == letter:
            unknown_word[a - 1] = letter
   
while True:
    #print(sibenice[counter])
    if "_" in unknown_word:
        letter = input("\nHadej pismeno, ktere se nachazi ve slove\n")
        if len(letter) > 1:
            print('\nZadej jen jedno pismeno!')
        else:
            if letter in unknown_word:
                print('Toto pismenko uz vis...\n Hadej jine')
            else:
                if letter in word:
                    guessing_the_word(letter)
                    
                else:
                    print('\nSpatne pismenko!')
                    hint_counter += 1
                    counter += 1
                if counter < len(sibenice):
                    if hint_counter // 3:
                        hint_counter = 0
                        print("Tady je mala napoveda")
                        while True:
                            hint_index = random.randrange(len(word))
                            letter = word[hint_index]
                            if letter not in unknown_word:
                                guessing_the_word(letter)
                                break
                    print(sibenice[counter])
                else:
                    exit('Prohral jsi!!')

                for i in unknown_word:
                    print(i, end = " ")
                #print('\n', word)
    else:
        exit('\nVyhral jsi!!')

