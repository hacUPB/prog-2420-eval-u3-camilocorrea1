[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Camilo Correa Tabares
ID:  000509030
    Taquilla de cine

Este programa simula una taquilla de cine que permite al usuario realizar la compra de boletos para películas de Marvel, así como combos de crispetas y gaseosa. El usuario puede elegir el día en que asistirá al cine, seleccionar una película de una lista de películas disponibles y decidir si quiere comprar un combo pequeño o grande.
El objetivo principal es ofrecer una experiencia para calcular el total a pagar según las elecciones del usuario; el día de la semana afecta el precio de la boleta, y el tipo de combo incrementa el costo total.

Este programa es útil para facilitar el proceso de compra de boletas en una taquilla o en línea, agilizando la interacción con los clientes, minimizando errores en la selección de productos y precios, y brindando una experiencia de usuario más rápida y eficiente.

Funcionalidades del Programa:

1-Mostrar películas disponibles: El programa muestra una lista de películas de Marvel para que el usuario seleccione cuál desea ver.
2-Selección de película: El usuario puede elegir una película ingresando el número correspondiente.
3-Cálculo del precio de la boleta según el día: El usuario indica qué día asistirá al cine, y el programa ajusta el precio de la boleta dependiendo de si es un día de semana o fin de semana.
4-Selección de combo: El usuario puede elegir si desea comprar un combo de comida y bebida, eligiendo entre un combo pequeño o grande, o ninguno.
5-Cálculo total: El programa suma el costo de la boleta y el combo (si se selecciona) para mostrar el precio total a pagar.
6-Resumen de la compra: Al final, el programa muestra la película y el combo elegidos, junto con el costo total.

Casos Cubiertos:

-Días válidos: El programa cubre los días de la semana con precios específicos.
-Entradas no válidas: Si el usuario ingresa un número de película o combo incorrecto, se solicitará que elija nuevamente.
-Compras sin combo: El usuario puede decidir no comprar un combo.

Estructuras de Datos Utilizadas:

Listas: Se utiliza una lista para almacenar los nombres de las películas disponibles (peliculas). Esta lista es iterada para mostrar las opciones al usuario y permitir la selección.

Variables de precio: Se utilizan variables para almacenar los precios de las boletas (PRECIO_BOLETA_SEMANA, PRECIO_BOLETA_FINDE) y los combos (PRECIO_COMBO_PEQUENO, PRECIO_COMBO_GRANDE).

Pseudocódigo:
Inicio del Programa
    Mostrar lista de películas disponibles.
    Solicitar el día de la semana.
    Calcular precio de la boleta según el día.
Seleccionar Película
    Mostrar opciones y permitir al usuario seleccionar una.
    Validar la selección de película.
Seleccionar Combo
    Mostrar opciones de combo (pequeño, grande o ninguno).
    Validar la selección de combo.
Calcular Total
    Sumar precio de la boleta y el combo seleccionado.
Mostrar Resultado Final
    Mostrar película elegida.
    Mostrar combo seleccionado.
    Mostrar total a pagar.
Fin del Programa










