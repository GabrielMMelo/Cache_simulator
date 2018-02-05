#TODO:
# 	tinyurl.com/ydhcvqy3
# 	1 - Comparacao das tags com operadores logicos 
#	2 - FIFO para escrever ou contador
#	3 - a = c/l
#	4 - n = c/l*a 
#	5 - Caches inclusivos
#	6 - Politica de escrita: Write-through
#	TODO2:
#	*** Rodar para um processador apenas:
#	1 - Linha '129' list out of range
#	2 - DEMAIS ERROS QUE APARECEREM	
#
#	*** Rodar para demais processadores:
#	1 - Reconstruir as demais memorias como a primeira memoria
#
#
#	SAUDE: 
#	1 - Na entrada "asserti" nao eh explicitado o retorno 	TRUE
#	2 - O que usar no lugar do "log()"					LOG MESMO	
#	3 - deepcopy() ou reconstruir as proximas memorias 		RECONSTRUIR

import sys
import copy
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

	def doInstruction(self, ins):
		for i in range(1,len(ins)):
			ins[i] = float(ins[i])
		print ins
		if ins[0] == "cl1d":
			return self.createSACache(ins[1], ins[2], ins[3])
		elif ins[0] == "cl1i":
			return self.createSACache(ins[1], ins[2], ins[3])
		elif ins[0] == "cl2":
			return self.createSACache(ins[1], ins[2], ins[3])
		elif ins[0] == "cl3":
			l3 = self.createSACache(ins[1], ins[2], ins[3])
			return l3
		elif ins[0] == "cmp":
			return self.createMainMemory(ins[1], ins[2])
		elif ins[0] == "cmem":
			return self.createMemory(hier_cache, main)
		elif ins[0] == "cp":
			return self.createProcessor(hier_mem, ins[1])
		elif ins[0] == "ri":
			# ncore & address
			return self.getInstruction(processador.memory[int(ins[1])],ins[2])
		elif ins[0] == "wi":
			print "Chamou setInstruction()"
			return self.setInstruction(processador.memory[int(ins[1])],ins[2], ins[3])
		elif ins[0] == "rd":
			return self.getData(processador.memory[int(ins[1])],ins[2])
		elif ins[0] == "wd":
			print "Chamou setInstruction()"
			return self.setData(processador.memory[int(ins[1])],ins[2], ins[3])
		# n addr level value
		elif ins[0] == "asserti":
			pass
		# Nao explicita como deve ser o retorno
		elif ins[0] == "assertd":
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

	def getTACacheData(self, TACache, address, value):		# ELE PEDE PRA INCLUIR O VALUE, MAS NAO TA FAZENDO SENTIDO EM PYTHON
		_offset = self.getOffset(address, TACache.line_size)	
		_tag = address - _offset
		count = 0
		for addr in TACache.tag:
			if addr == _tag:
				value = TACache.lines[count][_offset]
				return True, value 
			count += 1
		return False, value

		
	def setTACacheLine(self, TACache, address, line):		
		_offset = self.getOffset(address, TACache.line_size)
		_tag = address - _offset
		if TACache.count != TACache.assoc:	# Usando uma fila pra armazenar as tags, conforme solicitado no documento para usar uma estrutura FIFO
			TACache.tag[TACache.count] = _tag
			count = 0
			
			for l in line:
				#print TACache.lines
				#print line
				#print count
				#print TACache.count

				TACache.lines[TACache.count][count] = l
				count += 1
			#print TACache.lines[0]
			TACache.count += 1
		else:
			TACache.count = 0
			TACache.tag[TACache.count] = _tag
			count = 0
			for l in line:
				TACache.lines[TACache.count][count] = l
				count += 1
			TACache.count += 1

	def setTACacheData(self, TACache, address, value): # Se retornar FALSE, devemos chamar setTACacheLine e dps chamar this denovo
		_offset = self.getOffset(address, TACache.line_size)
		_tag = address - _offset
		count = 0
		for addr in TACache.tag:
			if addr == _tag:
				TACache.lines[count][_offset] = value
				return True
			count += 1
		return False

	def getOffset(self, address, l):	
		#address = address>>2
		offset = address & int(l-49)
		return offset

	def getLookup(self, address, l_size, o_size):
		#address = address>>2
		lookup = address >> o_size
		lookup = lookup & int(l_size-1)
		return lookup

	###  SACache  ###
	def createSACache(self, c, a, l):
		return SACache(c, a, l)
	def getSACacheCapacity(self, SACache):
		return SACache.capacity
	def getSACacheLineSize(self, SACache):
		return SACache.line_size

	def getSACacheData(self, SACache, address):
		_offset = self.getOffset(address, SACache.blocks[0].line_size)
		_lookup = self.getLookup(address, SACache.lookup_size, SACache.offset_size)
		_lookup2 = _lookup << int(m.ceil(m.log(SACache.offset_size,2)))
		_lookup2 += _offset
		_tag = address - _lookup2
		#_tag = address << int((m.ceil(m.log(SACache.lookup_size,2) + m.log(SACache.offset_size,2))))
		value = 0
		SACache.count = 0
		for addr in SACache.blocks[_lookup].tag:
			if addr == _tag:
				value = SACache.blocks[_lookup].lines[SACache.count][_offset]
				return True, value
			SACache.count += 1
		return False, value


	def setSACacheLine(self, SACache, address, line):
		_offset = self.getOffset(address, SACache.blocks[0].line_size)
		_lookup = self.getLookup(address, SACache.lookup_size, SACache.offset_size)
		self.setTACacheLine(SACache.blocks[_lookup], address, line)

	def setSACacheData(self, SACache, address, value):	
		_offset = self.getOffset(address, SACache.line_size)
		_lookup = self.getLookup(address, SACache.lookup_size, SACache.offset_size)
		_tag = address - _offset
		
		count = 0

		for addr in SACache.blocks[_lookup].tag:
			if addr == _tag:
				SACache.blocks[_lookup].lines[count][_offset] = value
				return True
			count += 1
		return False

	def duplicateSACache(self, SACache):
		return copy.deepcopy(SACache)

	###  Cache  ###
	def createCache(self):
		return Cache()

	# TODO
	# Retirar os values do cache 
	# Usar o retorno dos Get para o value do Set
	def getCacheData(self, c, mmem, address):
		ret1, value = self.getSACacheData(c.l1d,address)
		print value
		if ret1:
			return 1
		ret2, value = self.getSACacheData(c.l2,address)
		if ret2:
			setSACacheData(c.l1d, address, value)
			return 2
		ret3, value = self.getSACacheData(c.l3,address)
		if ret3:
			setSACacheData(c.l1d, address, value)
			setSACacheData(c.l2, address, value)
			return 3

		if address >= mmem.mainsize:
			return -1

		self.fetchCacheData(c, mmem, address)
		return 4

	def getCacheInstruction(self, c, mmem, address):
		ret1, value = self.getSACacheData(c.l1d,address)
		if ret1:
			return 1
		ret2, value = self.getSACacheData(c.l2,address)
		if ret2:
			setSACacheData(c.l1d, address, value)
			return 2
		ret3, value = self.getSACacheData(c.l3,address)
		if ret3:
			setSACacheData(c.l1d, address, value)
			setSACacheData(c.l2, address, value)
			return 3
		
		if address >= mmem.mainsize:
			return -1

		self.fetchCacheInstruction(c, mmem, address)
		return 4

	def setCacheData(self, c, address, value):
		self.setSACacheData(c.l1d, address, value)
		#	self.setSACacheLine(c.l1d, address, value)
		self.setSACacheData(c.l2, address, value)
		#	self.setSACacheLine(c.l2, address, value)
		self.setSACacheData(c.l3, address, value)
		#	self.setSACacheLine(c.l3, address, value)

	def setCacheInstruction(self, c, address, value):
		self.setSACacheData(c.l1i, address, value)
		#	self.setSACacheLine(c.l1i, address, value)
		self.setSACacheData(c.l2, address, value)
		#	self.setSACacheLine(c.l2, address, value)
		self.setSACacheData(c.l3, address, value)
		#	self.setSACacheLine(c.l3, address, value)

	def duplicateCache(self, c):
		return copy.deepcopy(SACache)

	def fetchCacheData(self, c, mmem, address):
		line = []
		_offset = self.getOffset(address, c.l1d.line_size)
		_tag = address - _offset
		ia = _tag 
		fa = ia + (int(c.l1d.line_size)>>2) - 1
		for i in range(ia,fa+1):
			line.append(copy.deepcopy(mmem.main[i]))
		self.setSACacheLine(c.l1d, address, line)

		line = []
		_offset = self.getOffset(address, c.l2.line_size)
		_tag = address - _offset
		ia = _tag 
		fa = ia + (int(c.l2.line_size)>>2) - 1
		for i in range(ia,fa+1):
			line.append(copy.deepcopy(mmem.main[i]))
		self.setSACacheLine(c.l2, address, line)

		line = []
		_offset = self.getOffset(address, c.l3.line_size)
		_tag = address - _offset
		ia = _tag 
		fa = ia + (int(c.l3.line_size)>>2) - 1
		for i in range(ia,fa+1):
			line.append(copy.deepcopy(mmem.main[i]))
		self.setSACacheLine(c.l3, address, line)


	def fetchCacheInstruction(self, c, mmem, address):
		line = []
		_offset = self.getOffset(address, c.l1i.line_size)
		_tag = address - _offset
		ia = _tag 
		fa = ia + (int(c.l1i.line_size)>>2) - 1
		for i in range(ia,fa+1):
			line.append(copy.deepcopy(mmem.main[i]))
		self.setSACacheLine(c.l1d, address, line)

		line = []
		_offset = self.getOffset(address, c.l2.line_size)
		_tag = address - _offset
		ia = _tag 
		fa = ia + (int(c.l2.line_size)>>2) - 1
		for i in range(ia,fa+1):
			line.append(copy.deepcopy(mmem.main[i]))
		self.setSACacheLine(c.l2, address, line)

		line = []
		_offset = self.getOffset(address, c.l3.line_size)
		_tag = address - _offset
		ia = _tag 
		fa = ia + (int(c.l3.line_size)>>2) - 1
		for i in range(ia,fa+1):
			line.append(copy.deepcopy(mmem.main[i]))
		self.setSACacheLine(c.l3, address, line)

	### Main Memory ###
	def createMainMemory(self, ramsize, vmsize):
		return MainMemory(ramsize, vmsize)

	def getMainMemoryData(self, mem, address,value): # ELE PEDE PRA INCLUIR O VALUE, MAS NAO TA FAZENDO SENTIDO EM PYTHON
		if address < 0 or address > (mem.mainsize -1):
			return -1

		if mem.main[address] != None:
			return 4, mem.main[address]

		return -1, mem.main[address]

	def setMainMemoryData(self, mem, address, value):
		if address < 0 or address > (mem.mainsize -1):
			return -1

		mem.main[address] = value
	#	print mem.main[address]
		return 4
		
	### Memory ###
	def createMemory(self, c, mem):
		return Memory(c, mem)
	def getData(self, mem, address):
		address = int(address)>>2
		return self.getCacheData(mem.cache, mem.memory, address)

	def getInstruction(self, mem, address):
		address = int(address)>>2
		return self.getCacheInstruction(mem.cache, mem.memory, address)


	def setData(self, mem, address, value):
		address = int(address)>>2
		print "Chamou setCacheInstruction() e setMainMemoryData()"
		self.setCacheData(mem.cache, address, value)
		self.setMainMemoryData(mem.memory, address, value)

	def setInstruction(self, mem, address, value):
		address = int(address)>>2
		print "Chamou setCacheInstruction() e setMainMemoryData()"
		self.setCacheInstruction(mem.cache, address, value)
		self.setMainMemoryData(mem.memory, address, value)

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
		#print "OFFSET ###########"
		#print self.offset_size
		self.capacity = c
		self.line_size = l
		self.assoc = c/l
		#self.tag = q.Queue()	# Fila - FIFO
		self.tag = [None]*int(c/l)
		self.lines = []
		aux = [None]* (int(l)>>2)
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
		self.miss = 0
		self.hit = 0
		self.count = 0
		self.capacity = c
		self.line_size = l
		self.lookup_size = c / (l * a)
		self.blocks = []
		self.offset_size = int(m.log(l,2))
		for i in range (0, int(self.lookup_size)):
			self.blocks.append(TACache(c/self.lookup_size,l))

