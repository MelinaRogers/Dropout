import numpy as np
import random

input_nodes = 10
hidden_nodes = 5
output_nodes = 7

#wih = weights between input and hidden layer
wih = np.random.randint(-10, 10, (hidden_nodes, input_nodes))
#print(wih , "\n")
#woh = weights between hidden and output layer
who = np.random.randint(-10, 10, (output_nodes, hidden_nodes))
#print(woh)

active_input_percentage = 0.7
active_output_percentage = 0.7

active_input_nodes = int(active_input_percentage * input_nodes)
active_input_indices = sorted(random.sample(range(0, input_nodes), active_input_nodes))

active_hidden_nodes = int(active_output_percentage * hidden_nodes)
active_hidden_indices = sorted(random.sample(range(0,hidden_nodes), active_hidden_nodes))


wih_old = wih.copy()
wih = wih[:,active_input_indices] #only takes columns with active nodes

who_old = who.copy()
who = who[:active_hidden_indices]