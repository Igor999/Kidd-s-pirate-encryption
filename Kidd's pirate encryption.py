#Шифрование пирата Кидда своими руками
#Реализуйте функцию шифрования, которую использовал пират Кидд из рассказа Эдгара Аллана По "Золотой жук".
#
#Используйте словарь:
def kidds_encryption(text, reverse=False):
    letter = ['e','t','h','o','s','n','a','i','r','f','d','l','m','b','y','g','u','v','c','p']
    symbols = ['8',';','4','‡',')','*','5','6','(','1','†','0','9','2',':','3','?','¶','-','.']
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = alphabet.lower()
    new_text = ""
    result = ""
    if reverse == False:
        text = text.lower()
        for i in text:
            if i in alphabet:
                new_text +=i
        for i in new_text:
            if i in letter:
                ind = letter.index(i)
                result+=symbols[ind]
            else:
                result+=""
    elif reverse == True:
        for i in text:
            ind = symbols.index(i)
            result+=letter[ind]
    return result
