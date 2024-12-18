import PySimpleGUI as sg
from datetime import date, timedelta

def obtine_zodia_soare(zi, luna):
    if (luna == 3 and zi >= 21) or (luna == 4 and zi <= 19):
        return "Berbec"
    elif (luna == 4 and zi >= 20) or (luna == 5 and zi <= 20):
        return "Taur"
    elif (luna == 5 and zi >= 21) or (luna == 6 and zi <= 20):
        return "Gemeni"
    elif (luna == 6 and zi >= 21) or (luna == 7 and zi <= 22):
        return "Rac"
    elif (luna == 7 and zi >= 23) or (luna == 8 and zi <= 22):
        return "Leu"
    elif (luna == 8 and zi >= 23) or (luna == 9 and zi <= 22):
        return "Fecioara"
    elif (luna == 9 and zi >= 23) or (luna == 10 and zi <= 22):
        return "Balanta"
    elif (luna == 10 and zi >= 23) or (luna == 11 and zi <= 21):
        return "Scorpion"
    elif (luna == 11 and zi >= 22) or (luna == 12 and zi <= 21):
        return "Sagetator"
    elif (luna == 12 and zi >= 22) or (luna == 1 and zi <= 19):
        return "Capricorn"
    elif (luna == 1 and zi >= 20) or (luna == 2 and zi <= 18):
        return "Varsator"
    elif (luna == 2 and zi >= 19) or (luna == 3 and zi <= 20):
        return "Pesti"
    else:
        return "Data invalida"

def nume_luna_in_numar(nume_luna):
    luni = {
        "ianuarie": 1, "februarie": 2, "martie": 3, "aprilie": 4, "mai": 5, "iunie": 6,
        "iulie": 7, "august": 8, "septembrie": 9, "octombrie": 10, "noiembrie": 11, "decembrie": 12
    }
    return luni.get(nume_luna.lower(), "Luna invalida")

def verifica_nume_valid(nume):
    return nume.isalpha()

def calculeaza_varsta(zi, luna, an):
    azi = date.today()
    nastere = date(an, luna, zi)
    varsta = azi.year - nastere.year - ((azi.month, azi.day) < (nastere.month, nastere.day))
    return varsta

def calculeaza_diferenta_varsta(zi1, luna1, an1, zi2, luna2, an2):
    data1 = date(an1, luna1, zi1)
    data2 = date(an2, luna2, zi2)
    if data1 > data2:
        delta = data1 - data2
    else:
        delta = data2 - data1
    ani = delta.days // 365
    luni = (delta.days % 365) // 30
    zile = (delta.days % 365) % 30
    return ani, luni, zile

layout = [
    [sg.Text('Prima persoana', size=(40, 1), justification='center')],
    [sg.Text('Introduceti numele:'), sg.InputText(key='-NUME1-', size=(20, 1))],
    [sg.Text('Introduceti ziua nasterii:'), sg.InputText(key='-ZI1-', size=(5, 1))],
    [sg.Text('Introduceti luna nasterii (numar/nume):'), sg.InputText(key='-LUNA1-', size=(15, 1))],
    [sg.Text('Introduceti anul nasterii:'), sg.InputText(key='-AN1-', size=(10, 1))],
    [sg.HorizontalSeparator()],
    [sg.Text('A doua persoana', size=(40, 1), justification='center')],
    [sg.Text('Introduceti numele:'), sg.InputText(key='-NUME2-', size=(20, 1))],
    [sg.Text('Introduceti ziua nasterii:'), sg.InputText(key='-ZI2-', size=(5, 1))],
    [sg.Text('Introduceti luna nasterii (numar/nume):'), sg.InputText(key='-LUNA2-', size=(15, 1))],
    [sg.Text('Introduceti anul nasterii:'), sg.InputText(key='-AN2-', size=(10, 1))],
    [sg.Button('Afla detalii')],
    [sg.Text('', size=(100, 6), key='-REZULTAT-')]
]

fereastra = sg.Window('Comparatie Astrologica', layout)

while True:
    eveniment, valori = fereastra.read()
    if eveniment == sg.WINDOW_CLOSED:
        break

    if eveniment == 'Afla detalii':
        try:
            nume1 = valori['-NUME1-']
            if not verifica_nume_valid(nume1):
                fereastra['-REZULTAT-'].update('Numele primei persoane trebuie sa contina doar litere.')
                continue
            zi1 = int(valori['-ZI1-'])
            luna_str1 = valori['-LUNA1-']
            an1 = int(valori['-AN1-'])

            if luna_str1.isdigit():
                luna1 = int(luna_str1)
            else:
                luna1 = nume_luna_in_numar(luna_str1)

            if luna1 == "Luna invalida":
                fereastra['-REZULTAT-'].update('Introduceti o luna valida pentru prima persoana.')
                continue

            nume2 = valori['-NUME2-']
            if not verifica_nume_valid(nume2):
                fereastra['-REZULTAT-'].update('Numele celei de-a doua persoane trebuie sa contina doar litere.')
                continue
            zi2 = int(valori['-ZI2-'])
            luna_str2 = valori['-LUNA2-']
            an2 = int(valori['-AN2-'])

            if luna_str2.isdigit():
                luna2 = int(luna_str2)
            else:
                luna2 = nume_luna_in_numar(luna_str2)

            if luna2 == "Luna invalida":
                fereastra['-REZULTAT-'].update('Introduceti o luna valida pentru a doua persoana.')
                continue


            varsta1 = calculeaza_varsta(zi1, luna1, an1)
            varsta2 = calculeaza_varsta(zi2, luna2, an2)
            ani, luni, zile = calculeaza_diferenta_varsta(zi1, luna1, an1, zi2, luna2, an2)

            zodia1 = obtine_zodia_soare(zi1, luna1)
            zodia2 = obtine_zodia_soare(zi2, luna2)

            mesaj_rezultat = (
                f"{nume1} are varsta de {varsta1} ani si semnul zodiacal {zodia1}.\n"
                f"{nume2} are varsta de {varsta2} ani si semnul zodiacal {zodia2}.\n"
                f"Diferenta de varsta intre cele doua persoane este de {ani} ani, {luni} luni si {zile} zile."
            )

            fereastra['-REZULTAT-'].update(mesaj_rezultat)

        except ValueError:
            fereastra['-REZULTAT-'].update('Introduceti date valide.')

fereastra.close()