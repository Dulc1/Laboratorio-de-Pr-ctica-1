import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)  # Llama al constructor de la clase base Dataset con la fuente (URL)

    def cargar_datos(self):
        try:
            response = requests.get(self.fuente)  # Hace una petición GET a la URL almacenada en fuente
            if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
                df = pd.json_normalize(response.json())  # Normaliza el JSON a un DataFrame de pandas

                # Función para verificar si un valor es una lista
                def es_lista(x):
                    return isinstance(x, list)

                # Función para convertir listas en strings separados por coma
                def lista_a_string(x):
                    if isinstance(x, list):
                        return ", ".join(map(str, x))  # Convierte cada elemento de la lista a string y une con comas
                    

                # Recorre todas las columnas del DataFrame y convierte a texto
                for col in df.columns:
                    # Aplica la función es_lista a cada valor de la columna y verifica si alguno es lista
                    if df[col].apply(es_lista).any():
                        # Si la columna contiene listas, las convierte a string usando lista_a_string
                        df[col] = df[col].apply(lista_a_string)

                self.datos = df  # Guarda el DataFrame procesado en el atributo datos
                print (self.datos)
                print("API cargada")

                # Valida y transforma los datos si son correctos
                if self.validar_datos():
                    self.transformar_datos()
            else:
                print("Error al obtener datos de API")

        except Exception as e:
            print(f'Error API. {e}')  # Captura y muestra cualquier error ocurrido durante la carga
