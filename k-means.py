#! /usr/bin/python


import math


sample = [[1.0,1.0],[1.5, 2.0], [3.0, 4.0], [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]]
slist = []
mean = []



class Data:
    def __init__(self,a , b, cluster):
        self.a = a
        self.b = b
        self.cluster = cluster


    def get_a():
        return self.a

    def get_b():
        return self.b

    def set_cluster(cluster):
        self.set_cluster = cluster

    def get_cluster():
        return self.cluster


class centroid:
    def __init__( self,a , b, num):
        self.a =a
        self.b = b
        self.num = num

    def get_cen_a():
        return self.a

    def get_cen_b():
        return self.b

    
def assign_cluster(x,y, mean):

    d0 = math.sqrt(math.pow(x - mean[0].a,2) + math.pow(y -mean[0].b ,2))
    
    d1 = math.sqrt(math.pow(x - mean[1].a,2) + math.pow(y - mean[1].b ,2))
    
    if ( d0 < d1 ):

        mean[0].a = mean[0].a * mean[0].num
        mean[0].b = mean[0].b * mean[0].num
        
        mean[0].a = mean[0].a + x
        mean[0].b = mean[0].b + y
        
        mean[0].num = mean[0].num + 1
        
        mean[0].a = mean[0].a / mean[0].num
        mean[0].b = mean[0].b / mean[0].num

        print("mean cluster 0:", mean[0].a,"\t",mean[0].b)
        
        return 0
    
    else:
        
        mean[1].a = mean[1].a * mean[1].num
        mean[1].b = mean[1].b * mean[1].num
        
        mean[1].a = mean[1].a + x
        mean[1].b = mean[1].b + y
        
        mean[1].num = mean[1].num + 1
        
        mean[1].a = mean[1].a / mean[1].num
        mean[1].b = mean[1].b / mean[1].num
        
        print("mean cluster 1:", mean[1].a,"\t",mean[1].b)
        return 1    


def k_means(x,y,mean):

    d0 = math.sqrt(math.pow(x - mean[0].a,2) + math.pow(y -mean[0].b ,2))
    
    d1 = math.sqrt(math.pow(x - mean[1].a,2) + math.pow(y - mean[1].b ,2))

    if (d0 > d1):
        return 1
    else:
        return 0
    
def update_centroid(slist):
    cnt0 = 0
    cnt1 = 0
    sum_0_a = 0
    sum_0_b = 0
    sum_1_a = 0
    sum_1_b = 0
    
    for i in range(7):

        if slist[i].cluster == 0:
            cnt0 = cnt0 + 1
            sum_0_a = sum_0_a + slist[i].a
            sum_0_b = sum_0_b + slist[i].b
        else:
            cnt1 = cnt1 + 1
            sum_1_a = sum_1_a + slist[i].a
            sum_1_b = sum_1_b + slist[i].b           

    if cnt0 != 0:
        
        mean[0].a = sum_0_a /cnt0
        mean[0].b = sum_0_b /cnt0
        
    if cnt1 != 0:
        mean[1].a = sum_1_a /cnt1
        mean[1].b = sum_1_b /cnt1


    
    return

'---------exe--------'
print("Student\tSubj A\tSubj B") 

for i in range(7):
    print(i,"\t",sample[i][0],"\t",sample[i][1])
    
    slist.append(Data(sample[i][0],sample[i][1],0))
   

slist[3].cluster = 1
mean.append(centroid(sample[0][0],sample[0][1],1))
mean.append(centroid(sample[3][0],sample[3][1],1))

print("centroid for 2 groups: 0 & 3")

print("Student\tCluster number") 

for i in range(7):

    if i != 0 and i!=3:
        
        slist[i].cluster = assign_cluster(slist[i].a,slist[i].b,mean )
        print ("placed - ",i,"\tin cluster ", slist[i].cluster)
        print("\n")


print("\nmean cluster 0: a", mean[0].a,"\tb", mean[0].b )
print("mean cluster 1: a", mean[1].a,"\tb", mean[1].b )

flag = 1

while flag == 1:

    flag = 0
    print("start round")
    for i in range(7):
    
        new_cluster = k_means(slist[i].a,slist[i].b,mean)

        if new_cluster != slist[i].cluster:
            flag = 1
            slist[i].cluster = new_cluster
            print("student ",i," moved to cluster ",new_cluster)

    print("\n end of round ")
    update_centroid(slist)
    print("mean cluster 0: a", mean[0].a,"\tb", mean[0].b )
    print("mean cluster 1: a", mean[1].a,"\tb", mean[1].b )


print("\n Final cluster for students")

print(" student\tcluster number")
for i in range(7):

    print(" ",i,"\t",slist[i].cluster)
    
