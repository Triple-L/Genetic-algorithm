import numpy as np
from random import randint
#1.Initial population

N = 4
Initial = np.zeros(N)
Initial_1 = np.ones(N)
population=[Initial_1,Initial]

def select_Top2(population):
    max_fit = 0
    second_max = 0
    max_item = []
    second_item=[]
    coefficent = np.array([0.2, 0.3, 0.5, 0.1])
    for item in population:
        Fitness = np.sum(item*coefficent)
        if Fitness > max_fit:
            max_fit = Fitness
            max_item = item
        elif max_fit >= Fitness>= second_max:
            second_max = Fitness
            second_item = item
    return max_fit,max_item,second_max,second_item



def Crossover(Parent1,Parent2):
    cross_point = randint(1, N - 1)
    offSpring1 = np.append(Parent1[:cross_point],Parent2[cross_point:])
    offSpring2 = np.append(Parent2[:cross_point], Parent1[cross_point:])
    print("The Parent_1 and Parent_2 is:",Parent1,Parent2)
    print("The crossovered offSpring is:", offSpring1,offSpring2)
    return offSpring1,offSpring2

def Exist_or_not(Chromosome,Population):
    flag =True
    for x in Population:
        if np.array_equal(x, Chromosome):
            flag =False
    if(flag):
        Population.extend([Chromosome])
    return Population


def mutation(offspring_crossover):
    mut = np.random.rand(4,1)
    print('The mutation number is:',mut)
    offspring_crossover_new=np.zeros(N)
    for index, item in enumerate(mut):
        if item>0.5:
           offspring_crossover_new[index]=1-offspring_crossover[index]
        else:
           offspring_crossover_new[index] = offspring_crossover[index]
    print("The mutated chromosome is:",offspring_crossover_new)
    return offspring_crossover_new


def Population_select(population):
    max=0
    new_population = []
    for item in population:
        print("The item is:",item)
    #for item in population:
        equation1=np.array([0.5,1,1.5,0.1])
        equation2=np.array([0.3,0.8,1.5,0.4])
        equation3=np.array([0.2,0.2,0.3,0.1])
        fit_coefficent =np.array([0.2,0.3,0.5,0.1])
        reward1 = np.sum(item*equation1)
        reward2 = np.sum(item*equation2)
        reward3 = np.sum(item*equation3)
        Fitness = np.sum(item*fit_coefficent)
        print("The Fitness :",Fitness)
        if((reward1<=3.1)&(reward2<=2.5)&(reward3<=0.4)):
            new_population.append([item])
            if Fitness>max:
                max = Fitness
                Fitness_final= Fitness
                max_item =item
    return max_item,Fitness_final,new_population


if __name__ == '__main__':
    #2.Fitness function
    x1,x2,x3,x4 = population[1]
    Fitness = 0.2*x1+0.3*x2+0.5*x3+0.1*x4
    head_count = 2
    head_count_before = 0
    while(head_count!=head_count_before):
        head_count_before=head_count
        head_count=0
#select function
        max_fit,max_item,second_max,second_item = select_Top2(population)
        mut_parent_1 = mutation(max_item)
        mut_parent_2 = mutation(second_item)
        population = Exist_or_not(mut_parent_1, population)
        population = Exist_or_not(mut_parent_2, population)
#3.crossover. Offspring
        offspring_A,offspring_B = Crossover(max_item,second_item)
        print("The generated children1 is :",offspring_A)
        print("The generated children2 is :",offspring_B)
        population = Exist_or_not(offspring_A, population)
        population = Exist_or_not(offspring_B, population)
#4.mutation
        mut_offsp_A=mutation(offspring_A)
        mut_offsp_B=mutation(offspring_B)
        population = Exist_or_not(mut_offsp_A, population)
        population = Exist_or_not(mut_offsp_B, population)

        head_count =np.shape(population)[0]
#5.stopping criterion

    item,Fitness,new_poputalion = Population_select(population)
    head_count = np.shape(new_poputalion)[0]
    print("The population is:", new_poputalion)
    print("Best solution : ",item)
    print("Best solution fitness : ",Fitness)
    print("The size of population: ", head_count)
