'''
script description: Get all data about
'''

import requests
import os 
os.system('clear')

def get_comets(): 
    global count
    print ("::: COMETS INFORMATION :::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try: 
        #Request to API
        response = requests.get(url)
        response.raise_for_status()

        #Convertir la respuesta a dormato JSON
        data = response.json()
        #print all comets names 

        count = 0

        print(":::SOLAR SYSTEM MENU:::")
        print("[1].Planets")
        print("[2].Moons")
        print("[3].Stars")
        print("[4].Asteroid")
        print("[5].Comets")
        opt = int(input ("Escoge una opcion"))

        if opt ==1:
            body_type = "Planet"
        elif opt ==2:
            body_type = "Moon"
        elif opt ==3:
            body_type = "Star"
        elif opt ==4:
            body_type = "Asteroid"
        elif opt ==5:
            body_type = "Comet"
        else:
            print ("::: Invalid option:::")

        total = int(input("Cantidad de datos a mostrar:"))
        


        for comet in data ["bodies"]:

            #if comet["isPlanet"]== True:
            if comet ["bodyType"] == body_type:
            

                print("English name: ", comet["englishName"])
                print("Moons:", comet ["moons"])
                print("Gravity:", comet ["gravity"])
                print("Is planet?:", comet ["isPlanet"])
                print("Body_type:", comet ["bodytype"])
                print ("\n") 

                count = count + 1
            if count == total :
                break
            print (count)







    except requests.exceptions.RequestException as e:
        print (f"API error: {e}")



#llamar funcion
get_comets()
