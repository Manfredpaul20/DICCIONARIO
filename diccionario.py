# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero en Sistemas"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la profesion
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
