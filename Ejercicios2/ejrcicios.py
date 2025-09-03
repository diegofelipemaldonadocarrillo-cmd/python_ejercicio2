def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Sistema de Reservas")
        print("2. Juego FizzBuzz")
        print("3. Calculadora Simple")
        print("4. Control de Temperatura en Invernadero")
        print("5. Detección de Intrusos")
        print("6. Control de Luces Automático")
        print("7. Control de Aire Acondicionado")
        print("8. Control de Acceso a una Tienda")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema_reservas()
        elif opcion == "2":
            juego_fizzbuzz()
        elif opcion == "3":
            calculadora_simple()
        elif opcion == "4":
            control_temperatura()
        elif opcion == "5":
            deteccion_intrusos()
        elif opcion == "6":
            control_luces()
        elif opcion == "7":
            control_aire()
        elif opcion == "8":
            control_acceso()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

# 1. Sistema de Reservas
def sistema_reservas():
    print("\n--- SISTEMA DE RESERVAS ---")
    capacidad = 5
    reservados = 0
    while True:
        print(f"Asientos disponibles: {capacidad - reservados}")
        print("1. Reservar asiento")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if reservados < capacidad:
                reservados += 1
                print("Reserva realizada.")
            else:
                print("No hay asientos disponibles.")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

# 2. FizzBuzz
def juego_fizzbuzz():
    print("\n--- JUEGO FIZZBUZZ ---")
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    input("Presione Enter para volver al menú...")

# 3. Calculadora
def calculadora_simple():
    print("\n--- CALCULADORA SIMPLE ---")
    while True:
        print("1. Realizar cálculo")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese operación (+, -, *, /): ")

            if operacion == "+":
                print("Resultado:", a + b)
            elif operacion == "-":
                print("Resultado:", a - b)
            elif operacion == "*":
                print("Resultado:", a * b)
            elif operacion == "/":
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("No se puede dividir por cero.")
            else:
                print("Operación inválida.")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

# 4. Control de Temperatura
def control_temperatura():
    print("\n--- CONTROL DE TEMPERATURA EN INVERNADERO ---")
    for i in range(3):  # Simula 3 lecturas manuales
        temp = float(input("Ingrese la temperatura en °C: "))
        if temp < 10:
            print("Estado: Calefactor ACTIVADO")
        elif temp > 25:
            print("Estado: Ventilador ACTIVADO")
        else:
            print("Estado: Inactivo")
    input("Presione Enter para volver al menú...")

# 5. Detección de Intrusos
def deteccion_intrusos():
    print("\n--- DETECCIÓN DE INTRUSOS ---")
    alarma_activada = True
    for i in range(3):  # 3 intentos de simulación
        print("Ingrese si los sensores detectan movimiento (s/n):")
        s1 = input("Sensor 1: ").lower() == "s"
        s2 = input("Sensor 2: ").lower() == "s"
        s3 = input("Sensor 3: ").lower() == "s"
        noche = input("¿Es de noche? (s/n): ").lower() == "s"

        if (s1 + s2 + s3) >= 2 and noche and alarma_activada:
            print("ALERTA: Alarma ACTIVADA")
        else:
            print("Alarma NO activada")
    input("Presione Enter para volver al menú...")

# 6. Control de Luces
def control_luces():
    print("\n--- CONTROL DE LUCES AUTOMÁTICO ---")
    for i in range(3):
        noche = input("¿Es de noche? (s/n): ").lower() == "s"
        movimiento = input("¿Hay movimiento? (s/n): ").lower() == "s"
        if noche and movimiento:
            print("Luces ENCENDIDAS")
        else:
            print("Luces APAGADAS")
    input("Presione Enter para volver al menú...")

# 7. Control de Aire Acondicionado
def control_aire():
    print("\n--- CONTROL DE AIRE ACONDICIONADO ---")
    for i in range(3):
        temp = float(input("Ingrese temperatura °C: "))
        humedad = float(input("Ingrese humedad %: "))
        if (temp > 28 and humedad > 60) or temp > 30:
            print("Aire Acondicionado: ENCENDIDO")
        else:
            print("Aire Acondicionado: APAGADO")
    input("Presione Enter para volver al menú...")

# 8. Control de Acceso a Tienda
def control_acceso():
    print("\n--- CONTROL DE ACCESO A UNA TIENDA ---")
    for i in range(3):
        tiene_membresia = input("¿Tiene membresía? (s/n): ").lower() == "s"
        es_empleado = input("¿Es empleado? (s/n): ").lower() == "s"
        horario = input("¿Está dentro del horario de atención? (s/n): ").lower() == "s"

        if (tiene_membresia and horario) or es_empleado:
            print("Acceso PERMITIDO")
        else:
            print("Acceso DENEGADO")
    input("Presione Enter para volver al menú...")

# Iniciar el programa
menu_principal()

