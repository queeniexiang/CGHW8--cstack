from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 12, 125 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'my_script', edges, polygons, transform, screen, color )
