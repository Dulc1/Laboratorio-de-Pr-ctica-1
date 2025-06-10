import pandas as pd
from domain.dataset import Dataset  # Importo mi clase base Dataset que ya tiene lógica común

# Creo una clase que se llama DataSetExcel y hereda de Dataset
class DataSetExcel(Dataset):

    # El constructor solo llama al constructor del padre pasándole la fuente (la ruta del archivo Excel)
    def __init__(self, fuente):
        super().__init__(fuente)

    # Aca defino cómo se cargan los datos desde un archivo Excel
    def cargar_datos(self):
        try:
            # Leo el archivo Excel que está en la ruta que guardé en self.fuente
            df = pd.read_excel(self.fuente)

            # Le asigno el dataframe al atributo "datos" (uso el setter)
            self.datos = df

            # Muestro que cargó bien
            print("Excel cargado.")

            # Si los datos están bien (sin nulos ni duplicados), aplico las transformaciones
            if self.validar_datos():
                self.transformar_datos()

        # Si pasa cualquier error (archivo dañado, ruta mal escrita, etc.), lo muestro
        except Exception as e:
            print(f"error cargando Excel: {e}")  # Muestro el error para entender qué pasó