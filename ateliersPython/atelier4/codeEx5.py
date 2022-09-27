import time
import matplotlib.pyplot as plt
import numpy as np
import random
#-----------------------fin des importartations---------------------------------------------------------
def mix_list(list_to_mix:list) -> list:
    return random.sample(list_to_mix, len(list_to_mix))
#-------------------------------------------------------------------------------------------------------
def extract_elements_list(list_in_which_to_choose:list, int_of_element_to_extract:int = 9) -> list:
    return [random.choice(list_in_which_to_choose) for i in range(int_of_element_to_extract)]
#-------------------------------------------------------------------------------------------------------
listeTaille = [10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000]
axis_mixList = [0]
axis_shuffle = [0]
axis_extract_elements_list = [0]
axis_sample = [0]
for j in listeTaille:
    LIST_TEST = [random.randint(0,10) for i in range(j)]
    #---------------------test extract element-------------------
    start_pc = time.perf_counter()
    extract_elements_list(LIST_TEST)
    end_pc = time.perf_counter()
    axis_extract_elements_list.append(end_pc-start_pc)
    #------------------------------------------------------------
    start_pc2 = time.perf_counter()
    random.sample(LIST_TEST,9)
    end_pc2 = time.perf_counter()
    axis_sample.append(end_pc2-start_pc2)
    #--------------------test mixlist----------------------------
    start_pc = time.perf_counter()
    mix_list(LIST_TEST)
    end_pc = time.perf_counter()
    axis_mixList.append(end_pc-start_pc)
    #------------------------------------------------------------
    start_pc2 = time.perf_counter()
    random.shuffle(LIST_TEST)
    end_pc2 = time.perf_counter()
    axis_shuffle.append(end_pc2-start_pc2)
#-------------------------------------------------------------------------------------------------------
fig, ax = plt.subplots()
ax.plot(listeTaille,axis_mixList,'bo-',label='mix_liste')
ax.plot(listeTaille,axis_shuffle, 'r*-', label='shuffle')
ax.plot(listeTaille,axis_extract_elements_list,'g^-',label='extract_elements_list')
ax.plot(listeTaille,axis_sample, 'yx-', label='sample')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',title='comparaison fonction python et moi')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')

plt.show()

