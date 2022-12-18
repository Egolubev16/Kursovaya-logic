from chempy.util import periodic

def callback(event):
    textline.configure(state='normal')
    if change() != None:
        textline.replace(1.0, END, change())
    else:
        print('Подходящих реакций не найдено')
        textline.delete('1.0', END)
        textline.insert('1.0', 'Подходящих реакций не найдено')
    textline.configure(state='disabled')

def change():
    one_symb = {'F', 'C', 'H', 'O', 'B', 'N', 'S', 'P', 'K', 'I', 'U', 'W', 'Y', 'V'}
    reactions = []
    mylines = []
    with open('Reactions.txt', 'r') as myfile:
        for myline in myfile:
            mylines.append(myline.rstrip('\n'))
    result = None
    element = comboExample.get()
    for line in mylines:
        index = line.find(element)
        while index != -1:
            if element in one_symb:
                if line[index+1].islower() != True:
                    reactions.append(line)
                    result = '\n'.join(reactions)
                    break
            else:
                reactions.append(line)
                result = '\n'.join(reactions)
                break
            index = line.find(element, index + 1)
    return result



def btn_click():
    f = open('Reactions.txt', 'a+')
    f.write(entry_n1.get() + '\n')
    f.close()

def btn_click1():
    textline.configure(state='normal')
    textline.replace(1.0, END, show())

def show():
    mylines = []
    with open('Reactions.txt', 'r') as myfile:
        for myline in myfile:
            mylines.append(myline.rstrip('\n'))
            result = '\n'.join(mylines)
        return result

def write_elements():
    chemicals_list = []
    n = 117
    for i in range(0, n + 1):
        chemicals_list.append(periodic.symbols[i])
    chemicals_list.append('Все реакции')
    return chemicals_list

def changeelement():
    chemicals_list = write_elements()
    comboExample['values'] = chemicals_list