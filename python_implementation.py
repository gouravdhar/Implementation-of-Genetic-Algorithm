from random import randrange


class Individual(object):
	def __init__(self):
		self.fitness = 0
		self.geneLength = 5
		self.genes = [0,0,0,0,0]
		for i in range(self.geneLength) :
			self.genes[i] = randrange(0,2)

	def calc_fitness(self):
		self.fitness = 0
		for i in range(5):
			if self.genes[i] == 1:
				self.fitness = self.fitness + 1

class Population(object):
	def __init__(self):
		self.popsize = 10
		self.fittest = 0
		self.individuals = [None]*10
		for i in range(10):
			self.individuals[i] = Individual() 

	# get fittest individual
	def get_fittest(self):
		self.maxfit = -1
		self.maxfitindex = 0
		for i in range(10):
			if self.maxfit <= self.individuals[i].fitness:
				self.maxfit = self.individuals[i].fitness
				self.maxfitindex = i 

		self.fittest = self.individuals[self.maxfitindex].fitness
		return self.individuals[self.maxfitindex]

	#get second fittest individual
	def get_second_fittest():
		self.maxfit1 = 0
		self.maxfit2 = 0
		for  i in range(10) :
			if self.individuals[i].fitness > self.individuals[maxfitindex].fitness:
				self.maxfit2 = self.maxfit1
				self.maxfit1 = i 

			elif self.individuals[i].fitness > self.individuals[maxfit2].fitness:
				self.maxfit2 = i 

		return self.individuals[maxfit2]

	def get_least_fittest_index():
		self.minfitval = 6
		self.minfitindex = 0
		for i in range(10):
			if self.minfitval >= self.individuals[i].fitness:
				self.minfitval = self.individuals[i].fitness
				self.minfitindex = i
		return self.minfitindex

	def calculate_fitness(self):
		for i in range(10):
			self.individuals[i].calc_fitness()
		self.get_fittest()


if __name__ == '__main__':

	population = Population()
	# Individual fittest
	# Individual get_second_fittest
	generationCount = 0
	population.calculate_fitness()
	# population.calculate_fitness();
	print (population.fittest)