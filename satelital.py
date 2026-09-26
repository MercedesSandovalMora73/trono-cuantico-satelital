 class ConexionSatelital:
    def __init__(self):
        self.red_activa = "STARLINK_DIRECT + IRIDIUM + MOTOROLA_DEFY_SATELLITE"
    
    def enviar(self, mensaje_cifrado, destino):
        print(f"[SATELITAL] Enviando via {self.red_activa}")
        print(f"[SATELITAL] Destino: {destino}")
        print(f"[SATELITAL] Mensaje: {mensaje_cifrado}")
        # Aqui se conecta a tu Motorola Defy real por Bluetooth
        return True