MANUAL DE USUARIO — AHORCADO DEL 
BIENESTAR
Versión: 1.05Desarrollado por:
Gabriel Rodrigo Enríquez Guerra
Fernando Alejandro Hernández Ramos

 Descripción general del juego:
Ahorcado del Bienestar es un juego en consola donde el jugador debe adivinar una palabra oculta antes de 
quedarse sin intentos. Cada error dibuja una parte del ahorcado hasta completar la figura, lo que significa 
perder.
El juego ofrece 4 niveles de dificultad, cada uno con un número distinto de intentos y palabras más complejas y 
específicas.

 Requisitos del sistema:
Sistema operativo: Windows, Linux o MacOS
Python 3.8 o superior
Consola o terminal para ejecutar el script
No requiere conexión a internet

 ¿Cómo iniciar el juego?
1. Descarga o copia el archivo del programa con extensión .py.
2. Abre una terminal en la carpeta donde esté el archivo.
3. Ejecuta el comando:
4. Python ahorcado.py
5. Aparecerá el menú principal.

 Menú principal
Cuando inicias el programa verás:
1 - Fácil
2 - Medio
3 - Difícil
4 - Modo Diablo 😛😈🔥
0 - Salir
Opciones:
1 — Fácil: palabras cortas, 6 intentos.
2 — Medio: dificultad moderada, 5 intentos.
3 — Difícil: palabras largas, 4 intentos.
4 — Modo Diablo: palabras complejas, solo 2 intentos.
0 — Salir: termina el programa.


Para elegir un modo, escribe el número y presiona Enter.

Mecánicas de juego
Una vez elegido el nivel:
1. Se selecciona una palabra oculta al azar.
2. El jugador debe ingresar una letra por turno.
3. El sistema valida la letra:
No puede ser un número.
No puede repetirse.
Debe ser solo un carácter.
4. Si aciertas:
La letra se revela en la palabra.
5. Si fallas:
Pierdes un intento.
Se dibuja una parte del ahorcado.
La letra se agrega a la lista de descartadas.
El estado se muestra así:
Intentos restantes
Letras usadas
Avance de la palabra
Dibujo del ahorcado actual

¿Cómo Ganar?
Ganará el jugador si:
✔ Completa todas las letras de la palabra antes de quedarse sin intentos.
El sistema mostrará:
✔ ¡Palabra completada!
La palabra es: <palabra>

Derrota
El jugador pierde si:
❌ Se quedan sin intentos antes de completar la palabra.
Aparecerá el dibujo final del ahorcado y el mensaje de derrota.

 Reinicio y continuación
Al completar o perder una palabra:
Si aún quedan palabras en el nivel, inicia automáticamente la siguiente.
Si ya no hay palabras disponibles o deseas salir, regresas al menú.


Ejemplos:
Entrada del jugador:
INTRODUCE LETRA: a
Mensaje posible:
Si aciertas: “¡Has acertado la letra! Sigue así.”
Si fallas: “¡Has fallado la letra!”

¡Errores frecuentes del usuario!
Situación Mensaje del sistema

Se escribe más de una letra "Has puesto más de una letra"

Se repite una letra descartada "Esa letra ya la habías dicho"

Se repite una letra acertada "Ya la has acertado"

No es una letra del abecedario "No has introducido una letra del abecedario"

El sistema obliga a ingresar una letra válida antes de continuar.

 Consejos de uso
Juega primero en nivel fácil para familiarizarte.
Evita repetir letras: revisa siempre la lista de descartadas.
Usa lógica: empieza con vocales y consonantes comunes (s, r, n, l).
Las palabras son generalmente muy específicas, por lo que deberás tener algún conocimiento sobre 
conceptos de tecnologías en algunos niveles como el medio 
En modo Diablo, arriesga bien: solo tienes 2 intentos. Con palabras que el 99% falla ;)

Soporte
Para soporte, reportes o sugerencias, contactar a los desarrolladores originales. Gabriel Rodrigo Enríquez 
Guerra y Fernando Alejandro Hernández Ramos 
