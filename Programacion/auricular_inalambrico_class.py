class Auricular_Inalambrico:
    def __init__(self, modelo, precio, rango_alcance, duracion_bateria_horas, marca, color):
        self._modelo = modelo
        self._precio = precio
        self._rango_alcance_metros = rango_alcance
        self._duracion_bateria_horas = duracion_bateria_horas
        self._marca = marca
        self._color = color
        self._encendido = False
        self._volumen = 50
        self._bateria_restante = duracion_bateria_horas
    
    # Getters y Setters
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    def get_precio(self):
        return self._precio
    
    def set_precio(self, precio):
        self._precio = precio
    
    def get_rango_alcance_metros(self):
        return self._rango_alcance_metros
    
    def set_rango_alcance_metros(self, rango_alcance):
        self._rango_alcance_metros = rango_alcance
    
    def get_duracion_bateria(self):
        return self._duracion_bateria_horas
    
    def set_duracion_bateria(self, duracion_bateria_horas):
        self._duracion_bateria_horas = duracion_bateria_horas
    
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color

    # Comportamientos
    def encender(self, distancia_dispositivo):
        if not self._encendido and distancia_dispositivo <= self._rango_alcance_metros:
            self._encendido = True
            return (f"{self._modelo} encendido.")
        else:
            raise ValueError (f"{self._modelo} ya está encendido o fuera de alcance.")
    
    def apagar(self, distancia_dispositivo):
        if self._encendido and distancia_dispositivo <= self._rango_alcance_metros:
            self._encendido = False
            return (f"{self._modelo} apagado.")
        else:
            raise ValueError (f"{self._modelo} ya está apagado o fuera de alcance.")

    def ajustar_volumen(self, nuevo_volumen):
        if 0 <= nuevo_volumen <= 100:
            self._volumen = nuevo_volumen
            return (f"Volumen ajustado a {self._volumen}%.")
        else:
            raise ValueError ("El volumen debe estar entre 0 y 100.")

    def usar_auriculares(self, horas_uso):
        if self._encendido:
            if horas_uso <= self._bateria_restante:
                self._bateria_restante -= horas_uso
                return (f"Has usado los auriculares por {horas_uso} horas. Batería restante: {self._bateria_restante} horas.")
            else:
                raise ValueError ("No tienes suficiente batería para este tiempo de uso.")
        else:
            raise ValueError("Los auriculares están apagados, no puedes usarlos.")
    
    def conectar(self, distancia_dispositivo):
        if distancia_dispositivo <= self._rango_alcance_metros:
            return ("Auriculares conectados.")
        else:
            raise ValueError ("Fuera de rango, no se puede conectar.")

    def __str__(self):
        return (f"Auricular {self._modelo}, Marca: {self._marca}, Precio: {self._precio}$, Color: {self._color}, Batería restante: {self._bateria_restante} horas.")
