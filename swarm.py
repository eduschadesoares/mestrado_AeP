import random
import numpy as np

max_it = 10000
factor = 0.5 / max_it
stop_crit = 0.02
benchmark_qntd = 20
w = 0.9
min_func = -10
max_func = 10
population = 30
dimension = 30
fitness_S = []
fitness_Pbest = []
global_best = []
control_new_global = False


#populacao é Swarm (S)
#individuo é a Partícula (Xi)

def initialization():
    global S, P_best, Vel

    #Initialization of S, PBest and Velocity
    S = init_swarm()
    P_best = init_swarm()
    Vel = init_swarm()

    #print vector
    #print_swarms("Xi", S)
    #print_swarms("P_best", P_best)
    #print_swarms("Velocity", Vel)

    #Get initial global best
    g_best(S)

def clear():
    global S, P_best, Vel

    S.clear()
    P_best.clear()
    Vel.clear()

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
    return fit_particle

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

def vel_update(each, w):
    #w = round(random.uniform(0.4, 0.9),1)

    C1, C2 = 2,2

    #print("validaocao***********")
    #print("P_BEST", P_best[each])
    #print("S", S[each])

    array1 = np.array(P_best[each])
    array2 = np.array(S[each])
    array3 = np.array(global_best[each])

    A = np.subtract(array1, array2)
    B = np.subtract(array3, array2)
    
    #print("Subtraido A", A)
    #print("Subtraido B", B)

    personal_weight = C1 * round(random.uniform(0, 1),1) * A
    global_weight = C2 * round(random.uniform(0, 1),1) * B

    #print("personal w", personal_weight)
    #print("global w", global_weight)

    temp_vec = []

    for i in Vel[each]:
        temp_vec.append(round(i * w, 1))

    #print("Retorno:", round(temp_vec + personal_weight + global_weight, 1))
    return temp_vec + personal_weight + global_weight
    
def benchmark():
    var_ = 0
    while var_ < benchmark_qntd:
        
        initialization()
        print(main())
        var_ += 1
        clear()

def main():
    i = 1
    global global_best, control_new_global, w
    #laço enorme
    while i < max_it + 1:
        
        if fitness_sphere(global_best) > stop_crit:

            w = w - factor 
            #for in population
            for each in range (len(S)):
                fitness_S.append(fitness_sphere(S[each]))
                fitness_Pbest.append(fitness_sphere(P_best[each]))

                #fit_S = fitness_sphere(S[each])
                #fit_P_best = fitness_sphere(P_best[each])

                #verify personal best
                if fitness_sphere(S[each]) < fitness_sphere(P_best[each]):
                    P_best[each] = S[each]

                #verify global best
                if fitness_sphere(P_best[each]) < fitness_sphere(global_best):
                    global_best = P_best[each]
                    #print("- New Global Best:", global_best, "Fitness:", fitness_sphere(global_best))
                    control_new_global = True

                # Atualização de Velocidade
                # Veli = W * Veli + C1 * RND(0~1) * (Pbi - Xi) + C2 * RND(0~1) * (Gb - Xi)
                # Xi = Xi + Vi

                #print("Antes:", S[each])
                S[each] = S[each] + vel_update(each, w)
                #print("atualizado **********", S[each])
                
            #update each iteration
            #(print("Iteration:", i))
        else:
            return i
        i += 1


benchmark()

#Main function
#main()
print("")

print("Final Fitness", f'{fitness_sphere(global_best):.20f}')

#if there's a new global best, then print
#if control_new_global:
   # print_swarms("New P_best - UPDATED", P_best)

