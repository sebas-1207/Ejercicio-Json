#Juan Sebastian Lozano Siza. Grupo: R4
import json

with open('Ahorradores.json') as archivo_entrada:
    data = json.load(archivo_entrada)

ahorradores_filtrados = [ahorrador for ahorrador in data['cliente'] if ahorrador['Saldo'] > 35_000_000]

nueva_lista = []
consecutivo = 1

for ahorrador in ahorradores_filtrados:
    nueva_lista.append({
        "Consecutivo": consecutivo,
        "NumCuenta": ahorrador["NumCuenta"],
        "Saldo": ahorrador["Saldo"]
    })
    consecutivo += 1

nuevo_data = {"cliente": nueva_lista}

with open('Dian.json', 'w') as archivo_salida:
    json.dump(nuevo_data, archivo_salida, indent=4)

print("Archivo 'Dian.json' generado correctamente.")
