# Créer une fonction qui permet de voir si un mot peut se lire dans les deux sens

punctuations = """!()-[]{};:'"\\,<>./?@#$%^&*_~"""


def palindrome(text):
    word = text.replace(" ", "").lower()
    word_clean = ""

    for letter in word:
        if letter not in punctuations:
            word_clean += letter

    if word_clean == word_clean[::-1]:
        print(f"PALINDROME")
    else:
        print("Rien à signaler !")


# NE PAS TOUCHER ============================================
palindrome("A Cuba, Anna a bu ca :)")  # PALINDROME
palindrome("02/02/2020")  # PALINDROME
palindrome("Borrow or rob?")  # PALINDROME
palindrome("Bon sport, trop snob ?")  # PALINDROME
palindrome("Reussir a Paris : suer !!!")  # PALINDROME
palindrome("Hello allo")  # Rien à signaler !
# ===========================================================
