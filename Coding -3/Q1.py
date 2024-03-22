class RowVectorFloat:
    # The __init__ method initializes the RowVectorFloat object with a vector
    def __init__(self,vector):
        self.vector=vector;

    # The __str__ method returns the string representation of the RowVectorFloat object
    def __str__(self):
        s=""
        for i in self.vector:
            s+=f"{i} ";
        return s;

    # The __len__ method returns the length of the vector in the RowVectorFloat object
    def __len__(self):
        l=len(self.vector);
        return l;

    # The __getitem__ method returns the element at the given index of the vector in the RowVectorFloat object
    def __getitem__(self, n): 
        return self.vector[n];

    # The __setitem__ method sets the element at the given index of the vector in the RowVectorFloat object to the given value
    def __setitem__(self, n,value):
        self.vector[n]=value;

    # The __add__ method overloads the '+' operator to allow vector addition of two RowVectorFloat objects
    def __add__(self, other):
        if len(self.vector)==len(other.vector):
            sol=[]
            for i,j in zip(self.vector,other.vector):
                sol.append(i+j);
            return RowVectorFloat(sol);
        else:
            raise Exception("Vector addition is not possible")

    # The __mul__ method overloads the '*' operator to allow scalar multiplication of a RowVectorFloat object
    def __mul__(self,scalar):
        sol=[]
        for i in self.vector:
            sol.append(scalar*i);
        return RowVectorFloat(sol)

    # The __rmul__ method overloads the '*' operator to allow scalar multiplication of a RowVectorFloat object in the reverse order
    def __rmul__(self,n):
        sol=[]
        for i in self.vector:
            sol.append(n*i);
        return RowVectorFloat(sol)
        
    
r=RowVectorFloat([1,2,3])
print(r)

r = RowVectorFloat([1, 2 , 4])
print(r[1])
print(len(r))
r = RowVectorFloat([])
print(len(r))
r = RowVectorFloat([1, 2 , 4])
r[2] = 5
print(r)
r1=RowVectorFloat([1,2,4])
r2=RowVectorFloat([1,2,3])
print(r1+r2)
r1 = RowVectorFloat([1, 2 , 4])
r2 = RowVectorFloat([1, 1 , 1])
r3 = r1*2+r2*(-3)
r4 = 2*r1+(-3)*r2
print(r3)
print(r4)

