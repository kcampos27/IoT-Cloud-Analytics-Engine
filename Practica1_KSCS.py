import urllib

import requests
def create_channel(name):
    user_api_key = '3BQCGGFZJQM7S641'

    # --- PASO 1: Chequeo de existencia ---
    print(f"Comprobando si el canal '{name}' ya existe...")
    list_uri = f'https://api.thingspeak.com/channels.json?api_key={user_api_key}'

    try:
        resp_lista = requests.get(list_uri)
        if resp_lista.status_code == 200:
            canales = resp_lista.json()
            # Buscamos si algún canal tiene el mismo nombre (ignorando mayúsculas/minúsculas)
            existe = any(canal.get('name').lower() == name.lower() for canal in canales)

            if existe:
                print(f"Abortando: Ya tienes un canal llamado '{name}'.")
                return  # Salimos de la función
        else:
            print("No se pudo verificar la lista de canales, procediendo con precaución...")
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
        return

    # Se envia la peticion HTTP
    uri = 'https://api.thingspeak.com/channels.json'
    metodo = 'POST'
    cabeceras = {'Host': "api.thingspeak.com",
                 'Content-Type': 'application/x-www-form-urlencoded'}
    cuerpo = {'api_key': '3BQCGGFZJQM7S641', #ESTA API KEY ES LA DE LA CUENTA, NO DEL CANAL!!!!!!
              'name': name,
              'field1': '%CPU',
              'field2': '%RAM'}
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
        print("Canal creado correctamente")
    else:
        print("Error al crear el canal")

def delete_channel(id_channel):
    # Se envia la peticion HTTP
    uri = 'https://api.thingspeak.com/channels/'+id_channel+'.json'
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
    else:
        print("Error al eliminar el canal")

if __name__ == '__main__':
    create_channel('kscsCanal')
