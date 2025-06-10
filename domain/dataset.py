# Importamos las herramientas necesarias para crear una clase abstracta
from abc import ABC, abstractmethod

# Definimos una clase abstracta llamada 'Dataset'
class Dataset(ABC):  # ABC significa "Abstract Base Class"
    
    # Método constructor: se ejecuta cuando se crea una nueva instancia de la clase
    def __init__(self, fuente):
        # Atributo privado (con doble guion bajo) que guarda la fuente de los datos, por ejemplo, un archivo o URL
        self.__fuente = fuente
        
        # atributo privado que almacena los datos una vez cargados
        self.__datos = None

    # Definimos una propiedad (getter) para acceder al atributo __datos desde fuera de la clase
    @property
    def datos(self):
        return self.__datos
    
    # Definimos el setter de la propiedad 'datos', para poder modificar el valor de __datos de forma controlada
    @datos.setter
    def datos(self, value):
        import pandas as pd
    # Validación mejorada: ahora no se permite asignar cualquier tipo de valor al atributo 'datos'
    # Esta línea verifica si el valor que se está asignando es un DataFrame de pandas
        if not isinstance(value, pd.DataFrame):
            # Si no es un DataFrame, lanza un error de tipo con un mensaje y el tipo que recibio.
            raise TypeError(f"Los datos deben ser un DataFrame de pandas. Se recibió: {type(value).__name__}")
        self.__datos = value


    # Otra propiedad, esta vez solo con getter, para acceder a la fuente (solo lectura)
    @property
    def fuente(self):
        return self.__fuente
        
    # Método abstracto: todas las clases hijas de Dataset tiene que si o si implementar este método
    @abstractmethod
    def cargar_datos(self):
        pass  # No tiene ninguna implementación porque depende de cada subclase

    def validar_datos (self):
        #veo la existencia de los datos, es decir que exista el dataframe pq en "self.datos=NONE" lo inicializamos vacio. Y si no hay datos disparo un error.
        if self.datos is None:
            raise ValueError("Dato no cargados")
        
        if self.datos.isnull().sum().sum() > 0:
            print("Datos faltantes detectados.")
        if self.datos.duplicated().sum() > 0:
            print("Filas duplicadas detectadas.")
        return True

    def transformar_datos (self):
            #1.  Pregunto si los datos no están vacíos o hay ausencia de datos
        if self.datos is not None: #(None representa la ausencia de un valor o un valor nulo)
            # 2. Normalizamos nombres de columnas: minúsculas, sin espacios al principio/final y con guiones bajos
            self.__datos.columns = self.__datos.columns.str.lower().str.strip().str.replace(" ", "_")
            # 3. Eliminamos duplicados
            self. __datos = self.datos.drop_duplicates()
            # 4. El for itera por las columanas y Convierte a texto y quita espacios en columnas tipo texto,para limpiar datos JSON de la API.
            for col in self.__datos.select_dtypes(include = "object").columns:
                self.__datos[col] = self.datos[col].astype(str).str.strip()
                print ("Transformaciones aplicadas")
        else:
            print("No hay datos para transformar")
    
    def mostrar_resumen(self):
    # Verifica si el atributo 'datos' contiene un DataFrame cargado
    # Si hay datos, utiliza el método .describe() para mostrar un resumen estadístico
    # El parámetro include='all' hace que se muestren estadísticas tanto de columnas numéricas como categóricas
    # Si no hay datos, imprime un mensaje indicando que no hay datos disponibles
        return print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")


    