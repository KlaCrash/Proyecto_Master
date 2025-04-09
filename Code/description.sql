--Muestra todos los datos de la tabla Alojamientos
SELECT * FROM Alojamientos;

--Muestra el número de filas de la tabla Alojamientos
SELECT COUNT(id_alojamiento) FROM Alojamientos;

--Muestra si hay o no un alojamiento que se llame "casa malferit"
SELECT nombre FROM Alojamientos WHERE nombre like 'casa malferit';

--Muestra si hay o no alojamientos que sean hoteles de Madrid, con una valoración de 2 estrellas.
SELECT nombre, tipo, ciudad, valoracion FROM Alojamientos WHERE tipo like 'hotel' AND ciudad like 'Madrid' AND valoracion like '2%';
