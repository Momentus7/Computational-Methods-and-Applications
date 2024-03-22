
class RowVectorFloat():
  def __init__(self,num):
    self.num=num
  def __str__(self):
    return(" ".join(str(i) for i in self.num))
  def __len__(self):
    return len(self.num)
  def __getitem__(self,items):
    return ( self.num[items])
  def __setitem__(self,key, value):
    self.num[key]=value
  def __add__(self, other):
    if (len(self.num)==len(other.num)):
      s=[]
      for i,j in zip(self.num, other.num):
        s.append(i+j);
      return RowVectorFloat(s)
    else:
      raise Exception("length of vectors not same")
  
  def __mul__(self,scalar):
    s=[]
    for i in self.num:
      s.append(scalar*i);
    return RowVectorFloat(s)
  
  def __rmul__(self,n):
    s=[]
    for i in self.num:
      s.append(n*i);
    return RowVectorFloat(s)

  



'''r=RowVectorFLoat([1,9,3])
print(r)
print(len(r))
print(r[1])

r[2]=8
print(r)'''

r1 = RowVectorFloat([1, 2, 4])
r2 = RowVectorFloat([1, 1, 1])
r3 = 2 * r1 + (-3) * r2
print(r3)