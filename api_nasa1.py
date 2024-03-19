'''API: Aplication programming Interface
NASA API: https://api.nasa.gov/
API_KEY_NASA: api_key
Developer: Daniela Rivera
Date: 2401224
Script description: Ger data from NASA API about comets

'''

import requests

def get_comet_data(api_key):
    print(":::COMET INFORMATION:::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
    
    try:
        #Realizar solicitud a la API
        response = requests.ger(url)
        response.raise_for_status() # => valida si se presenta algun error en la peticion
        #convertir la respuesta a formato JSON(JS Object Notation)
        datos = response.json()

        print(datos)
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la peticion a la API de NASA: {e}")


api_key_nasa= '7BBKZ4131BYwiHRsFxmE2CiibLqFg4bvoEhwH5nw'
get_comet_data(api_key_nasa)