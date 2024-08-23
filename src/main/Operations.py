from Set import Set

class Operations:

    def __init__(self, set1):
        self.set1 = set1


    # 'union' retorna la unión de los n conjuntos.
    def union(self, other_set):
        result = Set()
        result.elements = self.set1.elements.copy()
        for element in other_set.elements:
            if element not in result.elements:
                result.add_element(element)
        return result

    # 'intersection' retorna la intersección de los n conjuntos.
    def intersection(self, other_set):
        result = Set()
        for element in self.set1.elements:
            if element in other_set.elements:
                result.add_element(element)
        return result

    # 'difference' retorna la diferencia de los n conjuntos.
    def difference(self, other_set):
        result = Set()
        for element in self.set1.elements:
            if element not in other_set.elements:
                result.add_element(element)
        return result

    # 'symmetric_difference' retorna la diferencia simétrica de los n conjuntos.
    def symmetric_difference(self, other_set):
        result = Set()
        for element in self.set1.elements:
            if element not in other_set.elements:
                result.add_element(element)
        for element in other_set.elements:
            if element not in self.set1.elements:
                result.add_element(element)
        return result

    def complement(self):
        universal_set = Set()
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            if char not in self.set1.elements:
                universal_set.add_element(char)
        return universal_set

    def __str__(self):
        return '{' + ', '.join(self.set1.elements) + '}'
