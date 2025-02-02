import random
import os
import time
import sys
from estilos import *

class JuegoAhorcado:
    """Juego simple de Ahorcado donde el usuario debe adivinar una palabra proporcionando letras o bloques de letras."""
    # Constantes para las palabras y el número máximo de intentos
    PALABRAS = [
        "aeropuerto", "electrico", "elefante", "autopista", "educacion", "orquesta", "audiovisual", "universidad", 
        "incremento", "enfoque", "opinion", "aguila", "escalera", "ocasion", "asistente", "autonomo", "enfermera", 
        "articulo", "increible", "ideologia", "revolucionario", "extraordinario", "comunicacion", "desarrollo", 
        "iluminacion", "consideracion", "cooperacion", "anticipacion", "investigacion", "representacion", "provisto",
        "preocupacion", "evolutivo", "inauguracion", "experimentado", "compensatorio", "interesante", 
        "responsabilidad", "recuperacion", "oportunidades", "individualismo", "supervision", "restauracion", 
        "celebracion", "examinacion", "personalidad", "contribucion", "articulacion", "organizacion", 
        "legitimacion", "amplificacion", "tecnologia", "introspeccion", "generalizacion", "dignificacion", 
        "verificacion", "clarificacion", "aproximacion", "desintegracion", "internacional", "automatizacion"
    ]
    INTENTOS_MAXIMOS = 6

    def __init__(self):
        self.palabra_seleccionada = random.choice(self.PALABRAS)
        self.palabra_ahorcado = self._inicializarPalabraAhorcado()
        self.letras_adivinadas = 0
        self.letras_usadas = [self.palabra_seleccionada[0]]
        self.intentos = self.INTENTOS_MAXIMOS

    def _texto_animado(self, texto, velocidad=0.02):
        ''' Función que recibe un texto y lo imprime letra por letra con retraso especificado por el usuario (predeterminado 0.03 segundos) '''
        # Recorrer carácter por caracter el texto/frase introducida
        for char in texto:
            print(char, end="", flush=True)
            time.sleep(velocidad) # Retraso

        print() # Añadir salto de línea

    def _limpiar_terminal(self):
        ''' Función para limpiar la terminal '''
        os.system("cls" if os.name == "nt" else "clear")

    def _inicializarPalabraAhorcado(self):
        """ Inicializa palabra_ahorcado con guiones bajos para todas las letras excepto la primera """
        # Variables para la primera letra y la palabra
        primera_letra = self.palabra_seleccionada[0].lower()
        palabra = ""

        # Recorremos letra por letra
        for letra in self.palabra_seleccionada:

            # Comprobamos si la letra es igual a la primera letra
            if letra.lower() == primera_letra:
                palabra += letra # Añadimos la letra sin cambios a "palabra"

            else:
                palabra += "_" # Añadimos un guión a "palabra"

        return palabra # Retornar la palabra con los guiones bajos
                

    def _imprimirEncabezadoJuego(self):
        """ Imprime el encabezado del juego con las estadísticas actuales """
        print(color.azul + "\tJUEGO DEL AHORCADO" + color.RESET)
        print(color.amarillo + "\nNúmero de letras adivinadas:", color.purpura + str(self.letras_adivinadas) + color.RESET)
        print(color.amarillo + "Intentos restantes:", color.purpura + str(self.intentos) + color.RESET)
        print(color.amarillo + "Palabra a adivinar:", color.purpura + self.palabra_ahorcado.capitalize() + color.RESET)

    def _obtenerEntradaUsuario(self):
        """ Obtiene una letra del usuario """
        try:
            letra_usuario = input(color.azul + "\nEscribe una o varias letras [/m | /e | /r | /?]: " + color.purpura)
        
        # Si el usuario presiona Ctrl+C, salir del juego
        except KeyboardInterrupt:
            print() # Salto de línea
            self._texto_animado(color.cian + "\t¡Adiós!" + color.RESET)
            exit()
            
        return letra_usuario.lower()

    def _procesarEntradaUsuario(self, letra_usuario):
        """ Procesa la entrada del usuario """
        # Si el usuario escribe /m, mostrar las letras usadas
        if letra_usuario == "/m":
            print(color.cian + f"\nLetras usadas:", color.purpura + str(self.letras_usadas) + color.RESET)
            input(color.cian + "\nPresiona Enter para continuar..." + color.RESET)
            return True
        
        # Si el usuario escribe /e, salir del juego
        elif letra_usuario == "/e":
            self._texto_animado(color.cian + "\n\t¡Adiós!" + color.RESET)
            exit()

        # Si el usuario escribe /?, muestra la forma de jugar
        elif letra_usuario == "/?":
            self._texto_animado(color.cian + "\nDebes adivinar la palabra proporcionando una letra (o bloques de letras) que creas que está en la palabra.\n" + color.RESET)
            self._texto_animado(color.cian + "Si quieres ver las letras usadas, escribe: /m.\n" + color.RESET)
            self._texto_animado(color.cian + "Si quieres salir del juego, escribe: /e.\n" + color.RESET)
            self._texto_animado(color.cian + "Si quieres rendirte, escribe: /r.\n" + color.RESET)
            input(color.cian + "Presiona Enter para continuar..." + color.RESET)
            return True
        
        # Si el usuario escribe /r, sale pero mostrando la palabra y demás datos
        elif letra_usuario == "/r":
            self._limpiar_terminal()
            print(color.azul + "\tJUEGO DEL AHORCADO" + color.RESET)
            print(color.amarillo + "\nNúmero de letras adivinadas:", color.purpura + str(self.letras_adivinadas) + color.RESET)
            print(color.amarillo + "Intentos:", color.purpura + str(self.intentos) + color.RESET)
            print(color.amarillo + "Palabra:", color.purpura + self.palabra_seleccionada.capitalize() + color.RESET)
            self._texto_animado(color.cian + f"\n\t¡Adiós!" + color.RESET)
            exit()

        return False

    def _procesarAdivinanza(self, letra_usuario):
        """ Procesa la letra que el usuario adivinó """
        for letra in letra_usuario:
            # Comprobamos si la letra es correcta
            if letra not in (chr(l) for l in range(97, 123)):
                self._texto_animado(color.naranja + "\n\tSolo puedes introducir letras." + color.RESET)

            # Si la letra no está en la lista de usadas y es un solo carácter
            elif letra not in self.letras_usadas and len(letra) == 1:
                # Agregar la letra a la lista de letras usadas
                self.letras_usadas.append(letra)

                # Si la letra está en la palabra seleccionada
                if letra in self.palabra_seleccionada:
                    self.letras_adivinadas += 1 # Incrementar el número de letras adivinadas
                    self._actualizarPalabraAhorcado(letra) # Actualizar la palabra del ahorcado con la letra adivinada
                    self._texto_animado(color.verde + f"\n\tLa letra '{letra}' está en la palabra." + color.RESET)

                    # Imprimir un mensaje al usuario cuando gane y salir
                    if "_" not in self.palabra_ahorcado:
                        self._imprimirJuegoGanado()
                        exit()

                else:
                    # Imprimir un mensaje si la letra no está en la palabra y reducir intentos en 1
                    self._texto_animado(color.rojo + f"\n\tLa letra '{letra}' no está en la palabra." + color.RESET)
                    self.intentos -= 1

            else:
                # Imprimir un mensaje si la letra ya fue mencionada
                self._texto_animado(color.naranja + f"\n\tYa mencionaste la letra '{letra}'.\n\tPara ver las usadas, escribe: /m." + color.RESET)

    def _actualizarPalabraAhorcado(self, letra):
        """ Actualiza la palabra del ahorcado con la letra adivinada correctamente """
        self.palabra_ahorcado = ''.join([letra if self.palabra_seleccionada[i] == letra else self.palabra_ahorcado[i] 
                                         for i in range(len(self.palabra_seleccionada))])

    def _imprimirJuegoPerdido(self):
        """ Imprime el estado del juego cuando el usuario pierde """
        # Esperar 0.5 segundos y limpiar la pantalla.
        time.sleep(0.5)
        self._limpiar_terminal()

        # Imprimir el encabezado del juego y la palabra sin resolver.
        self._imprimirEncabezadoJuego()
        print(color.amarillo + "Palabra no resuelta:", color.purpura + self.palabra_seleccionada.capitalize() + color.RESET)
        self._texto_animado(color.rojo + f"\n\t¡Perdiste!" + color.RESET)

    def _imprimirJuegoGanado(self):
        """ Imprime el estado del juego cuando el usuario gana """
        # Esperar 0.5 segundos y limpiar la pantalla.
        time.sleep(0.5)
        self._limpiar_terminal()

        # Imprimir el encabezado del juego y un mensaje al usuario.
        self._imprimirEncabezadoJuego()
        self._texto_animado(color.verde + "\n\t¡Ganaste!" + color.RESET)

    def iniciarJuego(self):
        """ Inicia el juego del ahorcado """
        while self.intentos > 0:
            # Esperar 1 segundo y limpiar la pantalla.
            time.sleep(1)
            self._limpiar_terminal()

            # Imprimir el encabezado del juego y obtener la entrada del usuario.
            self._imprimirEncabezadoJuego()
            letra_usuario = self._obtenerEntradaUsuario()

            # Si la entrada no es una letra, procesarla.
            if self._procesarEntradaUsuario(letra_usuario):
                continue

            self._procesarAdivinanza(letra_usuario) # Procesar la adivinanza del usuario

        # Si no hay intentos y aún hay guiones en la palabra, imprimir el mensaje de pérdida
        if "_" in self.palabra_ahorcado:
            self._imprimirJuegoPerdido()

# Inicia el juego
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.iniciarJuego()
