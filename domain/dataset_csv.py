import pandas as pd
from .dataset import Dataset

# Defino una clase llamada DataSetCSV que hereda de Dataset
class DataSetCSV(Dataset):

    # Constructor: simplemente llama al constructor de la clase padre con la ruta del archivo
    def __init__(self, fuente):
        super().__init__(fuente)

    # Método que carga los datos desde un CSV
    def cargar_datos(self):
        try:
            # Leo el CSV desde la ruta guardada en self.fuente
            df = pd.read_csv(self.fuente)

            # Asigno el DataFrame al atributo datos (esto pasa por el setter que hice antes)
            self.datos = df

            # Si los datos están OK (sin nulos o duplicados), los transformo
            if self.validar_datos():
                self.transformar_datos()

        # Captura cualquier error (archivo dañado, ruta incorrecta, formato inválido, etc.)
        except Exception as e:
            print(f"error cargando CSV: {e}")  # Muestra el error