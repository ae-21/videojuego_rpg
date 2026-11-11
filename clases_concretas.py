import random
from .personaje import Personaje
from .interfaces import IAtacante, IDefensor, ICurable, IHabilidadEspecial
from .mixins import LogMixin, InventarioMixin

class Guerrero(Personaje, IAtacante, IDefensor, IHabilidadEspecial, LogMixin, InventarioMixin):
    def __init__(self, nombre):
        super().__init__(nombre=nombre, salud_maxima=120.0, ataque_base=25.0, defensa_base=20.0)

    def obtener_clase(self) -> str:
        return "Guerrero"

    def atacar(self, objetivo):
        daño = self.ataque_base * 1.5
        self.log(f"Ataca con espada a {objetivo.nombre} infiriendo {daño:.1f} de daño.")
        objetivo.recibir_dano(daño)

    def defender(self):
        super().defender()

    def obtener_defensa_total(self) -> float:
        return self.defensa_base * (1.5 if self._defendiendo else 1.0)

    def usar_habilidad_especial(self, objetivo=None):
        if objetivo:
            daño = self.ataque_base * 2.0
            self.log(f"¡Usa 'Golpe Aplastante' contra {objetivo.nombre} causando {daño:.1f} de daño!")
            objetivo.recibir_dano(daño)
            self.defensa_base *= 0.8
        else:
            self.log("¡Usa 'Golpe Aplastante', pero no hay objetivo válido!")

    def obtener_costo_habilidad(self) -> float:
        return 0.0


class Mago(Personaje, IAtacante, ICurable, IHabilidadEspecial, LogMixin, InventarioMixin):
    def __init__(self, nombre):
        super().__init__(nombre=nombre, salud_maxima=80.0, ataque_base=35.0, defensa_base=8.0)

    def obtener_clase(self) -> str:
        return "Mago"

    def atacar(self, objetivo):
        daño = self.ataque_base * 2.0
        self.log(f"Lanza rayo mágico a {objetivo.nombre} ignorando defensas, causando {daño:.1f} de daño.")
        objetivo.salud -= daño
        if objetivo.salud < 0:
            objetivo.salud = 0.0

    def curar_aliado(self, aliado, cantidad=30.0):
        self.log(f"Lanza hechizo de curación sobre su aliado {aliado.nombre}.")
        aliado.curar(cantidad)

    def revivir(self, aliado):
        if not aliado.esta_vivo():
            aliado.salud = aliado.salud_maxima * 0.5
            self.log(f"¡Ha revivido a {aliado.nombre} con el 50% de salud!")
        else:
            self.log(f"{aliado.nombre} ya está vivo.")

    def usar_habilidad_especial(self, objetivo=None):
        daño = self.ataque_base * 2.5
        self.log(f"¡Invoca 'Bola de Fuego' en área causando {daño:.1f} de daño!")
        if objetivo:
            objetivo.recibir_dano(daño)

    def obtener_costo_habilidad(self) -> float:
        return 10.0


class Arquero(Personaje, IAtacante, IHabilidadEspecial, LogMixin, InventarioMixin):
    def __init__(self, nombre):
        super().__init__(nombre=nombre, salud_maxima=95.0, ataque_base=30.0, defensa_base=12.0)

    def obtener_clase(self) -> str:
        return "Arquero"

    def atacar(self, objetivo):
        daño = self.ataque_base * 1.2
        self.log(f"Dispara flecha precisa a {objetivo.nombre} causando {daño:.1f} de daño.")
        objetivo.recibir_dano(daño)

    def usar_habilidad_especial(self, objetivo=None):
        if objetivo:
            critico = random.choice([True, False])
            multiplicador = 3.0 if critico else 1.5
            daño = self.ataque_base * multiplicador
            tipo = "¡GOLPE CRÍTICO! 🎯" if critico else "Disparo certero"
            self.log(f"Usa '{tipo}' con arco sobre {objetivo.nombre} infligiendo {daño:.1f} de daño.")
            objetivo.recibir_dano(daño)

    def obtener_costo_habilidad(self) -> float:
        return 5.0


class Sanador(Personaje, ICurable, IDefensor, IHabilidadEspecial, LogMixin, InventarioMixin):
    def __init__(self, nombre):
        super().__init__(nombre=nombre, salud_maxima=110.0, ataque_base=15.0, defensa_base=15.0)

    def obtener_clase(self) -> str:
        return "Sanador"

    def atacar(self, objetivo):
        daño = self.ataque_base * 1.0
        self.log(f"Golpea con báculo a {objetivo.nombre} causando {daño:.1f} de daño.")
        objetivo.recibir_dano(daño)

    def defender(self):
        super().defender()

    def obtener_defensa_total(self) -> float:
        return self.defensa_base * (1.5 if self._defendiendo else 1.0)

    def curar_aliado(self, aliado, cantidad=40.0):
        self.log(f"Canaliza luz divina para curar a {aliado.nombre}.")
        aliado.curar(cantidad)

    def revivir(self, aliado):
        if not aliado.esta_vivo():
            aliado.salud = aliado.salud_maxima
            self.log(f"¡Milagro! Ha revivido por completo a {aliado.nombre}.")

    def usar_habilidad_especial(self, objetivo=None):
        self.log("¡Emite una 'Bendición' general de apoyo!")

    def obtener_costo_habilidad(self) -> float:
        return 15.0