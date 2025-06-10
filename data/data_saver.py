import pandas as pd  
from sqlalchemy import create_engine # create_engine es una función de SQLAlchemy que se encarga de crear una conexión (o "motor") hacia una base de datos.
from sqlalchemy.exc import SQLAlchemyError #para manejar errores.
from decouple import config  #para leer variables de entorno (dbuser,dbpassword, etc)

class DataSaver:
    def __init__(self, ):
        user = config ('DB_USER')
        password = config ('DB_PASSWORD')
        host = config ('DB_HOST')
        database = config ('DB_NAME')
        port = config ('DB_PORT')

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine (url)



    def guardar_dataframe(self, df, nombre_tabla):
        # Verifica si el DataFrame está vacío
        if df is None:
            print(f'No se puede guardar: datos vacíos para {nombre_tabla}')
            return

        # Verifica que el tipo de dato recibido sea un DataFrame 
        if not isinstance(df, pd.DataFrame):
            print(f'Tipo inválido: se espera un DataFrame, se recibió {type(df)}.')
            return

        try:
            # Establece conexión con la base de datos SQLite
            #conn = sqlite3.connect(self.__db_path)

            # Guarda el DataFrame en una tabla SQLite
            # - if_exists='replace': reemplaza la tabla si ya existe
            # - index=False: no guarda el índice del DataFrame como columna
            #df.to_sql(nombre_tabla, conn, if_exists='replace', index=False)
            df.to_sql(nombre_tabla, con=self.engine, if_exists= 'replace', index=False)
            # Cierra la conexión a la base de datos
            #conn.close()

            print(f"Datos guardados en tabla: {nombre_tabla}")

        #except Exception as e:
        except SQLAlchemyError as e:
            # Captura cualquier error ocurrido durante el guardado
            print(f"Error guardando datos: {e}")
