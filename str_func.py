def capslock_function():
    '''Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами__'''
    word = input()
    capslock_word = word.upper()
    print(capslock_word)


def title_function():
    '''Функция, которая принимает на вход строку и возвращает ее с первой заглавной буквой'''
    word = input()
    title_word = word.title()
    print(title_word)


capslock_function()
title_function()
