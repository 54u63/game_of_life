from random import randint
def gen_tab(size):
    tab=[]
    for i in range(size):
        temp=[]
        for j in range(size):
            temp.append(randint(0,1))
        tab.append(temp)
    return tab

def print_tab(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j],end="")
        print("")

def output_summ(somme):
    if somme > 3:
        return 0
    if somme < 2:
        return 0
    else: 
        return 1
     
     
def run_line(tab,index,before,after):
    new_lane=[] 
    for i in range(len(tab[index])):
        if i==0:
            summ=sum([before[len(before)-1],before[i],before[i+1],tab[index][len(tab[index])-1],tab[index][i+1],after[len(after)-1],after[i],after[i+1]])
            new_lane.append(output_summ(summ))
        if i==len(tab[index])-1:
            summ=sum([before[i-1],before[i],before[0],tab[index][i-1],tab[index][0],after[i-1],after[i],after[0]])
            new_lane.append(output_summ(summ))
        else: 
            summ=sum([before[i-1],before[i],before[i+1],tab[index][i-1],tab[index][i+1],after[i-1],after[i],after[i+1]])
            new_lane.append(output_summ(summ))
    return(new_lane)


def cycle(tab):
    new_tab=[]
    for i in range(len(tab)):
        if i==0:
            new_tab.append(run_line(tab,i,tab[len(tab)-1],tab[1]))
        if i==len(tab)-1:
            new_tab.append(run_line(tab,i,tab[i-1],tab[0]))
        else:
            new_tab.append(run_line(tab,i,tab[i-1],tab[i+1]))
    return new_tab

tab=gen_tab(10)
print_tab(tab)
for i in range(5):
    new_tab=cycle(tab)
    print("#"*16+"\n"+"#"*16)
    print_tab(new_tab)
    tab=new_tab
