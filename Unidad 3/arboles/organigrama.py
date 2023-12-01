#árboles binarios
import anytree
from anytree import Node, RenderTree

print("Organigrama TECNM Pabellón")

root = Node("Dr. José Ernesto Olvera González (Dirección)")

level_1_child_1 = Node("Dolores Álvarez Muñoz (Subdirección de Planeación y Vinculación)", parent=root)
level_1_child_2 = Node("Ricardo Lara Colón (Subdirección Académica)", parent=root)
level_1_child_3 = Node("Victor Manuel Velasco Gallardo (Subdirección de Servicios Administrativos)", parent=root)
level_2_child_1 = Node("Julissa Elayne Cosme Castorena (Gestión Tecnológica y Vinculación)",parent = level_1_child_1)
level_2_child_2 = Node("Adriana Villegas Carrillo (Comunicación y Difusión)",parent = level_1_child_1)
level_2_child_3 = Node("Esther Betzabet Cervantes Villagrán (Planeación, Programación y Presupuestación)",parent = level_1_child_1)
level_2_child_4 = Node("Diego Jacob Dondiego Jaime (Servicios Escolares)",parent = level_1_child_1)
level_2_child_5 = Node("Uriel Luevano Hernández (Actividades Extraescolares)",parent = level_1_child_1)
level_2_child_6 = Node("Sergio Martinez Jara (Centro de Información)",parent = level_1_child_1)
level_2_child_7 = Node("Ma. Magdalena Cuevas Martinez (Ciencias Económico Administrativas)",parent = level_1_child_2)
level_2_child_8 = Node("Edgar Zacarías Moreno (Divisón de Estudios de Posgrado e Investigación)",parent = level_1_child_2)
level_2_child_9 = Node("Juana María Macías Cruz (Desarrollo Académico)",parent = level_1_child_2)
level_2_child_10 = Node("Jorge Fernando Carmona Espinoza (Ingenieria Industrial)",parent = level_1_child_2)
level_2_child_11 = Node("Nilton de Jesús Carbajal Palacios (Ciencias Básicas)",parent = level_1_child_2)
level_2_child_12 = Node("Dora María Guevara Alvarado (División de Estudios Profesionales)",parent = level_1_child_2)
level_2_child_13 = Node("Edinguer Vázquez Ayala (Departamento de Ingenierías)",parent = level_1_child_2)
level_2_child_14 = Node("Tannia Carolina Morán Bonilla (Recursos Humanos)",parent = level_1_child_3)
level_2_child_15 = Node("Alberto Díaz Juárez (Recursos Financieros)",parent = level_1_child_3)
level_2_child_16 = Node("Sergio Venegas Bravo (Recursos Materiales y Servicios)",parent = level_1_child_3)
level_2_child_17 = Node("Rafael Preciado Gutiérrez (Centro de Computo)",parent = level_1_child_3)
level_2_child_18 = Node("Raúl Llamas Esparza (Mantenimiento de Equipo)",parent = level_1_child_3)


for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))