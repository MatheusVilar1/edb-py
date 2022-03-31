# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

card1 = [1, 3, 5, 7, 9, 11, 13, 15]
card2 = [2, 3, 6, 7, 10, 11, 14, 15]
card3 = [4, 5, 6, 7, 12, 13, 14, 15]
card4 = [8, 9, 10, 11, 12, 13, 14, 15]

def print_ask(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def advinhar():
    resultado = 0

    r1 = input(f'O numero está aqui? (S/N) -> {card1}')
    if r1.upper() == "S":
        resultado = resultado + 1

    r2 = input(f'O numero está aqui? (S/N) -> {card2}')
    if r2.upper() == "S":
        resultado = resultado + 2

    r3 = input(f'O numero está aqui? (S/N) -> {card3}')
    if r3.upper() == "S":
        resultado = resultado + 4

    r4 = input(f'O numero está aqui? (S/N) -> {card4}')
    if r4.upper() == "S":
        resultado = resultado + 8

    print(f'Você pensou no número: {resultado}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_ask('Pense em um número entre 1 e 15...')

    ja_pensou = input('E ai, já pensou? (S/N) ')

    if ja_pensou.upper() != "S":
        print('Pois ande logo!')
    else:
        print('Não vai esquecer o número...')

    advinhar()

    correto = input(f'Acertei? (S/N)')
    if correto.upper() == "S":
        print('Eu sou demais!!! ;-)')
