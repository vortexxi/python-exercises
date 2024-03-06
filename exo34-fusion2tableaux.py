def fusion_2_tableaux(tab1, tab2, master):
    for element in tab1:
        master.append(element)

    for element in tab2:
        master.append(element)


tableau1 = [1, 2, 3, 4, 5]
tableau2 = [6, 7, 8, 9, 10]
master_tableau = []

fusion_2_tableaux(tableau1, tableau2, master_tableau)
print(master_tableau)
