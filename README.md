# Juego de Ahorcado

Este proyecto es una implementación del clásico juego de ahorcado en Python. El objetivo del juego es adivinar una palabra secreta letra por letra antes de quedarte sin intentos.

## Cómo Jugar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Cyber123-bot/JuegoAhorcado.git
   ```
2. Ejecuta el archivo `juegoahorcado.py` con Python:
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

## Requisitos

- Python 3.x
- Módulo `random`
- Módulo `os`
- Módulo `time`
- Módulo `style` (debe estar en el mismo directorio que `juegoahorcado.py`)

## Estructura del Código

- `JuegoAhorcado`: Clase principal que gestiona la lógica del juego.
  - `__init__`: Inicializa el juego.
  - `_inicializar_palabra_ahorcado`: Inicializa la palabra del ahorcado con guiones bajos.
  - `_imprimir_encabezado_juego`: Imprime el encabezado del juego con las estadísticas actuales.
  - `_obtener_entrada_usuario`: Obtiene una letra del usuario.
  - `_procesar_entrada_usuario`: Gestiona los comandos especiales del usuario.
  - `_procesar_adivinanza`: Procesa la letra adivinada por el usuario.
  - `_actualizar_palabra_ahorcado`: Actualiza la palabra del ahorcado con la letra correctamente adivinada.
  - `_imprimir_juego_perdido`: Imprime el estado del juego cuando el usuario pierde.
  - `_imprimir_juego_ganado`: Imprime el estado del juego cuando el usuario gana.
  - `iniciar_juego`: Inicia el juego.