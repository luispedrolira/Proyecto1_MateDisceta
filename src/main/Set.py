class Set:
    # '__init__' es el constructor que inicializa la lista de elementos.
    def __init__(self): 
        self.elements = []
    
    # 'add_element' agrega un elemento a la lista de elementos. 
    def add_element(self, element):
        if element not in self.elements:
            self.elements.append(element)

    # 'remove_element' remueve un elemento de la lista de elementos.
    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)

    # 'contains' verifica si un elemento está en la lista de elementos.
    def contains(self, element):
        return element in self.elements