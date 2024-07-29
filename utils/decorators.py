import time
import logging

logging.basicConfig(level=logging.INFO)

# Decorador para medir el tiempo de ejecución
def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.4f}  segundos")
        return result
    return wrapper
