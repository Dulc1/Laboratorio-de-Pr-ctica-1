from os import path
from domain.dataset_csv import DataSetCSV
from domain.dataset_excel import DataSetExcel
from domain.dataset_api import DatasetAPI
from domain.dataset_json import DataSetJSON

# Importo la clase que guarda los datos en una base de datos SQLite
from data.data_saver  import DataSaver

# Ruta de los archivos CSV y Excel usando la ruta del archivo actual (__file__)
csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")
excel_path = path.join(path.dirname(__file__), "files/ventas.xlsx")
json_path = path.join(path.dirname(__file__), "data/mercadolibre.json")


# Crea una instancia del manejador de datos CSV, pasando la ruta como argumento
csv = DataSetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

# Crea una instancia del manejador de datos Excel, pasando la ruta como argumento
excel = DataSetExcel(excel_path)
excel.cargar_datos()
excel.mostrar_resumen()

api = DatasetAPI ("https://apis.datos.gob.ar/georef/api/provincias")
api.cargar_datos()

# JSON
json_dataset = DataSetJSON(json_path)
json_dataset.cargar_datos()
json_dataset.mostrar_resumen()

# Crea una instancia del objeto encargado de guardar DataFrames en una base SQLite
db =DataSaver()
#db.guardar_dataframe(api.datos, "provincias_api")
db.guardar_dataframe(excel.datos, "ventas.xlsx")
db.guardar_dataframe(csv.datos, "w_mean_prod.csv")
db.guardar_dataframe(json_dataset.datos, "mercadolibre_json")