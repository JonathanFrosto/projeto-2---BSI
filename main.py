from delivery import Delivery


delivery = Delivery()
shortest_path = delivery.get_shortest_path()

shortest_path_str = ''
for element in shortest_path:
    shortest_path_str += str(element)

print(shortest_path_str)
