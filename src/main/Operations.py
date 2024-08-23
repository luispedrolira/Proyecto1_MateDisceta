import Set
class Operations:
    
    # 'union' retorna la unión de los n conjuntos.
    def union(self, other_set):
        result = Set()
        result.elements = self.elements.copy()
        for element in other_set.elements:
            if element not in result.elements:
                result.add_elementent(element)
        return result

    # 'intersection' retorna la intersección de los n conjuntos.
    def intersection(self, other_set):
        result = Set()
        for element in self.elements:
            if element in other_set.elements:
                result.add_elementent(element)
        return result

    # 'difference' retorna la diferencia de los n conjuntos.
    def difference(self, other_set):
        result = Set()
        for element in self.elements:
            if element not in other_set.elements:
                result.add_elementent(element)
        return result

    '''
        'symmetric_difference' retorna la diferencia simétrica de los n conjuntos.
        Basicamente, la diferencia simétrica se puede expresar de dos maneras:
        
        1. (A - B) U (B - A)
        2. (A U B) - (A ∩ B)
        
        En este caso, se implemento la primera opción.
    '''
    def symmetric_difference(self, other_set):
        result = Set()
        for elementent in self.elements:
            if elementent not in other_set.elements:
                result.add_elementent(elementent)
        for elementent in other_set.elements:
            if elementent not in self.elements:
                result.add_elementent(elementent)
        return result

    def complement(self):
        universal_set = Set()
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            if char not in self.elements:
                universal_set.add_elementent(char)
        return universal_set

    def __str__(self):
        return '{' + ', '.join(self.elements) + '}'