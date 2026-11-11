import random
from clases.clases_concretas import Guerrero, Mago, Arquero, Sanador

def batalla(equipo1, equipo2):
    """Simula una batalla por turnos entre dos equipos (polimorfismo puro)."""
    turno = 1
    while any(p.esta_vivo() for p in equipo1) and any(p.esta_vivo() for p in equipo2):
        print(f"\n" + "="*50)
        print(f"⚔️ TURNO {turno}")
        print(f"="*50)
        
        # Turno del equipo 1
        for personaje in equipo1:
            if personaje.esta_vivo() and any(p.esta_vivo() for p in equipo2):
                enemigos = [p for p in equipo2 if p.esta_vivo()]
                
                accion = random.choices(["atacar", "habilidad", "defender"], weights=[0.6, 0.3, 0.1])[0]
                
                if accion == "atacar" and enemigos:
                    objetivo = random.choice(enemigos)
                    personaje.atacar(objetivo)
                elif accion == "habilidad" and hasattr(personaje, 'usar_habilidad_especial'):
                    objetivo = random.choice(enemigos) if enemigos else None
                    personaje.usar_habilidad_especial(objetivo)
                elif accion == "defender" and hasattr(personaje, 'defender'):
                    personaje.defender()
                elif enemigos:
                    personaje.atacar(random.choice(enemigos))
        
        # Turno del equipo 2
        for personaje in equipo2:
            if personaje.esta_vivo() and any(p.esta_vivo() for p in equipo1):
                enemigos = [p for p in equipo1 if p.esta_vivo()]
                
                accion = random.choices(["atacar", "habilidad", "defender"], weights=[0.6, 0.3, 0.1])[0]
                
                if accion == "atacar" and enemigos:
                    objetivo = random.choice(enemigos)
                    personaje.atacar(objetivo)
                elif accion == "habilidad" and hasattr(personaje, 'usar_habilidad_especial'):
                    objetivo = random.choice(enemigos) if enemigos else None
                    personaje.usar_habilidad_especial(objetivo)
                elif accion == "defender" and hasattr(personaje, 'defender'):
                    personaje.defender()
                elif enemigos:
                    personaje.atacar(random.choice(enemigos))
        
        turno += 1
    
    print(f"\n" + "="*50)
    if any(p.esta_vivo() for p in equipo1):
        print("🏆 ¡EQUIPO 1 GANA LA BATALLA!")
    else:
        print("🏆 ¡EQUIPO 2 GANA LA BATALLA!")
    print("="*50)

def main():
    personajes_creados = []
    
    while True:
        print("\n" + "🎮 MENÚ PRINCIPAL - VIDEOJUEGO RPG 🎮")
        print("1. Crear personaje")
        print("2. Ver personajes")
        print("3. Simular batalla")
        print("4. Ver estadísticas por tipo")
        print("5. Salir")
        
        try:
            opcion = int(input("\nElige una opción (1-5): "))
        except ValueError:
            print("⚠️ Error: Ingresa un número válido del 1 al 5.")
            continue
            
        if opcion == 1:
            print("\n--- CREAR NUEVO PERSONAJE ---")
            print("Tipos disponibles: Guerrero, Mago, Arquero, Sanador")
            tipo = input("Ingresa el tipo de personaje: ").strip().capitalize()
            
            if tipo not in ["Guerrero", "Mago", "Arquero", "Sanador"]:
                print("❌ Tipo de personaje inválido. Intenta de nuevo.")
                continue
                
            nombre = input("Ingresa el nombre del personaje: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                continue
                
            try:
                if tipo == "Guerrero":
                    p = Guerrero(nombre)
                elif tipo == "Mago":
                    p = Mago(nombre)
                elif tipo == "Arquero":
                    p = Arquero(nombre)
                elif tipo == "Sanador":
                    p = Sanador(nombre)
                
                personajes_creados.append(p)
                p.agregar_item("Poción de vida")
                print(f"✅ ¡Personaje {tipo} '{nombre}' creado con éxito!")
            except Exception as e:
                print(f"❌ Error al crear el personaje: {e}")
                
        elif opcion == 2:
            print("\n--- LISTA DE PERSONAJES REGISTRADOS ---")
            if not personajes_creados:
                print("No hay personajes creados todavía.")
            else:
                for idx, p in enumerate(personajes_creados, 1):
                    print(f"\n[{idx}] ", end="")
                    p.mostrar_info()
                    
        elif opcion == 3:
            print("\n--- SIMULACIÓN DE BATALLA ---")
            if len(personajes_creados) < 2:
                print("⚠️ Necesitas al menos 2 personajes creados para simular una batalla.")
                continue
                
            try:
                num_por_equipo = int(input(f"¿Cuántos personajes por equipo? (Disponibles: {len(personajes_creados)} en total): "))
                if num_por_equipo < 1 or num_por_equipo * 2 > len(personajes_creados):
                    print("⚠️ Cantidad inválida según los personajes disponibles.")
                    continue
                
                copia_personajes = list(personajes_creados)
                random.shuffle(copia_personajes)
                
                equipo1 = copia_personajes[:num_por_equipo]
                equipo2 = copia_personajes[num_por_equipo:num_por_equipo*2]
                
                print("\n🛡️ EQUIPO 1:")
                for p in equipo1:
                    print(f" - {p}")
                print("\n⚔️ EQUIPO 2:")
                for p in equipo2:
                    print(f" - {p}")
                    
                input("\nPresiona Enter para iniciar la batalla...")
                batalla(equipo1, equipo2)
                
            except ValueError:
                print("⚠️ Ingresa un número entero válido.")
                
        elif opcion == 4:
            print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
            conteo = {"Guerrero": 0, "Mago": 0, "Arquero": 0, "Sanador": 0}
            for p in personajes_creados:
                tipo = p.obtener_clase()
                if tipo in conteo:
                    conteo[tipo] += 1
            
            print(f"Total de personajes: {len(personajes_creados)}")
            for tipo, cantidad in conteo.items():
                print(f" - {tipo}s: {cantidad}")
                
        elif opcion == 5:
            print("\n👋 ¡Gracias por jugar! Saliendo del programa...")
            break
        else:
            print("⚠️ Opción fuera de rango. Elige entre 1 y 5.")

if __name__ == "__main__":
    main()