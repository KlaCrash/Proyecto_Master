-- Eliminar la tabla Alojamientos si existe
DROP TABLE IF EXISTS Alojamientos;

-- Crear tabla principal para los alojamientos
CREATE TABLE Alojamientos (
    id_alojamiento INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    valoracion VARCHAR(6) NOT NULL,
    ciudad VARCHAR(20) NOT NULL,
    localizacion TEXT,
    distancia VARCHAR(50),
    cercanias TEXT,
    descripcion TEXT
);