#Questão_5
def invert_word(word):
    lst_letras = []
    for i in range(len(word)-1,-1,-1):
        lst_letras.append(word[i])
    new_word = ''.join(lst_letras)
    return new_word
print(invert_word('Caíque'))
#Output: euqíaC