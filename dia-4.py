"""
¡Es hora de poner el árbol de Navidad en casa! 🎄 Pero este año queremos que sea especial. Vamos a crear una función que recibe la altura del árbol (un entero positivo entre 1 y 100) y un carácter especial para decorarlo.

La función debe devolver un string que represente el árbol de Navidad, construido de la siguiente manera:
- El árbol está compuesto de triángulos de caracteres especiales.
- Los espacios en blanco a los lados del árbol se representan con guiones bajos _.
- Todos los árboles tienen un tronco de dos líneas, representado por el carácter #.
- El árbol siempre debe tener la misma longitud por cada lado.
- Debes asegurarte de que el árbol tenga la forma correcta usando saltos de línea \n para cada línea.
"""

def create_xmas_tree(height, ornament):
  tree_height = height + 2
  tree_width = 0
  for i in range(0, height):
    if i > 0:
      tree_width += 2
    else:
      tree_width += 1
  tree = ''
  lvl = 1
  for i in range(tree_height):
    if i == tree_height-1 or i == tree_height-2:
      cont = 1
      while cont < tree_width + 1:
        if(cont == (tree_width//2)+1):
          tree += "#"
        else:
          tree += "_"
        cont += 1
        if(cont == tree_width + 1 and i != tree_height-1):
          tree += "\n"
    else:
      side = (tree_width-lvl) // 2
      txt = side*"_" + lvl*ornament + side*"_" + "\n"
      tree += txt
      lvl += 2
    
  return tree

print(create_xmas_tree(3, "*"))