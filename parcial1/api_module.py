# api_module.py
import os
import pandas as pd

# Obtén la ruta completa del archivo CSV
ruta_archivo = os.path.join(os.path.dirname(__file__), 'components', 'Resultados_de_An_lisis_de_Laboratorio_Suelos_en_Colombia_20240301.csv')

# Cargar los datos una vez al inicio del módulo
datos = pd.read_csv(ruta_archivo, low_memory=False)

def obtener_datos(departamento, municipio, cultivo, limit):
    resultados = datos[(datos['Departamento'] == departamento) & 
                       (datos['Municipio'] == municipio) & 
                       (datos['Cultivo'] == cultivo)].head(limit)
    
    if resultados.empty:
        print("No se encontraron datos para la consulta.")
        return None, None

    # Nombres de las columnas edáficas con caracteres especiales
    columnas_edaficas = ['pH agua:suelo 2,5:1,0', 'Fósforo (P) Bray II mg/kg', 'Potasio (K) intercambiable cmol(+)/kg']

    # Convertir los valores a tipo numérico
    resultados[columnas_edaficas] = resultados[columnas_edaficas].apply(pd.to_numeric, errors='coerce')

    # Verificar la existencia de las columnas antes de calcular la mediana
    if all(col in resultados.columns for col in columnas_edaficas):
        mediana_edaficas = resultados[columnas_edaficas].median()

        # Crear nuevas columnas en los resultados con las medianas
        resultados['Mediana pH'] = mediana_edaficas['pH agua:suelo 2,5:1,0']
        resultados['Mediana Fósforo(P)'] = mediana_edaficas['Fósforo (P) Bray II mg/kg']
        resultados['Mediana Potasio(K)'] = mediana_edaficas['Potasio (K) intercambiable cmol(+)/kg']
    else:
        print("Algunas columnas edáficas no están presentes en los resultados.")
        mediana_edaficas = None

    return resultados, mediana_edaficas
