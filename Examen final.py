# Requerimiento de monto inicial
saldo_inicial=20000
# Requerimiento de los usuarios con sus respectivos pines
usuarios = {
    "1234567890": {"pin": "1234", "saldo": 15000},
    "0987654321": {"pin": "5678", "saldo": 10000},
}
retiros_realizados = []
# Requerimento de opciones de retiro
montos_disponibles = [10, 20, 50, 100, 350, 500]
def validacion_tarjeta(tarjeta):
    pin = input("Por favor, ingrese su PIN: ")
    if tarjeta in usuarios and pin == usuarios[tarjeta]["pin"]:
        return True
    return False
def consultar_saldo(tarjeta):
    saldo = usuarios[tarjeta]["saldo"]
    print("Su saldo actual es:", saldo, "Bs.")
def realizar_retiro(tarjeta):
    saldo = usuarios[tarjeta]["saldo"]
    print("Seleccione un monto de retiro:")
    for i, monto in enumerate(montos_disponibles):
        print(f"{i+1}. {monto} Bs")
    print(f"{len(montos_disponibles) + 1}. Otro monto")
    opcion = int(input("Opción: "))
    if opcion <= len(montos_disponibles):
        monto = montos_disponibles[opcion - 1]
    else:
        monto = float(input("Ingrese el monto a retirar: "))

    if saldo >= monto:
        usuarios[tarjeta]["saldo"] -= monto
        retiros_realizados.append(monto)
        print(f"Retiro exitoso. Ha retirado {monto} Bs")
        consultar_saldo(tarjeta)
    else:
        print("Disculpe pero su saldo es insuficiente")
def imprimir_saldo_y_retiros():
    print("Saldo del dia:")
    total_retiros = sum(retiros_realizados)
    print(f"Total retiros: {total_retiros} Bs")
    print(f"Saldo restante en el cajero: {saldo_inicial - total_retiros} Bs")
#Cajero SMAR en funcionamiento
while True:
    tarjeta = input("Ingrese su numero de tarjeta: ")
    if validacion_tarjeta(tarjeta):
        break
    print("Tarjeta invalida. Intente nuevamente.")

while True:
    print("Bienvenido a este cajero automatico del banco SMAR")
    print("1. Consultar el saldo")
    print("2. Realizar un retiro")
    print("3. Imprimir mi saldo y los retiros del dia")
    print("4. Salir")
    opcion = int(input("ingrese una de las opciones: "))
    if opcion == 1:
        consultar_saldo(tarjeta)
    elif opcion == 2:
        realizar_retiro(tarjeta)
    elif opcion == 3:
        imprimir_saldo_y_retiros()
    elif opcion == 4:
        print ("Gracias por confiar en el banco SMAR espero que temga un gran dia")
    else:
        print("Opcion invalida; Por favor intente nuevamente.")
