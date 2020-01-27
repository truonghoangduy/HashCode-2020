from typing import List,NamedTuple
import glob
file_dict={
    "example":"a_example.in",
    "medium":"c_medium.in",
    "big":"d_quite_big.in"
}


class Item(NamedTuple):
    pizza_type:int
    pizza_slide:int

class problem_Structure(NamedTuple):
    max_slide:int
    Item:List[Item]


def __printTable(table):
    for target_list in table:
        print(target_list)
        pass

def _knapback(items:List[Item],max_capacity:int):
    table=[[0 for x in range(max_capacity+1)] for x in range(len(items)+1)]

    # index base traveling (take a close look)
    for i,item in enumerate(items):
        for each_capacity in range(1,max_capacity+1):

            pre_vaule=table[i][each_capacity];

            if each_capacity >= item.pizza_slide:
                #looking backup to those pre_combination
                __somethingsIDK_=table[i][each_capacity-item.pizza_slide];

                # making the selecting of previous vaule of the upper combination 
                # or this section of combination
                table[i+1][each_capacity]=max(__somethingsIDK_+item.pizza_slide,pre_vaule);
                pass
            else:
                #if it not fit to the backpack with pre combination
                table[i+1][each_capacity]=pre_vaule
            pass
    print()

    ## Create temp varible to handle for the answer
    __result__=[];
    __totalOfSlide=0;
    # __printTable(table)
    __max_capacity=max_capacity;
    ## ----------------------

    #going reversive to check the combination of the table
    for target_list in range(len(items),0,-1):
        if table[target_list][__max_capacity]!=table[target_list-1][__max_capacity]:
            __result__.append(items[target_list-1]);
            # remove the weight
            # create a loop by sub the weights
            __max_capacity-=items[target_list-1].pizza_slide
            pass
        pass

    #counting the total slide that program could taken 
    for target_list in __result__:
        __totalOfSlide+=target_list.pizza_slide
        pass
    pass

    print("Final Anser  : only can take "+str(__totalOfSlide))
    print(__result__)





if __name__ == "__main__":

    # problem variable
    __maxslide__=0;
    PIZZAS: List[Item]=[]
    #------------------
    
    #You can send a problem file to it with .in => Uncomment the bellow line 🤣🤣
    # problem=open(glob.glob("*.in")[0],"r")
    #OR using the code own dictionnary within 4 example 😁😁
    # Un command this line
    problem=open(file_dict["medium"],"r")
    #--------------------------------------
    


    problem_maxslide=int(problem.readline().rstrip('\n').split(" ")[0]);
    # print(problem_maxslide);

    problem_pizzas=problem.readline().rstrip('\n').split(" ")
    

    for i,pizza in enumerate(problem_pizzas):
        PIZZAS.append(Item(int(i),int(pizza)))
    
    # print("total of Pizza")
    # print(PIZZAS)

    _knapback(PIZZAS,problem_maxslide)
    pass