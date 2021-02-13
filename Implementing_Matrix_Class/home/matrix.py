import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            det = self.g[0][0]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = a*d - b*c
            
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        tr = 0
        for r in range(self.h):
            for c in range(self.w):
                if r == c:
                    tr += self[r][c]                
            
        return tr

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
       
        if self.h == 1:
            inverse_matrix = [[1 / self.g[0][0]]]
            inv = Matrix(inverse_matrix)
            
        elif self.h == 2:
            denominator = self.determinant()
            trace_matrix = self.trace()
            I_matrix = identity(self.h)
             
            
            inv = (1/denominator) * (trace_matrix * I_matrix - self)
            
        return inv
    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        trans = []
        for c in range(self.w):
            temp = []
            for r in range(self.h):
                temp.append(self.g[r][c])
            trans.append(temp)
            
        return Matrix(trans)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
            
        matrix = [[0 for cell in range(self.w)]for row in range(self.h)]
        
        addition = Matrix(matrix)        
        
        for r in range(self.h):
            for c in range(self.w):
                addition.g[r][c] = self.g[r][c] + other.g[r][c]
            
        return addition

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        matrix = [[0 for cell in range(self.w)] for row in range(self.h)]
        neg = Matrix(matrix)        
        for r in range(self.h):
            for c in range(self.w):
                neg.g[r][c] = -self.g[r][c] 
            
        return neg 


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """  
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        result = []
        matrix = [[0 for cell in range(self.w)]for row in range(self.h)]
        sub = Matrix(matrix)        
        for r in range(self.h):
            for c in range(self.w):
                sub.g[r][c] = self.g[r][c] - other.g[r][c]
            
        return sub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied if the column of 1st matrix is equale to row of 2nd matrix") 
        #   
        # TODO - your code here
            
        matrix = [[0 for cell in range(other.w)] for row in range(self.h)]
        
        for i in range(self.h):
            for j in range(other.w):
                total = 0
                for k in range(self.w):
                    total += (self.g[i][k] *  other.g[k][j])
                matrix[i][j] = total
                
        mult_matrix = Matrix(matrix)       
        return mult_matrix

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        
            matrix = [[0 for cell in range(self.w)]for row in range(self.h)]
            
            for r in range(self.h):
                for c in range(self.w):
                    matrix[r][c] = self.g[r][c] * other
        
            rmul = Matrix(matrix) 
        
        return rmul
                    
            