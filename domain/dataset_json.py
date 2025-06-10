import pandas as pd  # Importo pandas para poder trabajar con dataframes
from domain.dataset import Dataset  # Importo la clase base Dataset que hice antes

# Defino la clase DataSetJSON que hereda de Dataset
class DataSetJSON(Dataset):
    
    # Constructor: solo llama al constructor del padre (Dataset)
    def __init__(self, fuente):
        super().__init__(fuente)  # Llama al constructor de Dataset y guarda la ruta o URL

    # Método para cargar los datos del JSON
    def cargar_datos(self):
        try:
            # Intenta leer el archivo JSON que está en self.fuente (la ruta)
            df = pd.read_json(self.fuente)
            
            # Si lo puede leer, lo guarda en el atributo self.datos
            self.datos = df

            # Mensaje de éxito
            print("JSON cargado correctamente.")

            # Si los datos se validan correctamente (verifica nulos y duplicados), entonces los transforma
            if self.validar_datos():
                self.transformar_datos()

        # Si hay un error de formato o contenido del JSON
        except ValueError:
            print("Error al cargar el JSON.")  # Capaz el JSON está mal formado

        # Si el archivo no existe en la ruta indicada
        except FileNotFoundError:
            print("Archivo no encontrado.")  # Me equivoqué en la ruta o el archivo no está

        # Para cualquier otro error que no haya previsto
        except Exception:
            print("Error desconocido.")