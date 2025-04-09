from Funciones_Proyecto import (
    configurar_servicio,
    inicializar_navegador,
    cargar_mas_resultados,
    esperar_div_padre,
    extraer_titulo,
    encontrar_div_hijos,
    extraer_estrellas,
    extraer_localizacion,
    extraer_distancia,
    extraer_cercanias,
    extraer_descripcion,
    guardar_en_csv,
    modificar_campo_csv
)

# URL del sitio web
urls = {
    "Madrid": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8164cd8ddb75d5a8c96d0dc0708d7aed&aid=304142&dest_id=-390625&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8164cd8ddb75d5a8c96d0dc0708d7aed&aid=304142&dest_id=-390625&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8164cd8ddb75d5a8c96d0dc0708d7aed&aid=304142&dest_id=-390625&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D203',  # URL para albergues
    },
    
    "Sevilla": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-402849&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-402849&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-402849&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D203',  # URL para albergues
    },

    "Granada": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-384328&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-384328&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-384328&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D203',  # URL para albergues
    },

    "Córdoba": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-378765&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-378765&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-378765&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203',  # URL para albergues
    },

    "Málaga": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-390787&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-390787&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-390787&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203',  # URL para albergues
    },

    "Barcelona": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-372490&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-372490&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-372490&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D203',  # URL para albergues
    },

    "Valencia": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-406131&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-406131&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-406131&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&nflt=ht_id%3D203',  # URL para albergues
    },

    "Toledo": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-404357&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-404357&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-404357&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203',  # URL para albergues
    },

    "Salamanca": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-400105&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-400105&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&dest_id=-400105&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203',  # URL para albergues
    },

    "Bilbao": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-373608&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-373608&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-373608&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203',  # URL para albergues
    },

    "Zaragoza": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-409149&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-409149&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-409149&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203',  # URL para albergues
    },

    "Benidorm": {
        "hotel": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-373226&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D204',  # URL para hoteles
        "hostal": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-373226&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D216',  # URL para hostales/pensiones
        "albergue": 'https://www.booking.com/searchresults.es.html?label=gen173nr-1FCAEoggI46AdIClgEaEaIAQGYAQq4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsDlz78GwAIB0gIkZjRmOTJhZWUtZTkwOC00NjZlLTg2NjgtNWNlNTZkMTNkNzY22AIF4AIB&sid=8eb0e60068c93b7156b24ed598dd28a4&aid=304142&checkin=2025-04-12&checkout=2025-04-13&dest_id=-373226&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&nflt=ht_id%3D203'  # URL para albergues
    }
}
# Ruta al ejecutable de chromedriver
path = r'.\chromedriver-win64\chromedriver.exe'

# Llama a la función para configurar el servicio para el controlador
service = configurar_servicio(path)

# Define las variables antes del bucle principal
datos_extraidos = []  # Lista para almacenar todos los datos extraídos
campos_csv = ["Nombre", "Tipo", "Valoración", "Localización", "Ciudad", "Distancia", "Cercanías", "Descripción"]

# Itera sobre cada tipo de alojamiento y su URL
for ciudades, tipos in urls.items():  # 'tipos' es el diccionario de "hotel", "hostal", "albergue"
    for tipo, url in tipos.items():  # Itera sobre los tipos de alojamiento y sus URLs
        print(f"Procesando {tipo}s en {ciudades}...")

        # Llama a la función para inicializar el navegador para cada URL
        driver = inicializar_navegador(service, url)

        # Llama a la función para cargar más resultados
        cargar_mas_resultados(driver)

        # Llama a la función para esperar el div padre
        div_padre = esperar_div_padre(driver, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]', 10)

        # Verifica si el div padre fue encontrado
        if not div_padre:
            print(f"No se pudo encontrar el div padre para {tipo}s en {ciudades}. Saltando a la siguiente URL.")
            driver.quit()
            continue

        # Llama a la función para encontrar los div hijos
        div_hijos = encontrar_div_hijos(driver)

        # Itera sobre los hijos y busca los datos
        for index, div_hijo in enumerate(div_hijos, start=1):
            try:
                # Llama a la función para extraer el título
                titulo = extraer_titulo(div_hijo)

                # Llama a la función para extraer las estrellas
                estrellas = extraer_estrellas(div_hijo)

                # Llama a la función para extraer la localización
                localizacion_data = extraer_localizacion(div_hijo)
                localizacion = localizacion_data["localizacion"] if localizacion_data else None
                ciudad = localizacion_data["ciudad"] if localizacion_data else None

                # Llama a la función para extraer la distancia
                distancia = extraer_distancia(div_hijo)

                # Llama a la función para extraer las cercanías
                cercanias = extraer_cercanias(div_hijo)

                # Llama a la función para extraer la descripción
                descripcion = extraer_descripcion(div_hijo)

                # Agrega los datos a la lista
                datos_extraidos.append({
                    "Nombre": titulo,
                    "Tipo": tipo.capitalize(),
                    "Valoración": estrellas,
                    "Localización": localizacion,
                    "Ciudad": ciudad,
                    "Distancia": distancia,
                    "Cercanías": cercanias,
                    "Descripción": descripcion
                })
            except Exception as e:
                print(f"Hijo {index}: Error al extraer datos para {tipo}s en {ciudades} - {e}")
        
        # Cierra el navegador después de procesar la URL
        driver.quit()

# Llama a la función para guardar los datos en un archivo CSV
guardar_en_csv("alojamientos.csv", datos_extraidos, campos_csv)

# Ruta del archivo CSV original y el archivo modificado
csv_file = 'alojamientos.csv'
output_file = 'alojamientos_modificado.csv'

# Llama a la función para modificar el campo valoraciones
modificar_campo_csv(csv_file, output_file, campo_index=2)