#TODO:
# 	tinyurl.com/ydhcvqy3
# 	1 - Comparacao das tags com operadores logicos 
#	2 - FIFO para escrever ou contador
#	3 - a = c/l
#	4 - n = c/l*a 
#	5 - Caches inclusivos
#	6 - Politica de escrita: Write-through

import sys
import copy
import Queue as q
import math as m

class Pow2Error(Exception):
	pass

def powCheck(n):
	return int(m.log(n,2)) == m.log(n,2)

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

	def counter(self, l1i, l1d, l2):
		self.countL1 = l1d.count
		self.countL1 += l1i.count
		self.countL2 = l2.count
		self.countHit = l1d.hit
		self.countHit += l1i.hit
		self.countHit += l2.hit
		self.countMiss = l1d.miss
		self.countMiss += l1i.miss
		self.countMiss += l2.miss
		pass

	def counterL3(self, l3):
		self.countL3 = l3.count
		self.countHit = l3.hit
		self.countMiss = l3.miss
		pass

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

	def getTACacheData(self, TACache, address):		# ELE PEDE PRA INCLUIR O VALUE, MAS NAO TA FAZENDO SENTIDO EM PYTHON
		_offset = self.getOffset(address, TACache.line_size)	
		_tag = address - _offset
		count = 0
		for addr in TACache.tag:
			if addr == _tag:
				value = TACache.lines[count][_offset]
				return True, value 
			count += 1
		return False, value
		'''
		l=getTACacheLineSize(TACache)
        x=l-1
        offset= address & x
        tag = address >> 6
        '''
	def getOffset(self, address, l):	#Por enquanto ta pegando na gambiarra, mas funciona
		offset = address & (l-49) 
		return offset
		'''
		if m.ceil(m.log(address,2)):
			o = address << int(l)
			print o
			o = bin(o)
			o = list(o)
			for i in range(0,int(l)):
				del(o[2])
			o = ''.join(o)
			o = int(o,2)
			return o >> int(l)
		else:
			return address
		'''
		
	def setTACacheData(self, TACache, address, value): 
		_offset = self.getOffset(address, TACache.line_size)
		_tag = address - _offset
		if TACache.count != TACache.assoc:	# Usando uma fila pra armazenar as tags, conforme solicitado no documento para usar uma estrutura FIFO
			TACache.tag[TACache.count] = _tag
			TACache.lines[TACache.count][_offset] = value
			TACache.count += 1
			#setValue(value)	-> Setar value na memoria (Nao sei como, da um help ai)
		else:
			TACache.count = 0
			TACache.tag[TACache.count] = _tag
			TACache.lines[TACache.count][_offset] = value
			TACache.count += 1
		print TACache.tag		

	###  SACache  ###
	def createSACache(self, c, a, l):
		return SACache(c, a, l)
	def getSACacheCapacity(self, SACache):
		return SACache.capacity
	def getSACacheLineSize(self, SACache):
		return SACache.line_size

	def getSACacheData(self, SACache, address, value):
		return  True, value

	def setSACacheData(self, SACache, address, value):
		pass

	def duplicateSACache(self, SACache):
		pass

	###  Cache  ###
	def createCache(self, l1d,l1i,l2,l3):
		return Cache(l1d, l1i, l2, l3)
	def getCacheData(self, c, adress, value):
		pass
	def getCacheInstruction(self, c, address, value):
		pass
	def setCacheData(self, c, address, value):
		pass
	def setCacheInstruction(self, c, address, value):
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
		if not powCheck(c):
			raise Pow2Error("Capacity isn't a power of two")
		if not powCheck(l):
			raise Pow2Error("Line size isn't a power of two")
		self.offset_size = int(m.log(l,2))
		print "OFFSET ###########"
		print self.offset_size
		self.capacity = c
		self.line_size = l
		self.assoc = c/l
		#self.tag = q.Queue()	# Fila - FIFO
		self.tag = [None]*int(c/l)
		self.lines = []
		aux = [None]*16
		for i in range(0,int(c/l)):
			self.lines.append((copy.deepcopy(aux)))
		self.count = 0
	
class SACache():
	def __init__(self, c, a, l):
		if not powCheck(c):
			raise Pow2Error("Capacity isn't a power of two")
		if not powCheck(l):
			raise Pow2Error("Line size isn't a power of two")
		if not powCheck(a):
			raise Pow2Error("Associativity isn't a power of two")
#		if c%(a*l)!=0
		self.miss = 0
		self.hit = 0
		self.count = 0
		self.capacity = c
		self.line_size = l
		self.block_size = c / l * a
		self.blocks = []
		self.offset_size = m.log(l,2)
		self.lookup_size = m.log(self.block_size,2)
		for i in range (0, self.block_size):
			self.blocks.append(TACache(c/self.block_size,l))

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
	
	ta = v.createTACache(512,64)
	print v.getTACacheCapacity(ta)
	print v.getTACacheLineSize(ta)
	v.setTACacheData(ta, 3, 4)
	v.setTACacheData(ta, 30, 2)
	v.setTACacheData(ta, 13, 1)
	v.setTACacheData(ta, 22, 3)
	v.setTACacheData(ta, 44, 5)
	v.setTACacheData(ta, 32, 7)
	v.setTACacheData(ta, 64, 9)
	v.setTACacheData(ta, 16, 11)
	v.setTACacheData(ta, 200, 13)
	v.setTACacheData(ta, 84, 15)
	print ta.lines

	print "\n\n#########\n\n"

	_, value = v.getTACacheData(ta,84)
	print value
	#print ta.tag
	#sa = v.createSACache(16,2,2)
	#print sa.blocks[1].offset_size
	#print v.getTACacheCapacity(sa.blocks[1])
	#print v.getTACacheCapacity(sa.blocks[2])
