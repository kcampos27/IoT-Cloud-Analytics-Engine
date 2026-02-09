import requests
import math
import time

def prueba_inicial():
    #Se envia la peticion HTTP
    uri = 'https://api.thingspeak.com/update'
    metodo = 'POST'
    cabeceras = {'Host': "api.thingspeak.com",
                 'Content-Type': 'application/x-www-form-urlencoded'}
    cuerpo = {'api_key': 'D4K2RCZANVI1NZTU',
              'field1': '0'}
    #Se envia la peticion HTTP
    respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo)

    for cabecera in respuesta.headers:
        print(cabecera + ": " + respuesta.headers[cabecera])

    cuerpo_rpta = respuesta.content
    print("AQUI VEREMOS EL CUERPO DE LA RESPUESTA:\n")
    print(cuerpo_rpta)
    print("FIN PRUEBA")

def onda_rapida():
    uri = 'https://api.thingspeak.com/update'
    api_key = 'D4K2RCZANVI1NZTU'

    puntos = 10  # Cantidad razonable para no morir de aburrimiento
    print(f"Generando onda corta de {puntos} puntos...")

    for i in range(puntos):
        # Al no dividir i, la onda completa casi un ciclo y medio en 10 pasos
        valor_seno = math.sin(i) * 10

        datos = {
            'api_key': api_key,
            'field1': f"{valor_seno:.2f}"
        }

        try:
            r = requests.post(uri, data=datos)

            if r.text != "0":
                print(f"[{i + 1}/{puntos}] Enviado: {valor_seno:.2f} -> ID: {r.text}")
            else:
                print(f"[{i + 1}/{puntos}] ThingSpeak rechazó el dato (demasiado rápido)")

        except Exception as e:
            print(f"Error: {e}")

        # Pausa obligatoria de seguridad
        if i < puntos - 1:
            time.sleep(16)

    print("\n¡Listo! Revisa tu gráfica en ThingSpeak.")


if __name__ == '__main__':
    onda_rapida()