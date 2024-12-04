"""
Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.
Reglas:
Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
Cada nombre debe estar en una línea, alineado a la izquierda.
El marco está construido con * y tiene un borde de una línea de ancho.
La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado.
"""

def create_frame(names):
    width = get_width(names)
    height = len(names)
    frame = "*" * (width+2) + "\n"
    for i in range(0, height):
        frame += "* " + names[i]
        w = len(names[i]) + 1
        while w < width-1:
            frame += " "
            w += 1
        frame += " *" + "\n"
    frame += "*" * (width+2)
    return frame

def get_width(names):
    width = 0
    for name in names:
        if len(name) > width:
            width = len(name)
    
    return width + 2


print(create_frame(['midu', 'madeval', 'educalvolpz']))