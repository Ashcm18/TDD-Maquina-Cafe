class MaquinaCafe:
    def __init__(self):
        self.tamanos = {
            "pequeno": 3,
            "mediano": 5,
            "grande": 7
        }

    def servir_cafe(self, tamano, azucar):
        if tamano not in self.tamanos:
            return "Tamaño inválido"

        return {
            "tamano": tamano,
            "cafe": self.tamanos[tamano],
            "azucar": azucar
        }