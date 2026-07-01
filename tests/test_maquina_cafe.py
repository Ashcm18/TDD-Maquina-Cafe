import unittest
from maquina_cafe import MaquinaCafe


class TestMaquinaCafe(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaCafe()

    def test_vaso_pequeno(self):
        resultado = self.maquina.servir_cafe("pequeno", 2)
        self.assertEqual(resultado["cafe"], 3)

    def test_vaso_mediano(self):
        resultado = self.maquina.servir_cafe("mediano", 1)
        self.assertEqual(resultado["cafe"], 5)

    def test_vaso_grande(self):
        resultado = self.maquina.servir_cafe("grande", 3)
        self.assertEqual(resultado["cafe"], 7)

    def test_tamano_invalido(self):
        resultado = self.maquina.servir_cafe("gigante", 2)
        self.assertEqual(resultado, "Tamaño inválido")


if __name__ == "__main__":
    unittest.main()