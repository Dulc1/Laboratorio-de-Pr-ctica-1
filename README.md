Este es el laboratorio 1 del curso de análisis de datos del Informatorio.

## ¿Qué hace este proyecto?

- Carga datos desde archivos (como Excel,CSV, JSON )
- Aplica algunas transformaciones
- Guarda los datos en una base de datos.

## Estructura

El proyecto está dividido en carpetas para organizar mejor el código:
- `data/`: para guardar funciones que cargan y limpian datos
- `db/`: para conectarse con la base de datos
- `domain/`: para manejar los datos como objetos
- `files/`: archivos de entrada como Excel o CSV

## Validaciones que agregué

Durante las clases surgió la idea de validar que los datos cargados sean correctos. Entonces, agregué una validación al atributo `datos` para asegurar de que siempre sea un DataFrame de pandas:

```python
@datos.setter
def datos(self, value):
    import pandas as pd
    if not isinstance(value, pd.DataFrame):
        raise TypeError(f"Los datos deben ser un DataFrame de pandas. Se recibió: {type(value).__name__}")
    self.__datos = value
```

## Mejora: soporte para archivos JSON
Personalmente hago web scraping, y por eso agregué soporte para cargar archivos en formato JSON. Esto me permite trabajar con datos en distintos formatos según lo necesite, no solo CSV.
