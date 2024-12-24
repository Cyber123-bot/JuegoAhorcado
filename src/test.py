import unittest
from juego_ahorcado import JuegoAhorcado
from unittest.mock import patch

class TestJuegoAhorcado(unittest.TestCase):

    def setUp(self):
        self.juego = JuegoAhorcado()
        self.juego.palabra_seleccionada = "prueba"
        self.juego.palabra_ahorcado = self.juego._inicializarPalabraAhorcado()
        self.juego.letras_usadas = [self.juego.palabra_seleccionada[0]]

    def test_inicializarPalabraAhorcado(self):
        self.assertEqual(self.juego._inicializarPalabraAhorcado(), "p_____")

    def test_procesarAdivinanza_correcta(self):
        self.juego._procesarAdivinanza("r")
        self.assertEqual(self.juego.palabra_ahorcado, "pr____")
        self.assertIn("r", self.juego.letras_usadas)
        self.assertEqual(self.juego.letras_adivinadas, 1)

    def test_procesarAdivinanza_incorrecta(self):
        self.juego._procesarAdivinanza("x")
        self.assertEqual(self.juego.palabra_ahorcado, "p_____")
        self.assertIn("x", self.juego.letras_usadas)
        self.assertEqual(self.juego.intentos, 5)
    @patch('builtins.input', return_value='')
    def test_procesarEntradaUsuario_comando_m(self, mock_input):
        self.assertTrue(self.juego._procesarEntradaUsuario("/m"))

    @patch('builtins.input', return_value='')
    def test_procesarEntradaUsuario_comando_e(self, mock_input):
        with self.assertRaises(SystemExit):
            self.juego._procesarEntradaUsuario("/e")

    @patch('builtins.input', return_value='')
    def test_procesarEntradaUsuario_comando_interrogacion(self, mock_input):
        self.assertTrue(self.juego._procesarEntradaUsuario("/?"))
        self.assertTrue(self.juego._procesarEntradaUsuario("/?"))

    def test_actualizarPalabraAhorcado(self):
        self.juego._actualizarPalabraAhorcado("r")
        self.assertEqual(self.juego.palabra_ahorcado, "pr____")

    def test_imprimirJuegoPerdido(self):
        self.juego.intentos = 0
        self.juego._imprimirJuegoPerdido()
        self.assertEqual(self.juego.intentos, 0)

    def test_imprimirJuegoGanado(self):
        self.juego.palabra_ahorcado = "prueba"
        self.juego._imprimirJuegoGanado()
        self.assertEqual(self.juego.palabra_ahorcado, "prueba")

if __name__ == "__main__":
    unittest.main()