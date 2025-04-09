import csv
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def configurar_servicio(path):
    """
    Configura el servicio para el controlador de Chrome.

    :param path: Ruta al ejecutable de chromedriver.
    :return: Instancia del servicio configurado.
    """
    return Service(path)

def inicializar_navegador(service, url):
    """
    Inicializa el navegador y carga la URL especificada.

    :param service: Instancia del servicio de Selenium (chromedriver).
    :param url: URL que se desea cargar en el navegador.
    :return: Instancia del navegador Selenium.
    """
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    return driver

def cargar_mas_resultados(driver):
    """
    Función para desplazarse hacia abajo y hacer clic en el botón "Cargar más resultados".
    Se detiene cuando no hay más resultados para cargar.
    """
    while True:
        try:
            # Desplázate hacia abajo para asegurarte de que el botón sea visible
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)  # Espera un momento para que se cargue el contenido dinámico, si lo pones a menos puede que no funcione.

            # Busca el botón "Cargar más resultados" usando una parte de la clase o su texto
            boton_cargar_mas = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "a83ed08757") and contains(., "Cargar más resultados")]'))
            )
            boton_cargar_mas.click()
            time.sleep(1)  # Espera un momento para que se carguen los nuevos elementos
        except:
            print("No hay más resultados para cargar.")
            break  # Sal del bucle si no hay más botones "Cargar más resultados"

def esperar_div_padre(driver, xpath, timeout=10):
    """
    Espera hasta que un elemento esté presente en el DOM.

    :param driver: Instancia del navegador Selenium.
    :param xpath: XPath del elemento a esperar.
    :param timeout: Tiempo máximo de espera en segundos (por defecto 10).
    :return: El elemento encontrado o None si no se encuentra.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except TimeoutException:
        print(f"El elemento con XPath '{xpath}' no se encontró en {timeout} segundos.")
        return None

def encontrar_div_hijos(driver, xpath='.//div[@data-testid="property-card"]'):
    """
    Encuentra todos los div hijos con el atributo data-testid="property-card".

    :param driver: Instancia del navegador Selenium.
    :param xpath: XPath para encontrar los div hijos (por defecto busca property-card).
    :return: Lista de elementos WebElement encontrados.
    """
    try:
        return driver.find_elements(By.XPATH, xpath)
    except Exception as e:
        print(f"Error al encontrar los div hijos: {e}")
        return []

def extraer_titulo(div_hijo):
    """
    Extrae el título de un div hijo.

    :param div_hijo: Elemento WebElement que representa un div hijo.
    :return: El texto del título o vacío (None/NULL) si no se encuentra.
    """
    try:
        titulo_div = div_hijo.find_element(By.XPATH, './/div[@data-testid="title"]')
        titulo = titulo_div.text.strip() 
        return titulo if titulo else None  # Devuelve None si el texto está vacío
    except:
        return None  # Si no se encuentra el título
    
def extraer_estrellas(div_hijo):
    """
    Extrae las estrellas de un div hijo.

    :param div_hijo: Elemento WebElement que representa un div hijo.
    :return: El texto de las estrellas o vacío (None/NULL) si no se encuentra.
    """
    try:
        estrellas_div = div_hijo.find_element(By.XPATH, './/div[contains(@class, "b3f3c831be")]')
        estrellas =  estrellas_div.get_attribute("aria-label").strip()
        return estrellas if estrellas else "0 de 5"  # Devuelve "0 de 5" si el texto está vacío
    except:
        return "0 de 5"  # Si no se encuentran las estrellas
    
def extraer_localizacion(div_hijo):
    """
    Extrae la localización de un div hijo y la divide en localización y ciudad.

    :param div_hijo: Elemento WebElement que representa un div hijo.
    :return: Un diccionario con 'localizacion' y 'ciudad', o None si no se encuentra.
    """
    try:
        localizacion_div = div_hijo.find_element(By.XPATH, './/span[contains(@class, "aee5343fdb def9bc142a")]')
        localizacion_completa = localizacion_div.text.strip()
        if localizacion_completa:
            partes = localizacion_completa.split(",", 1)  # Divide en dos partes como máximo
            localizacion = partes[0].strip() if len(partes) > 0 else None # Toma la primera parte
            ciudad = partes[1].strip() if len(partes) > 1 else None # Si hay más de una parte, toma la segunda parte
            return {"localizacion": localizacion, "ciudad": ciudad}
        return {"localizacion": None, "ciudad": None}  # Si el texto está vacío
    except:
        return {"localizacion": None, "ciudad": None}  # Si no se encuentra el elemento
    
def extraer_distancia(div_hijo):
    """
    Extrae la distancia de un div hijo.

    :param div_hijo: Elemento WebElement que representa un div hijo.
    :return: El texto de la distancia o vacío (None/NULL) si no se encuentra.
    """
    try:
        distancia_div = div_hijo.find_element(By.XPATH, './/span[@data-testid="distance"]')
        distancia = distancia_div.text.strip()
        return distancia if distancia else None  # Devuelve None si el texto está vacío
    except:
        return None # Si no se encuentra la distancia
    
def extraer_cercanias(div_hijo):
    """
    Extrae las cercanías de un div hijo.

    :param div_hijo: Elemento WebElement que representa un div hijo.
    :return: El texto de las cercanías o vacío (None/NULL) si no se encuentra.
    """
    try:
        cercanias_div = div_hijo.find_element(By.XPATH, './/span[contains(@class, "f419a93f12")]/span')
        cercanias = cercanias_div.text.strip()
        return cercanias if cercanias else None  # Devuelve None si el texto está vacío
    except:
        return None # Si no se encuentran las cercanías
    
def extraer_descripcion(div_hijo):
    """
    Extrae la descripción de un div hijo.

    :param div_hijo: Elemento WebElement que representa un div hijo.
    :return: El texto de la descripción o vacío (None/NULL) si no se encuentra.
    """
    try:
        descripcion_div = div_hijo.find_element(By.XPATH, './/div[@class="abf093bdfe"]')
        descripcion = descripcion_div.text.strip()
        return descripcion if descripcion else None  # Devuelve None si el texto está vacío
    except:
        return None # Si no se encuentra la descripción
    
def guardar_en_csv(nombre_archivo, datos, campos):
    """
    Guarda los datos extraídos en un archivo CSV.

    :param nombre_archivo: Nombre del archivo CSV.
    :param datos: Lista de diccionarios con los datos a guardar.
    :param campos: Lista de nombres de los campos (columnas) del CSV.
    """
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=';')
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"Datos guardados exitosamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo CSV: {e}")

def modificar_campo_csv(input_file, output_file, campo_index):
    """
    Modifica un campo específico de un archivo CSV para que solo contenga el primer carácter.

    Args:
        input_file (str): Ruta del archivo CSV original.
        output_file (str): Ruta del archivo CSV modificado.
        campo_index (int): Índice del campo a modificar (comienza en 0).
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Leer y escribir la cabecera
        header = next(reader)
        writer.writerow(header)

        # Procesar cada fila
        for row in reader:
            # Modificar el campo especificado para que solo tenga el primer carácter
            row[campo_index] = row[campo_index][0] if row[campo_index] else ''  # Manejar valores vacíos o nulos
            writer.writerow(row)

    print(f"Archivo modificado guardado como {output_file}")