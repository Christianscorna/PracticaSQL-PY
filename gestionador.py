import sqlite3 as sql

with sql.connect("Libreria.db") as con:
    cursor = con.cursor()
    cursor.execute('SELECT titulo, precio FROM Libro')
    datos = cursor.fetchall()
    cursor.execute('SELECT titulo, COUNT(*) as Cantidad FROM Libro GROUP BY titulo')
    datos2 = cursor.fetchall()

#Mostrar todos los libros disponibles con su precio
print("Lista de libros disponibles y sus precios:")
for li in datos:
    titulo, precio = li
    print(f" - {titulo}: ${precio:.2f}")

#Consultar el total de libros vendidos por título.
print("Cantidad de registros por título:")
for titulo, cantidad in datos2:
    print(f" - {titulo}: {cantidad}")