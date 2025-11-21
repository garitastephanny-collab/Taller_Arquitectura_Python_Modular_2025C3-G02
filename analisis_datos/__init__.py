"""
Inicializador del paquete analisis_datos.
"""

# RETO 5: Importa 'media' y 'mediana' desde .estadisticas
# TU CÓDIGO AQUÍ
from .estadisticas import media, mediana

# RETO 6: Importa 'generar_lista_compras' y 'guardar_lista_compras' desde .carga_datos
# TU CÓDIGO AQUÍ
from .carga_datos import generar_lista_compras, guardar_lista_compras

# Define la lista __all__ para exportar explícitamente
__all__ = ['media', 'mediana', 'generar_lista_compras', 'guardar_lista_compras']
