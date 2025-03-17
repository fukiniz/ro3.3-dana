from random import choice

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

max_wrong = len(HANGMAN)
WORDS = ('питон', 'игра', 'программирование')

word = choice(WORDS)
so_far = '_' * len(word)
wrong = 0
used = []

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])
    print('\nВы использовали следующие буквы:\n', used)
    print('\nНа данный момент слово выглядит вот так:\n', so_far)

    guess = input('\nВведите своё предположение: ')

    while guess in used:
        print('Вы уже угадали букву', guess)
        guess = input('Введите своё предположение: ')

    used.append(guess)

    if guess in word:
        print('\nДа! \'' + guess + '\' есть в слове!')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('\nИзвините, буквы \'' + guess + '\' нет в слове.')
        wrong += 1

if wrong == max_wrong:
    print(HANGMAN[wrong])
    print('\nТебя повесили!')
else:
    print('\nВы угадали слово!')

print('\nЗагаданное слово было \'' + word + '\'')
