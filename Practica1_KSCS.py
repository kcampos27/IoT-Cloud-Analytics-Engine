import urllib
import json
import requests
import os
from Prueba_ThingSpeak import onda_rapida

def create_channel():
    global id_channel, write_key
    user_api_key = '3BQCGGFZJQM7S641'

    # --- PASO 1: Chequeo de existencia ---
    print(f"Comprobando si el canal 'kscsCanal' ya existe...")
    list_uri = f'https://api.thingspeak.com/channels.json?api_key={user_api_key}'

    try:
        with open("registro.txt", "r", encoding="utf-8") as f:
            json_reg = json.load(f)
        id_channel = json_reg['id']
        write_key = json_reg['api_keys'][0]['api_key']
        print(f"El canal está almacenado en el registro, su ID es {id_channel} y su write_key es {write_key}")

        resp_lista = requests.get(list_uri)
        if resp_lista.status_code == 200:
            canales = resp_lista.json()
            # Buscamos si algún canal tiene el mismo nombre (ignorando mayúsculas/minúsculas)
            existe = any(canal.get('id') == id_channel for canal in canales)

            if existe:
                print(f"Abortando: El canal ya está almacenado en la API.")
                return  # Salimos de la función
        else:
            print("No se pudo verificar la lista de canales, procediendo con precaución...")

    except FileNotFoundError as e:
        print(f"No se encontro el archivo de registro, se procederá a intentar crear el canal... {e}")
        id_channel = 0
        write_key = 0
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
        return

    # Se envia la peticion HTTP
    uri = 'https://api.thingspeak.com/channels.json'
    metodo = 'POST'
    cabeceras = {'Host': "api.thingspeak.com",
                 'Content-Type': 'application/x-www-form-urlencoded'}
    cuerpo = {'api_key': '3BQCGGFZJQM7S641', #ESTA API KEY ES LA DE LA CUENTA, NO DEL CANAL!!!!!!
              'name': 'kscsCanal',
              'field1': '%CPU',
              'field2': '%RAM'}
    cuerpo_encoded = urllib.parse.urlencode(cuerpo)
    print('Este es el cuerpo del mensaje codificado en UTF8: \n'+cuerpo_encoded+'\n')
    cabeceras['Content-Length'] = str(len(cuerpo_encoded))
    # Se envia la peticion HTTP
    respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo_encoded, allow_redirects=False)

    codigo = respuesta.status_code
    descripcion = respuesta.reason

    print(str(codigo) + " " + descripcion)
    if (codigo == 200):
        print("Canal creado correctamente")
        id_channel = respuesta.json()["id"]
        write_key = respuesta.json()['api_keys'][0]['api_key']
        print(f'El ID del canal es: {id_channel} y el write API key es: {write_key}')
        with open("registro.txt", "w", encoding="utf-8") as archivo:
            archivo.write(respuesta.content.decode("utf-8"))
    else:
        print("Error al crear el canal")

def delete_channel(pId):
    # Se envia la peticion HTTP
    uri = 'https://api.thingspeak.com/channels/'+pId+'.json'
    metodo = 'DELETE'
    cabeceras = {'Host': "api.thingspeak.com",
                 'Content-Type': 'application/x-www-form-urlencoded'}
    cuerpo = {'api_key': '3BQCGGFZJQM7S641'} #ESTA API KEY ES LA DE LA CUENTA, NO DEL CANAL!!!!!!
    cuerpo_encoded = urllib.parse.urlencode(cuerpo)
    print('Este es el cuerpo del mensaje codificado en UTF8: \n'+cuerpo_encoded+'\n')
    cabeceras['Content-Length'] = str(len(cuerpo_encoded))
    # Se envia la peticion HTTP
    respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo_encoded, allow_redirects=False)

    for cabecera in respuesta.headers:
       print(cabecera + ": " + respuesta.headers[cabecera])

    cuerpo_rpta = respuesta.content
    codigo_respuesta = respuesta.status_code
    print("AQUI VEREMOS EL CUERPO DE LA RESPUESTA:\n")
    print(cuerpo_rpta)
    if (codigo_respuesta == 200):
        print("Canal eliminado correctamente")
        os.remove("registro.txt")

    else:
        print("Error al eliminar el canal")

if __name__ == '__main__':
    delete_channel('3257609')
    create_channel()
    onda_rapida(write_key)
