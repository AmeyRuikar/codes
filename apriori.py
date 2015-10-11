
min_sup = 2
min_con = 0.8

temp = []
L2 = []
L3= []
count = 0

one = 1


class transactions:

    def __init__(self, list, id):

        self.list = list
        self.id = id
        list.pop()

class itemset:

    def __init__(self, list, sup_cnt):
        self.ilist = list
        self.sup_cnt = sup_cnt


def prune(plist):

    flag =0
    print("prune")
    
    m = 0

    while(1):
        
        if plist[m].sup_cnt < min_sup:
            del plist[m]
            print(m)
            m = m - 2
            

        m = m + 1
        if m == len(plist):
            break
 


    return len(plist)

def join(plist, trans_objs):

    print("Join")
    cnt = 0 
    f2 =1

    for l in range(len(plist) - 1 ):
        
        for m in range(l+1,len(plist)):

            temp = plist[l].ilist + plist[m].ilist

            set1 = set(temp)

            if one == 0:
                
                for u in range(len(L3)):
                    if set(L3[u].ilist) == set1:
                        f2 = 0
            if f2 ==0:
                continue
            
            temp = list(set1)
            
            if one:
                L2.append(itemset(temp,0))
            else:            
                L3.append(itemset(temp,0))
                
    if one:
        size = len(L2)
    else:
        size = len(L3)
    

    
    for l in range(size):

        cnt = 0

        for m in range(len(trans_objs)):

            
            if one:
                
                if str (L2[l].ilist[0]) in trans_objs[m].list and str(L2[l].ilist[1]) in trans_objs[m].list:

                    cnt = cnt + 1
            else:
                if str (L3[l].ilist[0]) in trans_objs[m].list and str(L3[l].ilist[1]) in trans_objs[m].list and str(L3[l].ilist[2]) in trans_objs[m].list:

                    cnt = cnt + 1               
            
        if one:
            L2[l].sup_cnt = cnt
        else:
            L3[l].sup_cnt = cnt

    if one:
        return len(L2)
    else:
        return len(L3)

def gen_rules(alist):

    print("\nRules\n")

    for i in range(len(L2)):

        fset1 = frozenset(L2[i].ilist)

        for m in range(len(L3)):

            fset2 = frozenset(L3[m].ilist)

            if fset1.issubset(fset2):

                if L3[m].sup_cnt/ L2[i].sup_cnt >= min_con:

                    print(L2[i].ilist," -> ", list(fset2 - fset1),"\t" ,L3[m].sup_cnt/ L2[i].sup_cnt, " selected")
                else:
                                       print(L2[i].ilist," -> ", list(fset2 - fset1),"\t" ,L3[m].sup_cnt/ L2[i].sup_cnt, " rejected")
                    


def gen_rules_2(alist):
    
    print("\nRules\n")
    for i in range(len(L1)):

        fset1 = frozenset(L1[i].ilist)

        for m in range(len(L2)):

            fset2 = frozenset(L2[m].ilist)

            if fset1.issubset(fset2):

                if L2[m].sup_cnt/ L1[i].sup_cnt >= min_con:

                    print(L1[i].ilist," -> ", list(fset2 - fset1),"\t" ,L2[m].sup_cnt/ L1[i].sup_cnt, " selected")
                else:
                    print(L1[i].ilist," -> ", list(fset2 - fset1),"\t" ,L2[m].sup_cnt/ L1[i].sup_cnt, " rejected")
                    
                

                


fo = open("transactions.txt","r")

trans = []
trans_objs = []

L1 = []

i = 0

for line in fo:

    trans = line.split(' ')
    trans_objs.append(transactions(trans,i+1))
    i = i + 1
    'print(i)'

print("transaction", "\t\t", "item-set")    

for k in range(i):
    print(trans_objs[k].id, "\t\t\t", trans_objs[k].list)
    

for k in range(5):

    for m in range(i):
        
        if str((k+1)) in trans_objs[m].list:
            count = count + 1

    temp = [k + 1]       
    
    L1.append(itemset(temp,count))

    count = 0 

    
print("\nL1")
for k in range(5):
    print(L1[k].ilist,"-",L1[k].sup_cnt )

no = prune(L1)

for k in range(no):
    print( L1[k].ilist,"-",L1[k].sup_cnt )

# while no > 1   


no = join(L1, trans_objs)

for k in range(no):
    print( L2[k].ilist,"-",L2[k].sup_cnt )

no = prune(L2)

for k in range(no):
    print( L2[k].ilist,"-",L2[k].sup_cnt )
one = 0

no = join(L2, trans_objs)

for k in range(no):
    print( L3[k].ilist,"-",L3[k].sup_cnt )

no = prune(L3)



set2 = set(L3)
L3 = list(set2)

for k in range(len(L3)):
    print( L3[k].ilist,"-",L3[k].sup_cnt )



gen_rules_2(L2[k].ilist)

gen_rules(L3[k].ilist)


