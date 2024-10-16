
def main():
    # Lista de películas y precios de las boletas y combos para la taquilla del cine
    # Lista de películas de Marvel disponibles en el cine
    peliculas = [
        "Iron Man",
        "Capitán América",
        "Thor",
        "Avengers",
        "Doctor Strange",
        "Spider-Man"
    ]

    # Precios de las boletas según el día de la semana
    PRECIO_BOLETA_SEMANA = 10000  # Lunes a jueves
    PRECIO_BOLETA_FINDE = 16000   # Viernes a domingo

    # Precios de los combos disponibles
    PRECIO_COMBO_PEQUENO = 12000  # Crispetas y gaseosa
    PRECIO_COMBO_GRANDE = 20000   # Crispetas grandes y gaseosa grande

    def mostrar_peliculas_disponibles():
        """
        Imprime una lista de las películas disponibles para que el usuario elija.
        """
        print("Películas disponibles:")
        for indice, pelicula in enumerate(peliculas, 1):
            print(f"{indice}. {pelicula}")

    def obtener_pelicula_seleccionada():
        """
        Permite al usuario seleccionar una película.
        Devuelve el nombre de la película seleccionada.
        """
        mostrar_peliculas_disponibles()
        try:
            seleccion = int(
                input("Elige el número de la película que deseas ver: "))
            # Se valida la entrada del usuario para evitar errores de índice
            if 1 <= seleccion <= len(peliculas):
                return peliculas[seleccion - 1]
            else:
                print("Selección inválida. Inténtalo de nuevo.")
                return obtener_pelicula_seleccionada()
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
            return obtener_pelicula_seleccionada()

    def calcular_precio_boleta(dia_semana):
        """
        Determina el precio de la boleta según el día de la semana.
        Devuelve el precio de la boleta para ese día.
        """
        dia_semana = dia_semana.lower()  # Convertir a minúsculas

        # Determinar precio de la boleta según el día
        if dia_semana in ["lunes", "martes", "miercoles", "jueves"]:
            return PRECIO_BOLETA_SEMANA
        elif dia_semana in ["viernes", "sabado", "domingo"]:
            return PRECIO_BOLETA_FINDE
        else:
            print("Día inválido. Intenta nuevamente.")
            return None

    def seleccionar_combo():
        """
        Permite al usuario seleccionar si quiere comprar un combo, y el tamaño del combo.
        Devuelve el precio del combo seleccionado o 0 si no se desea comprar.
        """
        print("Combos disponibles:")
        print("1. Combo pequeño (crispetas y gaseosa) - $12000")
        print("2. Combo grande (crispetas y gaseosa) - $20000")
        seleccion_combo = input(
            "¿Deseas comprar un combo? (1 para pequeño, 2 para grande, N para ninguno): ").lower()

        # Determinar el precio del combo según la selección
        if seleccion_combo == "1":
            return PRECIO_COMBO_PEQUENO, "Combo pequeño"
        elif seleccion_combo == "2":
            return PRECIO_COMBO_GRANDE, "Combo grande"
        elif seleccion_combo == "n":
            return 0, "Ningún combo"
        else:
            print("Selección inválida. No se añadirá combo.")
            return 0, "Ningún combo"

    def procesar_compra():
        """
        Proceso de compra en la taquilla del cine:
        - Pide al usuario el día en que asistirá al cine.
        - Permite seleccionar una película.
        - Permite elegir si quiere un combo.
        - Calcula y muestra el total a pagar.
        """
        dia = input("¿Qué día asistirás al cine? (Lunes a Domingo): ")
        precio_boleta = calcular_precio_boleta(dia)

        # Verificar si el día ingresado es válido
        if precio_boleta is None:
            return

        # Elegir película
        pelicula_seleccionada = obtener_pelicula_seleccionada()
        print(f"Has seleccionado la película: {pelicula_seleccionada}")

        # Seleccionar combo
        precio_combo, combo_seleccionado = seleccionar_combo()

        # Calcular el total
        total = precio_boleta + precio_combo
        print(f"El valor total a pagar es: ${total}")

        print(f"Película elegida: {pelicula_seleccionada}")
        print(f"Combo elegido: {combo_seleccionado}")

    procesar_compra()


if __name__ == "__main__":
    main()
