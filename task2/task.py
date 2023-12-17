import csv

def process_file(file_data):
    
    state_matrix = []
    for i in range(6):
        state_matrix.append([0, 0, 0, 0, 0, 0])
    for i in file_data:
        state_matrix[int(i[0])-1][int(i[1])-1] = 1
        state_matrix[int(i[1])-1][int(i[0])-1] = -1


    direct_control = []
    for i in range(len(state_matrix)):
        for v in state_matrix[i]:
            if v == 1: 
                direct_control.append(i+1)
                break


    direct_subordination = []
    for i in range(len(state_matrix)):
        for v in state_matrix[i]:
            if v == -1: 
                direct_subordination.append(i+1)
                break
            

    mediocre_control = []
    for i in range(len(state_matrix)):
        for j in range(len(state_matrix)):
            if state_matrix[i][j] == 1:
                for el in state_matrix[j]:
                    if el == 1:
                        mediocre_control.append(i+1)
                        break
    

    medicore_subordination = []
    for i in range(len(state_matrix)):
        for j in range(len(state_matrix)):
            if state_matrix[i][j] == -1:
                for el in state_matrix[j]:
                    if el == -1:
                        medicore_subordination.append(i+1)
                        break
            

    cosubordination = []
    for i in range(len(state_matrix)):
        if state_matrix[i].count(1) > 1:
            for j in range(len(state_matrix)):
                if state_matrix[i][j] == 1:
                    cosubordination.append(j+1)
                    
    return [direct_control, direct_subordination, mediocre_control, medicore_subordination, cosubordination]

with open('task2/example.csv', 'r') as file:
        file_iter = csv.reader(file)
        rows = list(file_iter)

print(process_file(rows))