class Cache():
	def __init__(self):
		self.l1d = copy.deepcopy(L1d)
		self.l1i = copy.deepcopy(L1i)
		self.l2 = copy.deepcopy(L2)
		self.l3 = L3

class MainMemory():
	def __init__(self, ramsize, vmsize):
		self.mainsize = int(ramsize + vmsize) >> 2
		self.main = []
		self.value = None
		for i in range(0,self.mainsize):
			self.main.append(self.value)

class Memory():
	def __init__(self, c, mem):
		self.cache = c
		self.memory = mem

class Processor():
	def __init__(self, mem, ncores):
		self.memory = []
		self.ncores = ncores
		for i in range(0,int(ncores)):
			self.memory.append(mem)

if __name__ == "__main__":
	v = Validation()
	ins = ''
	for i in range(0,7):
		print i
		ins = v.lines[0].split()
		v.lines.remove(v.lines[0])
		if i == 0:
			global L1d 
			L1d = v.doInstruction(ins)
		elif i == 1:
			global L1i 
			L1i = v.doInstruction(ins)
		elif i == 2:
			global l2
			L2 = v.doInstruction(ins)
		elif i == 3:
			global L3 
			global hier_cache
			L3 = v.doInstruction(ins)
			hier_cache = Cache()
		elif i == 4:
			global main
			main = v.doInstruction(ins)
		elif i==5:
			global hier_mem
			hier_mem = v.doInstruction(ins)
		elif i==6:
			global processador
			processador = v.doInstruction(ins)


	#v.setInstruction(processador.memory[0], 1, 4)
	#print processador.memory[0].memory.main
	while len(v.lines) > 0:
		ins = v.lines[0].split()

		resposta = v.doInstruction(ins)
		print "ler"
		#print processador.memory[0].memory.main[int(ins[2]/4)]
		print "resposta"
		print resposta
		v.lines.remove(v.lines[0])


	#print processador.memory[0].cache.l1i.blocks[0].lines
	
