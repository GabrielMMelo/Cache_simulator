#	
#	Cabecalho: (tinyurl.com/ydhcvqy3)
# 	
# 	1 - Comparacao das tags com operadores logicos 
#	2 - FIFO para escrever ou contador
#	3 - a = c/l
#	4 - n = c/l*a 
#	5 - Caches inclusivos
#	6 - Politica de escrita: Write-through

import sys
import copy
import math as m

# Classe que dispara excecao para numeros nao multiplos
class MultipleError(Exception):
	pass
# Classe que dispara excecao para numeros que nao sejam potencia de 2
class Pow2Error(Exception):
	pass
# Classe que dispara excecao para entradas de funcoes invalidas
class sintaxError(Exception):
	pass

# Checa se um numero eh potencia de 2
def powCheck(n):
	return int(m.log(n,2)) == m.log(n,2)

# Classe de validacao do programa
class Validation():
	def __init__(self):
		self.countL1d = 0
		self.countL1i = 0
		self.countL2 = 0
		self.countL3 = 0
		self.countMem = 0
		self.countError = 0
		self.linhas = []
		fileName = sys.argv[1]
		file = open(fileName, 'r')
		lines_list = file.readlines()
		file.close()
		self.lines = lines_list

	# Metodo que executa as funcoes do arquivo de entrada
	def doInstruction(self, ins):
		for i in range(1,len(ins)):
			ins[i] = float(ins[i])
		#print ins
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
			return self.setInstruction(processador.memory[int(ins[1])],ins[2], ins[3])
		elif ins[0] == "rd":
			return self.getData(processador.memory[int(ins[1])],ins[2])
		elif ins[0] == "wd":
			return self.setData(processador.memory[int(ins[1])],ins[2], ins[3])

		elif ins[0] == "asserti": # O indice comeca no 1?
			if int(ins[3]) == 1:
				resp, value = self.getSACacheData(processador.memory[n].cache.l1i, int(ins[2]))
				if resp and (value == float(ins[4])):
					return True

			elif int(ins[3]) == 2:
				resp, value = self.getSACacheData(processador.memory[n].cache.l2, int(ins[2]))
				if resp and (value == float(ins[4])):
					return True
			elif int(ins[3]) == 3:
				resp, value = self.getSACacheData(processador.memory[n].cache.l3, int(ins[2]))
				if resp and (value == float(ins[4])):
					return True	
			return 0

		elif ins[0] == "assertd":
			if int(ins[3]) == 1:
				resp, value = self.getSACacheData(processador.memory[n].cache.l1d, int(ins[2]))
				if resp and (value == float(ins[4])):
					return True

			elif int(ins[3]) == 2:
				resp, value = self.getSACacheData(processador.memory[n].cache.l2, int(ins[2]))
				if resp and (value == float(ins[4])):
					return True
			elif int(ins[3]) == 3:
				resp, value = self.getSACacheData(processador.memory[n].cache.l3, int(ins[2]))
				if resp and (value == float(ins[4])):
					return True	
			return 0

		else:
			raise sintaxError("Invalid command: " + str(ins[0]))
			
	# Cria o relatorio final
	def createOutput(self):
		# - Descricao de toda a hierarquia de memoria, com dados de capacidade, associatividade e
		#	tamanho de linhas de cada nivel de cache, tamanho da memoria RAM e da memoria virtual,
		#	alem do tamanho das paginas.
		# - Numero total de hits para cada nivel (variando de 1 a 5 conforme retorno de getData).
		# - Numero total de erros (dos tipos -1 ou -2 conforme retorno de getData).
		print " _________________________________________________"
		print "|			L1d			  |" 
		print "|_________________________________________________|"
		print "|Capacity		|		  " + str(processador.memory[0].cache.l1d.capacity) + " |"
		print "|Associativity		|	  	      " + str(processador.memory[0].cache.l1d.associativity) + " |"
		print "|Line size 		|	  	     " + str(processador.memory[0].cache.l1d.line_size) + " |"
		print "|_______________________|_________________________| \n"

		print " _________________________________________________"
		print "|			L1i			  |" 
		print "|_________________________________________________|"
		print "|Capacity		|		  " + str(processador.memory[0].cache.l1i.capacity) + " |"
		print "|Associativity		|	  	      " + str(processador.memory[0].cache.l1i.associativity) + " |"
		print "|Line size 		|	  	     " + str(processador.memory[0].cache.l1i.line_size) + " |"
		print "|_______________________|_________________________| \n"

		print " _________________________________________________"
		print "|			L2			  |" 
		print "|_________________________________________________|"
		print "|Capacity		|		 " + str(processador.memory[0].cache.l2.capacity) + " |"
		print "|Associativity		|	  	      " + str(processador.memory[0].cache.l2.associativity) + " |"
		print "|Line size 		|	  	     " + str(processador.memory[0].cache.l2.line_size) + " |"
		print "|_______________________|_________________________| \n"

		print " _________________________________________________"
		print "|			L3			  |" 
		print "|_________________________________________________|"
		print "|Capacity		|		" + str(processador.memory[0].cache.l3.capacity) + " |"
		print "|Associativity		|	  	     " + str(processador.memory[0].cache.l3.associativity) + " |"
		print "|Line size 		|	  	    " + str(processador.memory[0].cache.l3.line_size) + " |"
		print "|_______________________|_________________________| \n"


		print "#########################################################\n"

		print "RAM size: " + str(processador.memory[0].memory.ramsize) + "\n"

		print "Virtual memory size: " + str(processador.memory[0].memory.vmsize) + "\n"

		print "#########################################################\n"

		print "HIT:\n"

		print "L1d: " + str(self.countL1d)
		print "L1i: " + str(self.countL1i)
		print "L2: " + str(self.countL2)
		print "L3: " + str(self.countL3) 
		print "Memory: " + str(self.countMem) + "\n"
		
		print "Errors: "  + str(self.countError)

	###  TACache  ###
	def createTACache(self, c, l):
		return TACache(c, l)

	def getTACacheCapacity(self, TACache):
		return TACache.capacity

	def getTACacheLineSize(self, TACache):
		return TACache.line_size

	def getTACacheData(self, TACache, address, value):
		_offset = self.getOffset(address, TACache.line_size)	
		_tag = address - _offset
		count = 0
		for addr in TACache.tag:
			if addr == _tag:
				value = TACache.lines[count][_offset]
				return True, value 
			count += 1
		return False, value
		
	def setTACacheLine(self, TACache, address, line):		#ERRO: Devia conferir se ja existe o valor na tag, porem "setTACacheLine" nao e acessivel fora da classe
		_offset = self.getOffset(address, TACache.line_size)
		_tag = address - _offset
		if TACache.count != TACache.assoc:	# Usando uma lista em formato FIFO usando um contador TACache.count
			TACache.tag[TACache.count] = _tag
			count = 0
			
			for l in line:
				TACache.lines[TACache.count][count] = l
				count += 1

			TACache.count += 1
		else:
			TACache.count = 0
			TACache.tag[TACache.count] = _tag
			count = 0
			for l in line:
				TACache.lines[TACache.count][count] = l
				count += 1
			TACache.count += 1

	def setTACacheData(self, TACache, address, value):
		_offset = self.getOffset(address, TACache.line_size)
		_tag = address - _offset
		count = 0
		for addr in TACache.tag:
			if addr == _tag:
				TACache.lines[count][_offset] = value
				return True
			count += 1
		return False

	# Retorna o offset
	def getOffset(self, address, l):	
		offset = address & int(((int(l) >> 2) - 1))
		return offset

	# Retorna o Lookup
	def getLookup(self, address, l_size, o_size):
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
		
		if not self.setTACacheData(SACache.blocks[_lookup], address, value):
			return False
		
		return True

	def duplicateSACache(self, SACache):
		pass

	###  Cache  ###
	def createCache(self, L1d, L1i, L2, L3):
		return Cache()

	def getCacheData(self, c, mmem, address):
		ret1, value = self.getSACacheData(c.l1d,address)
		if ret1:
			self.countL1d += 1
			return 1
		ret2, value = self.getSACacheData(c.l2,address)
		if ret2:
			self.countL2 += 1
			if not self.setSACacheData(c.l1d, address, value):
				self.fetchCacheData(c, mmem, address)
			return 2
		ret3, value = self.getSACacheData(c.l3,address)

		if ret3:
			self.countL3 += 1
			if not self.setSACacheData(c.l1d, address, value):
				self.fetchCacheData(c, mmem, address)
			if not self.setSACacheData(c.l2, address, value):
				self.fetchCacheData(c, mmem, address)
			return 3

		if address >= mmem.mainsize or address < 0:
			self.countError += 1
			return -1

		self.fetchCacheData(c, mmem, address)
		self.countMem += 1
		return 4

	def getCacheInstruction(self, c, mmem, address):
		ret1, value = self.getSACacheData(c.l1i,address)
		if ret1:
			self.countL1i += 1
			return 1
		ret2, value = self.getSACacheData(c.l2,address)
		if ret2:
			self.countL2 += 1
			if not self.setSACacheData(c.l1i, address, value):
				self.fetchCacheData(c, mmem, address)
			return 2
		ret3, value = self.getSACacheData(c.l3,address)

		if ret3:
			self.countL3 += 1
			if not self.setSACacheData(c.l1i, address, value):
				self.fetchCacheData(c, mmem, address)
			if not self.setSACacheData(c.l2, address, value):
				self.fetchCacheData(c, mmem, address)
			return 3
		
		if address >= mmem.mainsize or address < 0:
			self.countError += 1
			return -1

		self.fetchCacheInstruction(c, mmem, address)
		self.countMem += 1
		return 4

	def setCacheData(self, c, address, value):
		if self.setSACacheData(c.l1d, address, value):
			self.countL1d += 1
			#print "Hit 1"
			return 1

		elif self.setSACacheData(c.l2, address, value):
			self.countL2 += 1
			#print "Hit 2"
			return 2

		elif self.setSACacheData(c.l3, address, value):
			self.countL3 += 1
			#print "Hit 3"
			return 3

		else: 
			self.countMem += 1
			#print "Hit 4"
			return 4

	def setCacheInstruction(self, c, address, value):
		if self.setSACacheData(c.l1i, address, value):
			self.countL1d += 1
			#print "Hit 1"
			return 1

		elif self.setSACacheData(c.l2, address, value):
			self.countL2 += 1
			#print "Hit 2"
			return 2

		elif self.setSACacheData(c.l3, address, value):
			self.countL3 += 1
			#print "Hit 3"
			return 3

		else: 
			self.countMem += 1
			#print "Hit 4"
			return 4

	def duplicateCache(self, c):
		self.duplicateSACache(c.l1d)
		self.duplicateSACache(c.l1i)
		self.duplicateSACache(c.l2)
		self.duplicateSACache(c.l3)
		return self.createCache(c.l1d, c.l1i, c.l2, c.l3)

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
		self.setSACacheLine(c.l1i, address, line)

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

	def getMainMemoryData(self, mem, address,value):
		if address < 0 or address > (mem.mainsize -1):
			return -1

		if mem.main[address] != None:
			return 4, mem.main[address]

		return -1, mem.main[address]

	def setMainMemoryData(self, mem, address, value):
		if address < 0 or address > (mem.mainsize -1):
			return -1

		mem.main[address] = value
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
		self.setMainMemoryData(mem.memory, address, value)
		resp = self.setCacheData(mem.cache, address, value)
		if resp == 4 or resp == 3 or resp == 2:
			self.fetchCacheData(mem.cache, mem.memory, address)

	def setInstruction(self, mem, address, value):
		address = int(address)>>2
		self.setMainMemoryData(mem.memory, address, value)
		resp = self.setCacheInstruction(mem.cache, address, value)
		if resp == 4 or resp == 3 or resp == 2:
			self.fetchCacheData(mem.cache, mem.memory, address)

	def duplicateMemory(self, mem):
		return self.createMemory(self.duplicateCache(mem.cache), mem.memory)

	### Processor ###
	def createProcessor(self, mem, ncores):
		mem_list = []
		for i in range(int(ncores)):
			mem_list.append(self.duplicateMemory(mem))
		return Processor(mem_list, ncores)


class TACache():
	def __init__(self, c, l):
		if not powCheck(c):
			raise Pow2Error("Capacity isn't a power of two")
		if not powCheck(l):
			raise Pow2Error("Line size isn't a power of two")
		if (c % l) != 0:
			raise MultipleError(str(c) + " isn't multiple of " + str(l))

		self.offset_size = int(m.log(l,2))
		self.capacity = c
		self.line_size = l
		self.assoc = c/l
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
		if (c % (l*a)) != 0:
			raise MultipleError(str(c) + " isn't multiple of " + str(l*a))
		self.miss = 0
		self.hit = 0
		self.count = 0
		self.associativity = a
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
		self.ramsize = ramsize
		self.vmsize = vmsize
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
		self.memory = mem
		self.ncores = ncores

if __name__ == "__main__":
	v = Validation()
	ins = ''
	for i in range(0,7):
		#print i
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

	while len(v.lines) > 0:
		ins = v.lines[0].split()

		resposta = v.doInstruction(ins)
#		print resposta
		v.lines.remove(v.lines[0])

	v.createOutput()