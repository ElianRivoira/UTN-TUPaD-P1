class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None


class ContactTree:
    def __init__(self):
        self.root = None

    def insert(self, contact):
        def _insert(node, contact):
            if not node:
                return Node(contact)
            if contact.name.lower() < node.contact.name.lower():
                node.left = _insert(node.left, contact)
            elif contact.name.lower() > node.contact.name.lower():
                node.right = _insert(node.right, contact)
            else:
                # Si el nombre ya existe, actualizar el teléfono
                node.contact.phone = contact.phone
                print(f"Contacto '{contact.name}' actualizado.")
            return node

        self.root = _insert(self.root, contact)

    def search(self, name):
        def _search(node, name):
            if not node:
                return None
            if name.lower() == node.contact.name.lower():
                return node.contact
            elif name.lower() < node.contact.name.lower():
                return _search(node.left, name)
            else:
                return _search(node.right, name)

        return _search(self.root, name)

    def delete(self, name):
        def _find_min(node):
            """Encuentra el nodo con el valor mínimo (más a la izquierda)"""
            while node.left:
                node = node.left
            return node

        def _delete(node, name):
            if not node:
                return None
            
            name_lower = name.lower()
            node_name_lower = node.contact.name.lower()
            
            if name_lower < node_name_lower:
                node.left = _delete(node.left, name)
            elif name_lower > node_name_lower:
                node.right = _delete(node.right, name)
            else:
                # Nodo encontrado - casos de eliminación
                
                # Caso 1: Nodo sin hijos (hoja)
                if not node.left and not node.right:
                    return None
                
                # Caso 2: Nodo con un solo hijo
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # Caso 3: Nodo con dos hijos
                # Opción A: Reemplazar con el sucesor inorden (mínimo del subárbol derecho)
                else:
                    successor = _find_min(node.right)
                    # Reemplazar el contacto del nodo actual con el del sucesor
                    node.contact = successor.contact
                    # Eliminar el sucesor del subárbol derecho
                    node.right = _delete(node.right, successor.contact.name)
            
            return node

        initial_count = self.count_contacts()
        self.root = _delete(self.root, name)
        final_count = self.count_contacts()
        
        if initial_count > final_count:
            print(f"✅ Contacto '{name}' eliminado exitosamente.")
            return True
        else:
            print(f"❌ No se encontró ningún contacto con el nombre '{name}'.")
            return False

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(str(node.contact))
                _inorder(node.right)
        _inorder(self.root)
        return result

    def count_contacts(self):
        def _count(node):
            if not node:
                return 0
            return 1 + _count(node.left) + _count(node.right)
        return _count(self.root)


def mostrar_menu():
    print("\n" + "="*50)
    print("         AGENDA DE CONTACTOS - ABB")
    print("="*50)
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Estadísticas")
    print("6. Cargar contactos de ejemplo")
    print("7. Salir")
    print("="*50)


