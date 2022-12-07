import tkinter
from tkinter import ttk

def seleccion(numero):
    print('hola')
    print(numero)
    animales = {0:'perro'}
    
    


window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(4, weight=4)
label_title = tkinter.Label(window, text='¿Qué mascotas tienes?')
label_title.grid(column=1, row=0, sticky=tkinter.W)

seleccionado_perro = tkinter.IntVar()
seleccionado_gato = tkinter.BooleanVar()
seleccionado_peces = tkinter.BooleanVar()
seleccionado_serpiente = tkinter.BooleanVar()
seleccionado_pajaro = tkinter.BooleanVar()
seleccionado_dragon = tkinter.BooleanVar()
seleccionado_hamster = tkinter.BooleanVar()
seleccionado_pokemon = tkinter.BooleanVar()
seleccionado_tarantula = tkinter.BooleanVar()

checkbox_perro = tkinter.Checkbutton(window, text='Perro', variable=seleccionado_perro,onvalue = 1, command=seleccion(seleccionado_perro))
checkbox_perro.grid(column=1, row=1, sticky=tkinter.W)
checkbox_gato = tkinter.Checkbutton(window, text='Gato', variable=seleccionado_gato)
checkbox_gato.grid(column=2, row=1, sticky=tkinter.W)
checkbox_peces = tkinter.Checkbutton(window, text='Peces', variable=seleccionado_peces)
checkbox_peces.grid(column=3, row=1, sticky=tkinter.W)
checkbox_serpiente = tkinter.Checkbutton(window, text='Serpiente', variable=seleccionado_serpiente)
checkbox_serpiente.grid(column=1, row=2, sticky=tkinter.W)
checkbox_pajaro = tkinter.Checkbutton(window, text='Pájaro', variable=seleccionado_pajaro)
checkbox_pajaro.grid(column=2, row=2, sticky=tkinter.W)
checkbox_dragon = tkinter.Checkbutton(window, text='Dragón', variable=seleccionado_dragon)
checkbox_dragon.grid(column=3, row=2, sticky=tkinter.W)
checkbox_hamster = tkinter.Checkbutton(window, text='Hamster', variable=seleccionado_hamster)
checkbox_hamster.grid(column=1, row=3, sticky=tkinter.W)
checkbox_pokemon = tkinter.Checkbutton(window, text='Pokemon', variable=seleccionado_pokemon)
checkbox_pokemon.grid(column=2, row=3, sticky=tkinter.W)
checkbox_tarantula = tkinter.Checkbutton(window, text='Tarántula', variable=seleccionado_tarantula)
checkbox_tarantula.grid(column=3, row=3, sticky=tkinter.W)

aceptar_button = tkinter.Button(window, text='Aceptar')
aceptar_button.grid(column=3, row=4, sticky=tkinter.E)

window.mainloop()
