from math import sqrt 
class Vector: 
	def __init__(self, x, y, z): 
		self.x = x 
		self.y = y 
		self.z = z 
	def __add__(self, V): 

		return Vector(self.x + V.x, self.y + V.y, self.z + V.z) 

	def __sub__(self, V): 

		return Vector(self.x - V.x, self.y - V.y, self.z - V.z) 

	def __abs__(self):

		return sqrt(self.x**2 + self.y**2 + self.z**2)

	def __xor__(self, V): 

		return self.x * V.x + self.y * V.y + self.z * V.z 



	def __repr__(self): 

		out = str(self.x) 

		if self.y >= 0: 
			out +=" "
		out += str(self.y) 
		if self.z >= 0: 
			out += " "
		out += str(self.z) 

		return out 


if __name__ == "__main__": 

	V0 = Vector(1, 2, 3) 
	V1 = Vector(5, 6, 7) 
	print("Addition of V0 and V1: " , str(V0 + V1)) 

	print("Subtraction of V1 and V0: " , str(V1 - V0))

	print("abs of V0: " , V0.__abs__()) 

	print("Dot Product of V0 and V1: " , str(V0 ^ V1)) 