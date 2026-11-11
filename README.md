# ⚔️ Videojuego RPG por Turnos (Programación Orientada a Objetos)

Proyecto desarrollado para la actividad de programación orientada a objetos, aplicando conceptos avanzados como **clases abstractas, interfaces, herencia múltiple, mixins y polimorfismo puro** en Python.

---

## 📁 Estructura del Proyecto

El proyecto está organizado de forma modular para garantizar escalabilidad y buenas prácticas de arquitectura de software:

```text
videojuego_rpg/
│
├── main.py                  # Menú interactivo y simulación de batallas
└── clases/
    ├── __init__.py          # Paquete de clases
    ├── personaje.py         # Clase abstracta base (Personaje)
    ├── interfaces.py        # Contratos (IAtacante, IDefensor, ICurable, IHabilidadEspecial)
    ├── mixins.py            # Funcionalidad transversal (LogMixin, InventarioMixin)
    └── clases_concretas.py  # Clases concretas (Guerrero, Mago, Arquero, Sanador)