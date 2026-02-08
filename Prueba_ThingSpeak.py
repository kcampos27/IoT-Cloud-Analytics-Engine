import requests
def funcion():
    #Se envia la peticion HTTP
    cabeceras = {'Host ': "pi.thingspeak.com",
                 'Content‐Type': 'application/x‐www‐form‐urlencoded'}
    cuerpo = "api_key=D4K2RCZANVI1NZTU"

    #Se envia la peticion HTTP
    respuesta= requests.request(metodo, uri, headers=cabeceras, data=cuerpo)

    #Codigo de estado HTTP
    codigo= respuesta.status_code
    #Texto descriptivo del codigo
    descripcion= respuesta.reason

    print(str(codigo) + " " + descripcion)

    #Recorrer e imprimir todas las cabeceras de la respuesta
    for cabecera in respuesta.headers:
        print(cabecera + ": " + respuesta.headers[cabecera])
