from random import random
from random import randint

class Matrix:
    
    # Instantiate the class
    def __init__(self, rows, columns, name = "matrix"):
        
        self.name = name
        self.rows = rows
        self.columns = columns
        self.shape = (rows, columns)
        self.data = []
        
        for i in range(self.rows):
            rowList = []
            for j in range(self.columns):
                rowList.append(0.0)
            self.data.append(rowList)

    def log(self):
        print(str(self.name))
        for i in self.data:
            print(i)
        print("-----------")
        
    @staticmethod
    def static_multiply(a, b):
        try:
            b.rows
        except:
            output = Matrix(a.rows, a.columns, name = "Scalar")
            for i in range(a.rows):
                for j in range(a.columns):
                    output.data[i][j] = a.data[i][j] * b
            return output
        
        if a.columns == b.rows:
            output = Matrix(a.rows, b.columns, name = "Dot")
            for i in range(a.rows):
                for j in range(b.columns):
                    inner_product = 0
                    for k in range(a.columns):
                        inner_product += (a.data[i][k] * b.data[k][j])
                    output.data[i][j] = inner_product
            return output
        
        elif a.rows == b.rows and a.columns == b.columns:
            output = Matrix(a.rows, a.columns, name = "Hadamard")    
            for i in range (a.rows):
                for j in range(a.columns):
                    output.data[i][j] = a.data[i][j] * b.data[i][j]
            return output

        else:
            return "Matrices of dimensions" + str(a.shape) + " and " + str(b.shape) + " can't be multiplied"
        


    @staticmethod
    def static_add(a, b):
        
        if isinstance(b, int) or isinstance(b, float):
            output = Matrix(a.rows, a.columns, name = "Scalar")
            for i in range(a.rows):
                for j in range(a.columns):
                    output.data[i][j] = a.data[i][j] + b
            return output   

        elif a.shape == b.shape:
            output = Matrix(a.rows, a.columns, name = "Sum")
            for i in range(a.rows):
                for j in range(a.columns):
                    output.data[i][j] = a.data[i][j] + b.data[i][j]
            return output
        
        else:
            raise Exception("FormatError")

    @staticmethod
    def static_transpose(a):
        output = Matrix(a.columns, a.rows)
        for i in range(a.rows):
            for j in range(a.columns):
                output.data[j][i] = a.data[i][j]
        return output
    
    @staticmethod
    def static_fromArray(array):
        
        try:
            len(array[0])
        except:
            output = Matrix(len(array), 1)
            for i in range(len(array)):
                output.data[i][0] = array[i]
            return output
            

        for i in range(len(array)):
            if len(array[i]) != len(array[0]):
                return
        
    
        arrayColumns = len(array[0])
        arrayRows = len(array)
        output = Matrix(arrayRows, arrayColumns)
        for i in range(arrayRows):
            for j in range(arrayColumns):
                output.data[i][j] = array[i][j]
        return output

    @staticmethod
    def static_toArray(array):
        arr = ([])
        for i in range(array.rows):
            row = []
            for j in range(array.columns):
                row.append(array.data[i][j])
            arr.append(row)
        return arr

    @staticmethod
    def static_substract(a, b):
        
        if isinstance(b, int) or isinstance(b, float):
            output = Matrix(a.rows, a.columns, name = "Scalar")
            for i in range(a.rows):
                for j in range(a.columns):
                    output.data[i][j] = a.data[i][j] - b
            return output               
        

        elif a.shape == b.shape:
            output = Matrix(a.rows, a.columns, name = "Substract")
            for i in range(a.rows):
                for j in range(a.columns):
                    output.data[i][j] = a.data[i][j] - b.data[i][j]
            return output
        
        else:
            raise Exception("FormatError")

    @staticmethod
    def static_map(x, func):
        out = Matrix(x.rows, x.columns)
        for i in range(x.rows):
            for j in range(x.columns):
                val = x.data[i][j]
                out.data[i][j] = func(val)
        return out

    def map(self, func):
        for i in range(self.rows):
            for j in range(self.columns):
                val = self.data[i][j]
                self.data[i][j] = func(val)

    def multiply(self, b):
        
        try:
            b.rows
        except:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.data[i][j] = self.data[i][j] * b
            return
        
        # Dot method
        if self.columns == b.rows:
            output = Matrix(self.rows, b.columns, name = "Dot")
            for i in range(self.rows):
                for j in range(b.columns):
                    inner_product = 0
                    for k in range(self.columns):
                        inner_product += (self.data[j][k] * b.data[k][j])
                    output.data[i][j] = inner_product
            self.columns = output.columns
            self.rows = output.rows            
            self.data = output.data
            return
        
        elif self.rows == b.rows:

            output = Matrix(b.rows, b.columns, name = "Hadamard")    
            for i in range (b.rows):
                for j in range(b.columns):
                    self.data[i][j] *= b.data[i][j]           
            return
        
        else:
            raise Exception("FormatError")

    def add(self, n):

        if isinstance(n, int) or isinstance(n, float):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.data[i][j] = self.data[i][j] + n
            return
        
        elif self.rows == n.rows and self.columns == n.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.data[i][j] = self.data[i][j] + n.data[i][j]
            return
                
        else:
            raise Exception("FormatError")
    
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = random() * 2 - 1
        self.name = self.name + " randomized"
    
    def normalize(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = randint(0,5)
        self.name = self.name + "normalized"
        
    
    
    def transpose(self):
        output = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                output.data[j][i] = self.data[i][j]
        self.data = output.data
        self.rows = output.rows
        self.columns = output.columns
        self.shape = output.shape
