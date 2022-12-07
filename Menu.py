# Problema 1: Menu 
import os
os.system ("cls")
opcion=int(input("Menu de recomendaciones \n"+
                 "1. Literatura \n"+
                 "2. Cine \n"+
                 "3. Musica \n"+
                 "4. Videojuegos \n"+
                 "5. Salir \n"+ 
                 "Eliga una opcion :) \n"))
while opcion <=5:
    if opcion==1:
        print(input("Lecturas recomendables: \n"+
                    "+Esperandolo a Tito y otros cuentos de futbol (Eduardo Sacheri) \n"+
                    "+El juego de Ender (Orson Scott Card) \n"+
                    "+El sueño de los héroes (Adolfo Bioy Casares) \n"))
    elif opcion==2:
        print(input("Peliculas recomendables: \n"+
                    "+Matrix (1999) \n"+
                    "+El último samuray (2003) \n"+
                    "+Cars (2006) \n"))
    elif opcion==3:
        print(input("Discos recomendables: \n"+
                    "+Despedazado por mil partes (La Renga, 1996) \n"+
                    "+Bufalo (La Mississippi, 2008)) \n"+
                    "+Gaia (Mägo de Oz, 2003) \n"))
    elif opcion==4:
        print(input("Videojuegos clasicos recomendables: \n"+
                    "+Dia del tentáculo (LucasArts, 1993) \n"+
                    "+Terminal Velocity (Terminal Reality/3D Realms, 1995 \n"+
                    "+Death Rally (Remedy/Apogee, 1996) \n"))
    elif opcion==5:
        print(input("Gracias vuelva pronto"))
    else:
        print(input("Opcion no valida"))
    
    os.system ("cls")
    opcion=int(input("Menu de recomendaciones \n"+
                 "1. Literatura \n"+
                 "2. Cine \n"+
                 "3. Musica \n"+
                 "4. Videojuegos \n"+
                 "5. Salir \n"+ 
                 "Eliga una opcion :) \n"))