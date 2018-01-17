#TODO:
# 	1 - Comparacao das tags com operadores logicos 
#	2 - FIFO para escrever ou contador
#	3 - a = c/l
#	4 - n = c/l*a 
#	5 - Caches inclusivos
#	6 - Politica de escrita: Write-through

import sys
import copy

class Validation():
	def __init__(self):
		self.countL1 = 0
		self.countL2 = 0
		self.countL3 = 0
		self.countMiss = 0
		self.countHit = 0
		self.linhas = []
		fileName = sys.argv[1]
		file = open(fileName, 'r')
		lines_list = file.readlines()
		file.close()
		self.lines = lines_list

	def doInstruction(self, ins, par1, par2):
		pass

	def createOutput(self):
		# - Descricao de toda a hierarquia de memoria, com dados de capacidade, associatividade e
		#	tamanho de linhas de cada nivel de cache, tamanho da memoria RAM e da memoria virtual,
		#	alem do tamanho das paginas.
		# - Numero total de hits para cada nivel (variando de 1 a 5 conforme retorno de getData).
		# - Numero total de erros (dos tipos -1 ou -2 conforme retorno de getData).
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
		pass

	def setTACacheData(self, TACache, adress, value):
		pass

	###  SACache  ###
	def createSACache(self, c, a, l):
		return SACache(c, a, l)
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
		self.assoc = c/l
	
class SACache():
	def __init__(self, c, a, l):
		self.blocks = []
		for i in range (0, c/l*a):
			self.blocks.append(TACache(c,l))
		self.tag = 0
		self.offset = 0
		
class Cache():
	def __init__(self, l1d, l1i, l2, l3):
		self.l1d = copy.deepcopy(l1d)
		self.l1i = copy.deepcopy(l1i)
		self.l2 = copy.deepcopy(l2)
		self.l3 = l3

class MainMemory():
	def __init__(self, ramsize, vmsize):
		pass

class Memory():
	def __init__(self, c, mem):
		self.cache = c
		self.memory = mem

class Processor():
	def __init__(self, mem, ncores):
		self.memory = []
		self.ncores = ncores
		for i in range(0,ncores):
			self.memory.append(mem)

if __name__ == "__main__":
	v = Validation()
	ins = []

	while len(v.lines) > 0:
		ins = v.lines[0].split()
		v.doInstruction(ins[0],ins[1],ins[2])
		v.lines.remove(v.lines[0])
	
	ta = v.createTACache(10,2)
	print v.getTACacheCapacity(ta)
	print v.getTACacheLineSize(ta)
	sa = v.createSACache(10,2,2)
	print v.getTACacheCapacity(sa.blocks[1])
	print v.getTACacheCapacity(sa.blocks[2])

