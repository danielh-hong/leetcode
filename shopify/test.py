print(set([1, 2, 3 ,4 ,5]))

for i in "asldkjflsajdf":
  print(i)


result = []
for p1 in p1_genes:
    for p2 in p2_genes:
        valid = False
        
        # For each parent's gene pair, try every possible gene they could give to child
        for g1 in p1:  # Try each gene from parent1's pair
            for g2 in p2:  # Try each gene from parent2's pair
                # Order the child's genes correctly (A/B before O)
                if g1 == "O" or (g2 in "AB" and g1 not in "AB"):
                    child_genes = g2 + g1
                else:
                    child_genes = g1 + g2
                
                # Check if these genes give the correct blood type
                if child_genes in gene_to_phenotype and gene_to_phenotype[child_genes] == child:
                    valid = True
                    break
            if valid:
                break
        
        # If this parent combination could produce the child's blood type
        if valid:
            result.append([p1, p2])


def f1(kid, p1, p2):
    dic = {"A": [["A","A"],["A","O"]], "B": [["B","B"],["B","O"]], "AB": [["A","B"]], "O": [["O","O"]]}
    kp = dic[kid]
    pp = []
    for i in kp:
        for j in dic[p1]:
            if j.__contains__(i[0]) == True:
                for k in dic[p2]:
                    if k.__contains__(i[1]) == True and pp.__contains__([j,k]) == False:
                        pp.append([j,k])
            if j.__contains__(i[1]) == True:
                for k in dic[p2]:
                    if k.__contains__(i[0]) == True and pp.__contains__([j,k]) == False:
                        pp.append([j,k])
    if len(pp) == 0:
        return [["--","--"]]
    else: return pp
        