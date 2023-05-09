import random

max_it = 1
min_func = -10
max_func = 10
population = 5
dimension = 5
fitness_S = []
fitness_Pbest = []
global_best = []


#populacao é Swarm (S)
#individuo é a Partícula (Xi)

def init_particle():
    individual = []
    for i in range(population):
        individual.append(round(random.uniform(min_func, max_func),1))
    #print(individuo)
    return individual

def init_swarm():
    # To start a Swarm it needs to have individuals/particles
    vector_population = []
    for i in range(dimension):
        vector_population.append(init_particle())
    #print(poplacao)
    return vector_population

def fitness_sphere(particle):
    #calculo do sphere x^2
    fit_particle = 0
    for each in particle:
        fit_particle += each ** 2
    return round(fit_particle, 2)

def g_best(vector):
    global global_best
    gb_var = vector[0]
    for i in vector:
        if fitness_sphere(gb_var) > fitness_sphere(i):
            gb_var = i
    global_best = gb_var
    #print("Global Best:", global_best, "Fitness:", fitness_sphere(global_best))
    #print("")

def print_swarms(vector_name, vector):
    print("Vector:", vector_name)
    for indiv in range(len(vector)):
    #   print(vector[indiv])
    #   print("Indivíduo", indiv)
        for col in vector[indiv]:
            print("|",f'{col:6.2f}', end=" ")
        print("|", end=" ")
        print("#", fitness_sphere(vector[indiv]))
    print("")

def main():
    i = 0
    global global_best
    #laço enorme
    while i < max_it:
        
        for each in range (len(S)):
            fitness_S.append(fitness_sphere(S[each]))
            fitness_Pbest.append(fitness_sphere(P_best[each]))

            #fit_S = fitness_sphere(S[each])
            #fit_P_best = fitness_sphere(P_best[each])

            if fitness_sphere(S[each]) < fitness_sphere(P_best[each]):
                P_best[each] = S[each]

            if fitness_sphere(P_best[each]) < fitness_sphere(global_best):
                global_best = P_best[each]
                print("- New Global Best:", global_best, "Fitness:", fitness_sphere(global_best))

        i += 1


#Initialization of S, PBest and Velocity
S = init_swarm()
P_best = init_swarm()
Vel = init_swarm()

print_swarms("Xi", S)
print_swarms("P_best", P_best)
#print_swarms("Velocity", Vel)

#Get initial global best
g_best(S)

#Main function
main()

print("")
print_swarms("New P_best", P_best)

#print("Fitness:", fitnesses)

