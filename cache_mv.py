#TODO:
# 	1- Comparacao das tags com operadores logicos 
#	2- FIFO para escrever ou contador
#	3- a = c/l
#	4- n = c/l*a 

import sys


class Validation():
	def __init__(self):
		self.countL1 = 0
		self.countL2 = 0
		self.countL3 = 0
		self.countMiss = 0
		self.countHit = 0
		self.linhas = []
		nome_arquivo = sys.argv[1]
		arquivo = open(nome_arquivo, 'r')
		lista_linhas = arquivo.readlines()
		arquivo.close()
		self.linhas = lista_linhas

	def createOutput():
		# - Descrição de toda a hierarquia de memória, com dados de capacidade, associatividade e
		#tamanho de linhas de cada nível de cache, tamanho da memória RAM e da memória virtual,
		#além do tamanho das páginas.
		# - Número total de hits para cada nível (variando de 1 a 5 conforme retorno de getData).
		# - Número total de erros (dos tipos -1 ou -2 conforme retorno de getData).
		output = " "
		return output

	###  TACache  ###
	def createTACache(self, c, l):
		return TACache(c, l)

	def getTACacheCapacity(self, TACache):
		return TACache.capacity

	def getTACacheLineSize(self, TACache):
		return TACache.line_size

	def getTACacheData(self, TACache, adress, value):
		return False

	def setTACacheData(self, TACache, adress, value):
		return False

	###  SACache  ###
	def createSACache(self, c, a, l):
		return Cache(c, a, l)
	def getSACacheCapacity(self, SACache):
		pass
	def getSACacheLineSize(self, SACache):
		pass

	def getSACacheData(self, SACache, adress, value):
		pass

	def setSACacheData(self, SACache, adress, value):
		pass

	def duplicateSACache(self, SACache):
		pass

	###  Cache  ###
	def createCache(self, l1d,l1i,l2,l3):
		return Cache(l1d, l1i, l2, l3)
	def getCacheData(self, c, adress, value):
		pass
	def getCacheInstruction(self, c, adress, value):
		pass
	def setCacheData(self, c, adress, value):
		pass
	def setCacheInstruction(self, c, adress, value):
		pass
	def duplicateCache(self, c):
		pass

	### Main Memory ###
	def createMainMemory(self, ramsize, vmsize):
		return MainMemory(ramsize, vmsize)
	def allocSegment(self, mem, id, size):
		pass
	def freeSegment(self, mem, id):
		pass
	def getMainMemoryData(self, mem, address, value):
		pass
	def setMainMemoryData(self, mem, address, value):
		pass

	### Memory ###
	def createMemory(self, c, mem):
		return Memory(c, mem)
	def getData(self, mem, address, value):
		pass
	def getInstruction(self, mem, address, value):
		pass
	def getData(self, mem, address, value):
		pass
	def getInstruction(self, mem, address, value):
		pass
	def duplicateMemory(self, mem):
		pass

	### Processor ###
	def createProcessor(self, mem, ncores):
		return Processor(mem, ncores)

class TACache():
	def __init__(self, c, l):
		self.capacity = c
		self.line_size = l
		self.associacao = c/l
	
class SACache():
	def __init__(self, c, a, l):
		pass
		
class Cache():
	def __init__(self, l1d, l1i, l2, l3):
		pass

class MainMemory():
	def __init__(self, ramsize, vmsize):
		pass

class Memory():
	def __init__(self, c, mem):
		pass

class Processor():
	def __init__(self, mem, ncores):
		pass


if __name__ == "__main__":
	v = Validation()
	print v.linhas
	print v.linhas[0].split()
	ta = v.createTACache(10,2)
	print v.getTACacheCapacity(ta)
	print v.getTACacheLineSize(ta)