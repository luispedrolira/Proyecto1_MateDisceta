import Set
class Operations:
    
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements
    
    # 'union' retorna la unión de los conjuntos.
    def union(self, other_set):
        result = Set()
        result.elements = self.elements.copy()
        for element in other_set.elements:
            if element not in result.elements:
                result.add_element(element)
        return result

    # 'intersection' retorna la intersección de los conjuntos.
    def intersection(self, other_set):
        result = Set()
        for element in self.elements:
            if element in other_set.elements:
                result.add_element(element)
        return result

    # 'difference' retorna la diferencia de los conjuntos.
    def difference(self, other_set):
        result = Set()
        for element in self.elements:
            if element not in other_set.elements:
                result.add_element(element)
        return result

    # 'symmetric_difference' retorna la diferencia simétrica de los conjuntos.
    def symmetric_difference(self, other_set):
        result = Set()
        for element in self.elements:
            if element not in other_set.elements:
                result.add_element(element)
        for element in other_set.elements:
            if element not in self.elements:
                result.add_element(element)
        return result

    # 'complement' retorna el complemento del conjunto en relación con un conjunto universal.
    def complement(self):
        universal_set = Set()
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            if char not in self.elements:
                universal_set.add_element(char)
        return universal_set

    def __str__(self):
        return '{' + ', '.join(self.elements) + '}'