# Planificador de Actividades 

Proyecto final en Python con interfaz gráfica (Tkinter) y recordatorios automáticos (APScheduler).
Fundamentación Hacer una planificación de actividades en Python es una buena forma de practicar la programación mientras resolvemos algo útil. Con este lenguaje se pueden automatizar tareas, organizar fechas y manejar listas de actividades sin complicaciones. Además, usar Python para planificar ayuda a mejorar la lógica, la organización y el uso de librerías que son comunes en proyectos reales. El royecto es una aplicación de Python con interfaz gráfica de escritorio, de contexto abierto, vinculada a lo educativo con archivo CSV y repositorio en Github. Objetivos • Aplicar lo aprendido en programación a un caso práctico. • Organizar tareas y tiempos de forma más eficiente usando Python. • Usar librerías como datetime o agenda para manejar fechas y horarios. • Desarrollar hábitos de planificación y trabajo ordenado dentro de un proyecto.

Autores María Collazo y Carolina Bastida

## Funcionalidad
- Agregar, listar y eliminar tareas.
- Guardado automático en archivo JSON.
- Recordatorios programados según fecha/hora.
- Interfaz simple e intuitiva.

## Ejecución
```bash
pip install -r requirements.txt
python main.py
```

## Estructura
```
planificador_estudiante/
  gui.py
  logic.py
  storage.py
  reminder.py
  main.py
  data/tareas.json
  tests/test_logic.py
```
## JUstificación
Cada librería tuvo su propósito y juntas hicieron que el programa fuera completo:
Tkinter le dio una interfaz visual.
JSON permitió guardar los datos.
APScheduler agregó automatización.
Pytest ayudó a comprobar que todo funcione bien.
Con estas herramientas pudimos cumplir con todos los puntos del proyecto y aprender cómo combinar varias partes de Python en una sola aplicación.

## Fundamentación
Durante el desarrollo de este proyecto se ha aprendido a combinar distintas librerías de Python para crear una aplicación completa, con interfaz gráfica, almacenamiento de datos y recordatorios automáticos. Al principio fue un gran desafío lograr que todo funcione, especialmente la parte de guardar las tareas y programar los avisos, pero con práctica y pruebas logramos entender cómo se comunican los módulos entre sí. 
El uso de Tkinter nos permitió mejorar la presentación de la aplicación y hacerla más fácil. También aprendimos a trabajar con archivos JSON para guardar información de manera persistente, algo muy útil en programas reales.
Además,incluir pruebas con pytest nos ayudó a comprobar que las funciones del programa funcionan correctamente antes de entregar el trabajo.
Hemos logrado aprender los conocimientos de programación vistos en clase, entender mejor la importancia del diseño modular y valorar la práctica de documentar el código.
En resumen, nos dejó una experiencia muy completa, donde pudimos crear una herramienta funcional y a la vez seguir aprendiendo sobre cómo planificar, estructurar y mantener un proyecto de software.

