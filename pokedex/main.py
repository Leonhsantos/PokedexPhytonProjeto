from tkinter import*
from tkinter import ttk

# pillow
from PIL import Image, ImageTk

from dados import * 
##################### cores ############
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

#  criando janela

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")


# criando o frame

frame_pokemon = Frame(janela, width=550, height=290, relief= "flat")
frame_pokemon.grid(row=1, column=0)



# função trocar pokemon
def trocar_pok(i): 
    global imagem_pokemon, pok_imagem 

    # cor frame pokemon troca
    frame_pokemon['bg'] = pokemon[i] ['Tipo'] [3] 



    # func: detalhes pokemons
    pok_nome['text']= i 
    pok_nome['bg']= pokemon[i] ['Tipo'] [3] 
    pok_tipo['text']= pokemon[i] ['Tipo'] [1]
    pok_tipo['bg']= pokemon[i] ['Tipo'] [3] 
    pok_id['text'] = pokemon[i] ['Tipo'] [0]
    pok_id['bg']= pokemon[i] ['Tipo'] [3] 

    imagem_pokemon = pokemon[i] ['Tipo'] [2]

    # Imagem pokemon
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)


    pok_imagem= Label(frame_pokemon, image=imagem_pokemon, relief="flat", bg=pokemon[i] ['Tipo'] [3], fg=co1)
    pok_imagem.place(x=60, y=50)


    pok_tipo.lift() 

    # pokemon status func
    pok_hp['text'] = pokemon[i] ['Status'] [0]
    pok_attack['text'] = pokemon[i] ['Status'] [1]
    pok_defense['text'] = pokemon[i] ['Status'] [2]
    pok_speed['text'] = pokemon[i] ['Status'] [3]
    pok_total['text'] = pokemon[i] ['Status'] [4]


    # pokemon skill func
    pok_skill_1['text'] = pokemon[i] ['Skills'] [0]
    pok_skill_2['text'] = pokemon[i] ['Skills'] [1]

# nome
pok_nome= Label(frame_pokemon, text='', relief="flat", anchor= CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)

# tipo do pokemon
pok_tipo= Label(frame_pokemon, text='', relief="flat", anchor= CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

# ID do pokemon
pok_id= Label(frame_pokemon, text='', relief="flat", anchor= CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)





# status
pok_status= Label(janela, text='Status', relief="flat", anchor= CENTER, font=('Fixedsys  20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)


# HP
pok_hp= Label(janela, text='HP: 300', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

# Ataque
pok_attack= Label(janela, text='Attack: 600', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_attack.place(x=15, y=385)

# Defesa
pok_defense= Label(janela, text='Defense: 200', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_defense.place(x=15, y=410)

# Velocidade
pok_speed= Label(janela, text='Speed: 450', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_speed.place(x=15, y=435)

# Total
pok_total= Label(janela, text='Total: 300', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)



# Habilidades
pok_skills= Label(janela, text='Skills', relief="flat", anchor= CENTER, font=('Fixedsys  20'), bg=co1, fg=co0)
pok_skills.place(x=180, y=310)


# Skill-1
pok_skill_1= Label(janela, text='Thunder Shock', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_skill_1.place(x=185, y=360)

# Skill-2
pok_skill_2= Label(janela, text='Quick Attack', relief="flat", anchor= CENTER, font=('Ivy  10 bold italic'), bg=co1, fg=co4)
pok_skill_2.place(x=185, y=385)




# Criando botões para  pokemons
# Imagem pokemon_1
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1= Button(janela,command=lambda:trocar_pok('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width= 150, relief="raised", overrelief=RIDGE, compound=LEFT, anchor= NW, padx=5, font=('Fixedsys 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

# Imagem pokemon_2
imagem_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2= Button(janela,command=lambda:trocar_pok('Bulbasaur'), image=imagem_pokemon_2, text='Bulbasaur', width= 150, relief="raised", overrelief=RIDGE, compound=LEFT, anchor= NW, padx=5, font=('Fixedsys 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)

# Imagem pokemon_3
imagem_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3= Button(janela,command=lambda: trocar_pok('Charmander'), image=imagem_pokemon_3, text='Charmander', width= 150, relief="raised", overrelief=RIDGE, compound=LEFT, anchor= NW, padx=5, font=('Fixedsys 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

# Imagem p('')okemon_4
imagem_pokemon_4 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4= Button(janela,command=lambda: trocar_pok('Gyarados'),image=imagem_pokemon_4, text='Gyrados', width= 150, relief="raised", overrelief=RIDGE, compound=LEFT, anchor= NW, padx=5, font=('Fixedsys 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

# Imagem pokemon_5
imagem_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((50, 50))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5= Button(janela,command=lambda: trocar_pok('Gengar'),image=imagem_pokemon_5, text='Gengar', width= 150, relief="raised", overrelief=RIDGE, compound=LEFT, anchor= NW, padx=5, font=('Fixedsys 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)



import random
lista_pokemon = ['Pikachu', 'Bulbasaur', 'Gengar', 'Gyarados', 'Charmander']


pokemon_escolhido =  random.sample(lista_pokemon, 1)
trocar_pok(pokemon_escolhido[0])






















janela.mainloop()