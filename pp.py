class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores deben tener la misma longitud para sumarlos")
        result = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores deben tener la misma longitud para restarlos")
        result = [a - b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores deben tener la misma longitud para multiplicarlos elemento a elemento")
        result = [a * b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __matmul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores deben tener la misma longitud para calcular el producto punto")
        result = sum(a * b for a, b in zip(self.values, other.values))
        return result
    def __getitem__(self, index):
        return self.values[index]
   
    def __setitem__(self, index, value):
        self.values[index] = value

    def __eq__(self, other):
        return self.values == other.values
