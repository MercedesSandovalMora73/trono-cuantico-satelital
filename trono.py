from conexion_satelital import ConexionSatelital
from nucleo_cuantico import NucleoCuantico

class TronoCuanticoSatelital:
    def __init__(self):
        self.satelite = ConexionSatelital()
        self.cuantico = NucleoCuantico()
        print(">> TRONO CUANTICO INICIADO - MERCEDES 73")
        print(f">> RED: {self.satelite.red_activa}")

    def enviar_todo(self, mensaje, destino="global"):
        seguro = self.cuantico.cifrar_post_cuantico(mensaje)
        resultado = self.satelite.enviar(seguro, destino)
        return f"ENVIADO - PRESENTE + FUTURO A {destino}: {seguro}"

if __name__ == "__main__":
    trono = TronoCuanticoSatelital()
    print(trono.enviar_todo("SOS GLOBAL MERCEDES 73 - BOGOTA", "global"))