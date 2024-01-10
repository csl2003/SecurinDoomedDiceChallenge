def undoom_dice(die_A, die_B):
    combA=combinations([2,2,2,2,3,3,3,3], 4)
    combinationsA=[]
    for i in combA:
        l=[1]+list(i)+[4]
        combinationsA.append(l)
    combinationsB=combinations([1,2,3,4,5,6,7,8], 6)
    total_outcomes=len(die_A)*len(die_B) 
    for i in combinationsA:
        for j in combinationsB:
            if is_same_prob(i, j, total_outcomes, [2,3,4,5,6,7,8,9,10,11,12]):
                return i, j
    return None, None  
    

def is_same_prob(i, j, total_probability, possible_sums):
    total_outcomes=len(die_A)*len(die_B)  
    actual={}
    for outcome in range(2, 13):
        count=0
        for faceA in die_A:
            for faceB in die_B:
                if faceA+faceB==outcome:
                    count+= 1

        actual[outcome]=count/total_outcomes
    
    new={}
    for outcome in range(2, 13):
        count=0
        for faceA in i:
            for faceB in j:
                if faceA+faceB==outcome:
                    count+= 1

        new[outcome]=count/total_outcomes
    
    for actual_prob, new_prob in zip(list(actual.values()), list(new.values())):
        if abs(actual_prob-new_prob)!=0:
            return False
    return True
    
    
def combinations(l, leng):
    comb = []

    def helper(curr, l1, k):
        if k == 0:
            comb.append(curr[:])
            return
        for i in range(len(l1)):
            curr.append(l1[i])
            helper(curr, l1[i + 1:], k - 1)
            curr.pop()

    helper([], l, leng)
    return comb


die_A=[1,2,3,4,5,6]
die_B=[1,2,3,4,5,6]
newdice_a, newdice_b=undoom_dice(die_A, die_B)
print("DICE A VALUES : ", newdice_a,"\nDICE B VALUES : ",newdice_b)