'''
	#processador.memory[0].cache.l3.blocks[0].lines[1][1] = 1
	#print processador.memory[0].cache.l3.blocks[0].lines
	#processador.memory[0].cache.l1d.blocks[0].lines[1][1] = 1
	#print processador.memory[0].cache.l1d.blocks[0].lines
	#processador.memory[0].cache.cu = "bosta"
	#print processador.memory[0].cache.cu
	#print "######################"
	#processador.memory[0].cache.cu = "bosta"
	#print processador.memory[1].cache.cu
	#processador.memory[1].cache.l3.blocks[0].lines[1][0] = 2
	#print processador.memory[1].cache.l3.blocks[0].lines	
	#processador.memory[1].cache.l1d.blocks[0].lines[0][1] = 1
	#print processador.memory[1].cache.l1d.blocks[0].lines
	

# TA tests

	ta = v.createTACache(128,32)
	print v.getTACacheCapacity(ta)
	print v.getTACacheLineSize(ta)
	a,_ = v.getTACacheData(ta,12,8)
	print a

	print "####################"

# SA tests

	sa = v.createSACache(128,2,16)
	print v.getSACacheCapacity(sa)
	print v.getSACacheLineSize(sa)

	a,_ = v.getSACacheData(sa,20,8)
	print a

	print sa.blocks

	print sa.offset_size

	print sa.lookup_size

	sa2 = v.duplicateSACache(sa)
	
	print sa2.blocks

	print sa2.offset_size

	print sa2.lookup_size

	print "####################"

# Cache tests

	cache = v.createCache(sa,sa2, v.createSACache(256, 2, 16), v.createSACache(512,4,32))

# Main Memory

	mem = v.createMainMemory(2048,2048)
	print v.getMainMemoryData(mem, 533, 0)
	print v.setMainMemoryData(mem, 53, 1)
	a,value = v.getMainMemoryData(mem, 53, 0)


	mmem = v.createMainMemory(128,128)
	v.setMainMemoryData(mmem, 12, 20)
	_,data = v.getMainMemoryData(mmem,12)
	print data

	oi = v.getLookup(50,7,2)
	print oi
	
	ta = v.createTACache(512,64)
	print ta.lines

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
	
	print ta.tag
	sa = v.createSACache(16,2,2)
	print sa.blocks[1].offset_size
	print v.getTACacheCapacity(sa.blocks[1])
	print v.getTACacheCapacity(sa.blocks[2])
	'''