def agregar_contacto(tree):
    print("\n--- AGREGAR NUEVO CONTACTO ---")
    try:
        nombre = input("Ingrese el nombre: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            return
        
        # Validar que el nombre no sea solo números
        if nombre.isdigit():
            print("❌ El nombre no puede ser solo números.")
            return
        
        # Validar que el nombre contenga al menos una letra
        if not any(char.isalpha() for char in nombre):
            print("❌ El nombre debe contener al menos una letra.")
            return
        
        telefono = input("Ingrese el teléfono: ").strip()
        if not telefono:
            print("❌ El teléfono no puede estar vacío.")
            return
        
        # Validar que el teléfono contenga solo números
        if not telefono.isdigit():
            print("❌ El teléfono debe contener solo números.")
            return
        
        contacto = Contact(nombre, telefono)
        tree.insert(contacto)
        print(f"✅ Contacto '{nombre}' agregado exitosamente.")
        
    except Exception as e:
        print(f"❌ Error al agregar contacto: {e}")


def buscar_contacto(tree):
    print("\n--- BUSCAR CONTACTO ---")
    nombre = input("Ingrese el nombre a buscar: ").strip()
    
    if not nombre:
        print("❌ Debe ingresar un nombre para buscar.")
        return
    
    contacto = tree.search(nombre)
    if contacto:
        print(f"✅ Contacto encontrado: {contacto}")
    else:
        print(f"❌ No se encontró ningún contacto con el nombre '{nombre}'.")


def eliminar_contacto(tree):
    print("\n--- ELIMINAR CONTACTO ---")
    
    # Mostrar contactos disponibles
    contactos = tree.inorder()
    if not contactos:
        print("📝 No hay contactos en la agenda para eliminar.")
        return
    
    print("Contactos disponibles:")
    print("-" * 30)
    for i, contacto in enumerate(contactos, 1):
        print(f"{i:2d}. {contacto}")
    
    print("-" * 30)
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    
    if not nombre:
        print("❌ Debe ingresar un nombre para eliminar.")
        return
    
    # Confirmar eliminación
    contacto = tree.search(nombre)
    if contacto:
        print(f"Se eliminará el contacto: {contacto}")
        confirmacion = input("¿Está seguro? (s/n): ").strip().lower()
        if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
            tree.delete(nombre)
        else:
            print("❌ Eliminación cancelada.")
    else:
        print(f"❌ No se encontró ningún contacto con el nombre '{nombre}'.")


def mostrar_contactos(tree):
    print("\n--- LISTA DE CONTACTOS (ORDEN ALFABÉTICO) ---")
    contactos = tree.inorder()
    
    if not contactos:
        print("📝 No hay contactos en la agenda.")
        return
    
    print(f"Total de contactos: {len(contactos)}")
    print("-" * 40)
    for i, contacto in enumerate(contactos, 1):
        print(f"{i:2d}. {contacto}")


def mostrar_estadisticas(tree):
    print("\n--- ESTADÍSTICAS DE LA AGENDA ---")
    total = tree.count_contacts()
    print(f"📊 Total de contactos: {total}")
    
    if total > 0:
        contactos = tree.inorder()
        primer_contacto = contactos[0].split(":")[0]
        ultimo_contacto = contactos[-1].split(":")[0]
        print(f"📝 Primer contacto (alfabéticamente): {primer_contacto}")
        print(f"📝 Último contacto (alfabéticamente): {ultimo_contacto}")


def cargar_contactos_ejemplo(tree):
    print("\n--- CARGANDO CONTACTOS DE EJEMPLO ---")
    contactos_ejemplo = [
        ("Ana", "123456"),
        ("Luis", "654321"),
        ("Nicolas", "111111"),
        ("Marta", "222222"),
        ("Jorge", "345678"),
        ("Gabriel", "987654"),
        ("Silvia", "999999"),
    ]
    
    for nombre, telefono in contactos_ejemplo:
        tree.insert(Contact(nombre, telefono))
    
    print(f"✅ Se cargaron {len(contactos_ejemplo)} contactos de ejemplo.")


def main():
    tree = ContactTree()
    
    print("🌟 ¡Bienvenido a la Agenda de Contactos con Árbol Binario de Búsqueda!")
    print("Esta aplicación organiza automáticamente tus contactos en orden alfabético.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción (1-7): ").strip()
            match opcion:
              case "1":
                agregar_contacto(tree)
              case "2":
                buscar_contacto(tree)
              case "3":
                mostrar_contactos(tree)
              case "4":
                eliminar_contacto(tree)
              case "5":
                mostrar_estadisticas(tree)
              case "6":
                cargar_contactos_ejemplo(tree)
              case "7":
                print("\n👋 ¡Gracias por usar la Agenda de Contactos!")
                print("Desarrollado con Árboles Binarios de Búsqueda - TUP")
                break
              case _:
                print("❌ Opción inválida. Por favor, seleccione una opción del 1 al 7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()