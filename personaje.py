from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre: str, salud_maxima: float, ataque_base: float, defensa_base: float):
        if salud_maxima <= 0 or ataque_base < 0 or defensa_base < 0:
            raise ValueError("Las estadísticas deben ser valores positivos o mayores a cero.")
        
        self.nombre = nombre
        self.nivel = 1
        self.salud_maxima = float(salud_maxima)
        self.salud = float(salud_maxima)
        self.ataque_base = float(ataque_base)
        self.defensa_base = float(defensa_base)
        self._defendiendo = False

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def usar_habilidad_especial(self, objetivo=None):
        pass

    @abstractmethod
    def obtener_clase(self) -> str:
        pass

    def recibir_dano(self, cantidad: float):
        daño_recibido = cantidad
        if self._defendiendo:
            daño_recibido /= 2.0
            self._defendiendo = False  # Se consume el efecto de defensa
            
        self.salud -= daño_recibido
        if self.salud < 0:
            self.salud = 0.0
        if hasattr(self, 'log'):
            self.log(f"Recibió {daño_recibido:.1f} de daño. Salud restante: {self.salud:.1f}/{self.salud_maxima:.1f}")

    def defender(self):
        self._defendiendo = True
        if hasattr(self, 'log'):
            self.log("Se ha puesto en posición defensiva (reducirá el próximo daño a la mitad).")

    def curar(self, cantidad: float):
        self.salud += cantidad
        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima
        if hasattr(self, 'log'):
            self.log(f"Recuperó {cantidad:.1f} de salud. Salud actual: {self.salud:.1f}/{self.salud_maxima:.1f}")

    def subir_nivel(self):
        self.nivel += 1
        self.salud_maxima *= 1.2
        self.salud = self.salud_maxima
        self.ataque_base *= 1.15
        self.defensa_base *= 1.15
        if hasattr(self, 'log'):
            self.log(f"¡Ha subido al nivel {self.nivel}! Estadísticas mejoradas.")

    def esta_vivo(self) -> bool:
        return self.salud > 0

    def mostrar_info(self):
        estado = "Vivo 🟢" if self.esta_vivo() else "Derrotado 💀"
        print(f"[{self.obtener_clase()}] {self.nombre} (Nivel {self.nivel})")
        print(f"  Salud: {self.salud:.1f}/{self.salud_maxima:.1f} | Ataque: {self.ataque_base:.1f} | Defensa: {self.defensa_base:.1f}")
        print(f"  Estado: {estado} | Inventario: {getattr(self, 'inventario', [])}")

    def __str__(self):
        return f"{self.obtener_clase()} {self.nombre} (Nv. {self.nivel}) - HP: {self.salud:.1f}/{self.salud_maxima:.1f}"