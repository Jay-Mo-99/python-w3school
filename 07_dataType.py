#text type: str
#numeric types: int, float, complex
#sequence Types: list, tuple, range
#Mapping type: dict
#Set types: set, frozenset
#Boolean Type: bool
#Binary Type: bytes, bytearray,memoryview
#None Type: NoneType 

a =["a",500,"White"]
b=("apple","banana")
c= range(0,10,5)
d = {"name" : "Jane","age":25}
e={100,200,500}
f=frozenset({10,20,50})
g=False
h=b"Hello"
i = bytearray(5)


x = memoryview(bytes(5))
print(x)
print(type(x))

y=bool(-1)
z=bytearray(5)
print(z)