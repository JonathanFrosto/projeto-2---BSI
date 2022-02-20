from src.algorithms import BruteForce
from src.inputfile import InputFileReader

input_file = InputFileReader('../matrix.txt')
drone_manager = BruteForce(input_file.get_matrix())
drone_manager.get_shortest_path()
