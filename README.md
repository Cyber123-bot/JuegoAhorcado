# Juego del Ahorcado

Este proyecto es una implementación del clásico juego de ahorcado en Python. El objetivo del juego es adivinar una palabra secreta letra por letra (o por bloques de letras) antes de quedarte sin intentos.

## Cómo Jugar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Cyber123-bot/JuegoAhorcado.git
   ```
2. Ejecuta el archivo `juego_ahorcado.py` con Python:
    ```sh
    python juegoahorcado.py
    ```
3. El juego te mostrará una palabra con la primera letra revelada y el resto como guiones bajos.
4. Introduce una letra o bloques de letras que creas que están en la palabra.
5. Tienes un máximo de 6 intentos para adivinar la palabra completa.

## Comandos Especiales

- `/m`: Muestra las letras que ya has utilizado.
- `/e`: Salir del juego.
- `/?`: Muestra las instrucciones del juego.
- `/r`: Sale del juego, pero muestra información como: la palabra que debía adivinar, los intentos...

## Requisitos

- Python 3.x
- Módulo `random`
- Módulo `os`
- Módulo `time`
- Módulo `style` (debe estar en el mismo directorio que `juegoahorcado.py`)

## Testeo
Para asegurarte de que todo funciona correctamente puedes ejecutar el archivo `src/test.py`

## Estructura del Código

- `JuegoAhorcado`: Clase principal que gestiona la lógica del juego.
  - `__init__`: Inicializa el juego.
  - `_limpiar_terminal`: Limpia la terminal (compatibla en linux, windows y mac).
  - `_inicializarPalabraAhorcado`: Inicializa la palabra del ahorcado con guiones bajos.
  - `_imprimirEncabezadoJuego`: Imprime el encabezado del juego con las estadísticas actuales.
  - `_obtenerEntradaUsuario`: Obtiene una letra del usuario.
  - `_procesarEntradaUsuario`: Gestiona los comandos especiales del usuario.
  - `_procesarAdivinanza`: Procesa la letra adivinada por el usuario.
  - `_actualizarPalabraAhorcado`: Actualiza la palabra del ahorcado con la letra correctamente adivinada.
  - `_imprimirJuegoPerdido`: Imprime el estado del juego cuando el usuario pierde.
  - `_imprimirJuegoGanado`: Imprime el estado del juego cuando el usuario gana.
  - `iniciarJuego`: Inicia el juego.