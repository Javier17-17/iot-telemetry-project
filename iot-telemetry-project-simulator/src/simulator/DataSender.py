import requests

class DataSender:

    _url = "http://127.0.0.1:8000/telemetry/"

    @staticmethod
    def send_data(data):

        try:
            print("aaa")
            response = requests.post(DataSender._url, json = data)
            print("petición enviada correctamente")
        except Exception as e:
            print("Error al crear la petición")


        if response.status_code == 200:
            print("Datos enviados correctamente: ")
            print(response.json())
        else:
            print("Error", response.status_code)

