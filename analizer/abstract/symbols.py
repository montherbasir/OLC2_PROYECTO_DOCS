class Symbol:
	def __init__(self, name) -> None:
		self.name = name


class SymbolTable:
	def __init__(self) -> None:
		self.table = {}

	def addSymbol(self, Symbol, alias):
		self.table[alias] = Symbol
	
	def getSymbol(self, alias):
		try:
			return self.table[alias].name
		except KeyError:
			print("No existe el alias")

# SELECT nombre as name FROM cliente
t = SymbolTable()

x = Symbol("cliente.nombre")

t.addSymbol(x,"nombre")
t.addSymbol(x,"name")
print(t.table)

# cliente.nombre
print(t.getSymbol("name"))

y = Symbol("cliente.puta")

t.addSymbol(y,"name")

# cliente.puta
print(t.getSymbol("name"))
print(t.table)