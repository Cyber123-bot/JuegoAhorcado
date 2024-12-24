import unittest
from juego_ahorcado import JuegoAhorcado
from unittest.mock import patch

class TestJuegoAhorcado(unittest.TestCase):

    # Se ejecuta antes de cada prueba, configurando el estado inicial del juego
    def setUp(self):
        self.juego = JuegoAhorcado()
        self.juego.palabra_seleccionada = "prueba"  # Se define una palabra de prueba
        self.juego.palabra_ahorcado = self.juego._inicializarPalabraAhorcado()  # Se inicializa la palabra ahorcado con guiones bajos
        self.juego.letras_usadas = [self.juego.palabra_seleccionada[0]]  # Se usa la primera letra de la palabra al inicio

    # Test que verifica que la palabra se inicializa correctamente con guiones
    def test_inicializarPalabraAhorcado(self):
        self.assertEqual(self.juego._inicializarPalabraAhorcado(), "p_____")

    # Test que verifica el comportamiento cuando el jugador adivina correctamente una letra
    def test_procesarAdivinanza_correcta(self):
        self.juego._procesarAdivinanza("r")  # Adivina la letra 'r'
        self.assertEqual(self.juego.palabra_ahorcado, "pr____")  # Verifica que la palabra se actualizó correctamente
        self.assertIn("r", self.juego.letras_usadas)  # Verifica que la letra 'r' se agregó a letras_usadas
        self.assertEqual(self.juego.letras_adivinadas, 1)  # Verifica que el contador de letras adivinadas es 1

    # Test que verifica el comportamiento cuando el jugador adivina incorrectamente una letra
    def test_procesarAdivinanza_incorrecta(self):
        self.juego._procesarAdivinanza("x")  # Adivina una letra incorrecta 'x'
        self.assertEqual(self.juego.palabra_ahorcado, "p_____")  # La palabra no debe cambiar
        self.assertIn("x", self.juego.letras_usadas)  # Verifica que la letra 'x' se agregó a letras_usadas
        self.assertEqual(self.juego.intentos, 5)  # Verifica que los intentos se han decrementado

    # Test que verifica el comando '/m' (comando de mostrar la palabra) procesado correctamente
    @patch('builtins.input', return_value='')  # Se simula la entrada del usuario
    def test_procesarEntradaUsuario_comando_m(self, mock_input):
        self.assertTrue(self.juego._procesarEntradaUsuario("/m"))  # Verifica que el comando retorna True

    # Test que verifica que el comando '/e' (comando de exit) lance una excepción
    @patch('builtins.input', return_value='')  # Se simula la entrada del usuario
    def test_procesarEntradaUsuario_comando_e(self, mock_input):
        with self.assertRaises(SystemExit):  # Verifica que el juego termine
            self.juego._procesarEntradaUsuario("/e")

    # Test que verifica que el comando '/?' (comando de ayuda) funcione correctamente
    @patch('builtins.input', return_value='')  # Se simula la entrada del usuario
    def test_procesarEntradaUsuario_comando_interrogacion(self, mock_input):
        self.assertTrue(self.juego._procesarEntradaUsuario("/?"))  # Verifica que el comando retorne True
        self.assertTrue(self.juego._procesarEntradaUsuario("/?"))  # Verifica que el comando pueda ejecutarse múltiples veces

    # Test que verifica la actualización correcta de la palabra ahorcado cuando se adivina una letra
    def test_actualizarPalabraAhorcado(self):
        self.juego._actualizarPalabraAhorcado("r")  # Actualiza la palabra con la letra 'r'
        self.assertEqual(self.juego.palabra_ahorcado, "pr____")  # Verifica que la palabra se ha actualizado correctamente

    # Test que verifica que el juego se maneje correctamente cuando se pierde
    def test_imprimirJuegoPerdido(self):
        self.juego.intentos = 0  # Establece el contador de intentos a 0
        self.juego._imprimirJuegoPerdido()  # Llama al método que maneja el final del juego perdido
        self.assertEqual(self.juego.intentos, 0)  # Verifica que los intentos no cambien después de imprimir el mensaje

    # Test que verifica que el juego se maneje correctamente cuando se gana
    def test_imprimirJuegoGanado(self):
        self.juego.palabra_ahorcado = "prueba"  # Establece la palabra completa como adivinada
        self.juego._imprimirJuegoGanado()  # Llama al método que maneja el final del juego ganado
        self.assertEqual(self.juego.palabra_ahorcado, "prueba")  # Verifica que la palabra completa sea "prueba"

# Ejecuta las pruebas cuando este archivo es ejecutado directamente
if __name__ == "__main__":
    unittest.main()
