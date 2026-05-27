import requests


class DataSender:

    TELEMETRY_URL = "http://127.0.0.1:8000/telemetry/"
    SCALE_EVENTS_URL = "http://127.0.0.1:8000/scale-events/"

    @staticmethod
    def send_telemetry(data):
        DataSender.send_data(DataSender.TELEMETRY_URL, data)

    @staticmethod
    def send_scale_event(data):
        DataSender.send_data(DataSender.SCALE_EVENTS_URL, data)

    @staticmethod
    def send_data(url, data):
        try:
            response = requests.post(url, json=data)

            if response.status_code == 200:
                print("Datos enviados correctamente:")
                print(response.json())
            else:
                print("Error al enviar datos")
                print("Código:", response.status_code)
                print("Respuesta:", response.text)

        except Exception as e:
            print("Error al crear la petición")
            print(e)