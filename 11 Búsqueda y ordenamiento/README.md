# 🌳 Agenda de Contactos con Árbol Binario de Búsqueda (ABB) - Trabajo Integrador

> Trabajo Integrador - Programación I | Estructuras de Datos Avanzadas en Python

> Comisión 20

> Integrantes:
      - Elian Rivoira
      - Juan Francisco Reales

---

## 📌 Descripción

Este proyecto implementa una **estructura de Árbol Binario de Búsqueda (ABB)** en Python para simular una **agenda de contactos**. Cada contacto es almacenado en el árbol de forma ordenada alfabéticamente, permitiendo búsquedas e inserciones eficientes.

El objetivo del trabajo fue:
- Comprender y aplicar la estructura ABB.
- Desarrollar un caso práctico funcional en Python.
- Integrar teoría, desarrollo y reflexión sobre el aprendizaje.

---

## 🧠 Marco Teórico (Resumen)

Un **árbol binario de búsqueda** es una estructura jerárquica que organiza datos de forma tal que:

- Los nodos a la izquierda son menores que el nodo actual.
- Los nodos a la derecha son mayores.
  
Esto permite operaciones como búsqueda, inserción y eliminación en tiempo promedio **O(log n)**.

📚 Ver el documento de investigación completo para el marco teórico ampliado.

---

## 🛠️ Funcionalidades

- ✅ Insertar nuevos contactos (nombre y teléfono).
- 🔍 Buscar contactos por nombre.
- 📃 Listar todos los contactos en orden alfabético (recorrido inorden).
- ✨ Código limpio y documentado.

---

## 🧪 Ejemplo de Uso - Contexto Aplicado

Imaginemos que estamos desarrollando una **agenda digital** en una aplicación de escritorio o móvil. Esta agenda almacena cientos o miles de contactos que los usuarios pueden buscar por nombre, agregar nuevos o consultar de forma ordenada.

Aquí es donde un **Árbol Binario de Búsqueda (ABB)** se vuelve una excelente opción:

- Cuando un usuario **agrega un nuevo contacto**, el ABB lo inserta manteniendo el orden alfabético automáticamente.
- Si el usuario **busca un contacto específico por nombre**, el ABB permite encontrarlo rápidamente sin recorrer toda la agenda, gracias a su estructura jerárquica.
- Cuando se desea **mostrar todos los contactos ordenados alfabéticamente**, el recorrido inorden del árbol lo hace posible sin necesidad de ordenar manualmente.

A diferencia de una lista común, donde cada búsqueda requeriría recorrer todos los elementos (O(n)), el ABB optimiza esta operación a O(log n) en promedio, lo cual mejora notablemente el rendimiento a medida que crece la cantidad de datos.

Este tipo de estructura se adapta muy bien a sistemas donde se requiere **eficiencia, ordenamiento y escalabilidad**, como agendas, catálogos, inventarios, o incluso índices de bases de datos.

---

## 🧠 Reflexión Grupal y Conclusiones

Este trabajo nos permitió comprender en profundidad la importancia de las estructuras de datos avanzadas, en particular el Árbol Binario de Búsqueda (ABB), como herramienta fundamental para organizar y acceder eficientemente a la información.

### 🔍 Aprendizajes clave

- Entendimos el funcionamiento interno de los árboles y cómo aplicarlos en un contexto real como una agenda de contactos.
- Vimos cómo el recorrido inorden nos permite obtener resultados naturalmente ordenados.
- Identificamos los beneficios del ABB frente a listas tradicionales en cuanto a eficiencia.
- Reforzamos conceptos de programación orientada a objetos en Python y modularización del código.

### 💡 Desafíos y soluciones

- Tuvimos que analizar bien cómo organizar la inserción y búsqueda respetando las reglas del ABB.
- Nos ayudamos mutuamente revisando el código y optimizando la lógica para que fuera clara y funcional.
- Trabajamos de manera colaborativa usando Git, lo cual nos permitió versionar y organizar nuestras tareas.

### 🎯 Conclusión

Aplicar estructuras como los árboles no solo mejora el rendimiento de los programas, sino que también nos obliga a pensar de forma lógica y organizada. Este tipo de prácticas nos prepara para desafíos reales en el mundo del desarrollo de software.

Nos vamos de este trabajo con una mejor comprensión de los árboles, más confianza en el uso de Python, y habilidades reforzadas para trabajar en equipo y documentar proyectos.

## Video explicativo

https://www.youtube.com/watch?v=8mXYOfO2xXE