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
	def get_second_fittest(self):
		self.maxfit1 = 0
		self.maxfit2 = 0
		for  i in range(10) :
			if self.individuals[i].fitness > self.individuals[self.maxfitindex].fitness:
				self.maxfit2 = self.maxfit1
				self.maxfit1 = i 

			elif self.individuals[i].fitness > self.individuals[self.maxfit2].fitness:
				self.maxfit2 = i 

		return self.individuals[self.maxfit2]

	def get_least_fittest_index(self):
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

class genetic_algo(object):
	def __init__(self):
		self.population = Population()
		self.generationCount = 0

	def selection(self):
		self.fittest = self.population.get_fittest()
		self.secondfittest = self.population.get_second_fittest()

	def crossover(self):
		self.crossoverpoint = randrange(0,5)
		for i in range(self.crossoverpoint):
			self.temp = self.fittest.genes[i]
			self.fittest.genes[i] = self.secondfittest.genes[i]
			self.secondfittest.genes[i] = self.temp

	def mutation(self):
		self.mutationpoint = randrange(0,5)
		if self.fittest.genes[self.mutationpoint] == 0:
			self.fittest.genes[self.mutationpoint] = 1
		else :
			self.fittest.genes[self.mutationpoint] = 0

		self.mutationpoint = randrange(0,5)
		if self.secondfittest.genes[self.mutationpoint] == 0:
			self.secondfittest.genes[self.mutationpoint] = 1
		else :
			self.secondfittest.genes[self.mutationpoint] = 0

	def get_fittest_offspring(self):
		if self.fittest.fitness > self.secondfittest.fitness :
			return self.fittest
		else:
			return self.secondfittest

	def add_fittest_offspring(self):
		self.fittest.calc_fitness()
		self.secondfittest.calc_fitness()
		self.leastfittestindex = self.population.get_least_fittest_index()
		self.population.individuals[self.leastfittestindex] = self.get_fittest_offspring()







if __name__ == '__main__':

	demo = genetic_algo()
	demo.population.calculate_fitness()
	print ("Generation: ", demo.generationCount, " Fittest: ",demo.population.fittest)
	dummy = demo.population.fittest
	max_till_now = 0 
	while dummy < 5:
		demo.generationCount = demo.generationCount + 1
		demo.selection()
		demo.crossover()
		if randrange(0,7) < 5:
			demo.mutation()
		demo.add_fittest_offspring()
		demo.population.calculate_fitness()
		print ("Generation: ", demo.generationCount, " Fittest: ",demo.population.fittest)
		dummy = demo.population.fittest
		if demo.population.fittest > max_till_now:
			max_till_now = demo.population.fittest
		#if no. of generations exceeds 20000 we stop furthur calculations
		if demo.generationCount > 20000:
			if demo.population.fittest >= max_till_now:
				dummy = 5 
			
	print("Solution found in generation: ",demo.generationCount)
	print("Fitness: ",demo.population.get_fittest().fitness)
	for i in range(5):
		print(demo.population.get_fittest().genes[i])
 