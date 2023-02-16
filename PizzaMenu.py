class PizzaMenu:
    '''
    Fields: toppings (listof Str), crust(Str), sauce (Str) price (Float)
    '''
    
    ################## DO NOT DELETE ##################
    
    def __init__(self, toppings, crust, sauce, price):
        self.toppings = toppings
        self.crust = crust
        self.sauce = sauce
        self.price = price
    
    def __repr__(self):
        pizza_rep = "Pizza with {0}, {1} sauce, and a {2} crust; the total price is ${3}." 
        topping_str = ", ".join(self.toppings)
        return pizza_rep.format(topping_str, self.sauce, self.crust, self.price)
        
    def __eq__(self, other):
        if isinstance(other,Pizza):
            return self.toppings == other.toppings and self.crust == other.crust and self.sauce == other.sauce and self.price == other.price
        else:
            return False

###### CONSTANTS ########
menu={"HAWAIIAN":
      Pizza(["Traditional Ham",
	     "Smoked Bacon",
	     "Pineapple",
	     "Roasted Red Peppers",
	     "Mozzerela",
	     "Cheese"],
	    "Regular",
	    "Tomatoe",
	    18.99),
            "SPINICH AND FETA PIZZA":
      Pizza(["Alfredo Sauce",
             "Feta Cheese",
             "Baby Spinich",
             "Onion"],
            "Regular",
            "Tomatoe",
            18.99),
            "VEGGIE":
      Pizza(["Fresh Green Peppers",
             "Onion",
             "Tomatoes",
             "Mushrooms",
             "Olives"],
            "Regular",
            "Tomatoe",
            18.99),
            "CANADIAN PIZZA":
      Pizza(["Pepperoni",
             "Mushrooms",
             "Smoked Bacon",
             "Mozzerela"],
            "Regular",
            "Tomatoe",
            18.99),
            "BBQ CHICKEN FEAST":
      Pizza(["BBQ sauce",
             "Chicken",
             "Bacon",
             "Onions",
             "Green Peppers"],
            "Regular",
            "Tomatoe",
            18.99)}


Fake_delivery_pizza_map = {"NEW YORK": [["DUBAI", 11001], ["BEIJING", 10982], ["OTTAWA", 710], ["EGYPT", 2446]],
                           "DUBAI": [["BEIJING", 6000], ["NEW YORK", 11001]],
                           "OTTAWA": [["NEW YORK", 710], ["LONDON", 5400]],
                           "BEIJING": [["DUBAI", 6000], ["LONDON", 8200]],
                           "LONDON": [["BEIJING", 8200], ["OTTAWA", 5400], ["PARIS", 344], ["EGYPT", 3500]],
                           "PARIS": [["EGYPT", 3500], ["LONDON", 344]],
                           "EGYPT": [["NEW YORK", 2446], ["LONDON", 3500], ["PARIS", 3500]]}
    

welcome_msg = "Hello!!  Thanks for coming to Trumps Tasty Pizza!!!  Take a look around and be trump blown away!!!"
goodbye = "Thank you for ordering from Trumps Tasty Pizza today!!  We hope you enjoy your pizza and be sure to share this pizza store with all your friends "
custom_order = "Would you like to place a custom order today?!"
custom_toppings = "What topping would you like to have on your pizza"
custom_sauce = "What type of sauce would you like to have on your pizza?"
custom_crust = "What type of crust would you like on your pizza?"
custom_quant = "How many pizzas would you like to order?!"
            
no_path = "Sorry. There is no feasible path from {0} to {1}."
path = "The shortest path from {0} to {1} is {2} kilometres: {3}."
inf = 10000000000

#########################



def welcome():
    print(welcome_msg)
    print("Enter '1' if you would like to see the menu")
    print("Enter '2' if you would like to search for a particular item")
    print("Enter '3' if you are ready to order")
    
    prompt = input()
    
    ('\n')
    if prompt =='1':
        print('\n')
        for pizza in menu:
            print(pizza)
            print(menu[pizza])
            print('\n')
            
        print("Press 'ENTER' when you are ready to order")
        order = input()
        
        return take_order('regular',  [ ], 0)
            
    elif prompt =='2':
        prompt = input("Enter 'sort' to sort menu by price or 'search' to search for a particular pizza: ")
        if prompt.lower()=='sort':
            print(isort_menu(menu))

            print("Press 'ENTER' when you are ready to order")
            order = input()
            return take_order('regular', [ ], 0) 
            
        elif prompt.lower()=='search':
            Bool=True
            while Bool:
                filter_by = input('Select a filter: toppings or crust? ')
                if filter_by.lower() == 'toppings':
                    filt_by_toppings = (input("Show pizzas with: ")).split(", ")
                    print('\n')
                    print("Showing pizzas with: {0}".format((", ").join(filt_by_toppings)))
                    filter_toppings(filt_by_toppings, menu)
                elif filter_by.lower() == 'crust':
                    filt_by_crust = ("Show pizzas with thin, regular, or thick crust? ")
                    print('\n')
                    print("Showing pizzas with {0} crust".format(filt_by_crust))
                    filter_crust(filt_by_crust, menu) 
                
                reprompt=input("Would you like to keep searching? ")
                if reprompt.lower()=='no':
                    Bool=False
            
            print("Press 'ENTER' when you are ready to order")
            order = input()
            return take_order('regular', [ ], 0)             
    
    elif prompt =='3':

        order_type = input(custom_order)
        if order_type.lower()=='yes':
            return take_order('custom', [ ], 0)
        else:
            return take_order('regular', [], 0)
    
        
    else:
        print (goodbye)

        
        
def take_order(order_type, order_acc, cost_acc):
    if order_type=='done':
        print('\n')
        print('Your total is: {0}'.format(cost_acc))
        print(order_acc)
        print('\n')

        start = input('Please enter your location in the map: ').upper()
        end = input('Please enter your destination in the map: ').upper()

        shortest_path(Fake_delivery_pizza_map, start, end)
        
        print(goodbye)
    
    elif order_type=='regular':
        pizza_order = input('Enter your pizza: ').upper()
        quantity = int(input(('How many of {0} would you like? ').format(pizza_order)))
        order_acc.append([pizza_order, quantity])
        cost_acc = str((quantity * menu[pizza_order].price) + float(cost_acc))
        print('\n')
        print("Your order so far: ")
        print(order_acc)
        print("Your total so far is ${0}".format(cost_acc))
        
        print('\n')        
        
        re_order = input('Would you like to order more? ')
        
        return re_order_prompt(re_order,order_acc,cost_acc)
        
    elif order_type=='custom':
        print('\n')
        toppings = input(custom_toppings)
        crust = input(custom_crust)
        sauce = input(custom_sauce)
        list_of_toppings = toppings.split(',')
        quantity = int(input(custom_quant))
        custom_name = "Pizza on {0} crust, {1} sauce, with the toppings {2}".format(crust, sauce, toppings)
        custom_price= 14.99 + 1.99*4
        cost_acc = str((quantity * custom_price) + float(cost_acc))
        order_acc.append([custom_name, quantity])
        print('\n')
        print("Your order so far: ")
        print(order_acc)
        print("Your total so far is ${0}".format(cost_acc))
        
        print('\n')
        
        re_order = input('Would you like to order more? ')
        
        return re_order_prompt(re_order, order_acc,cost_acc)
        
def re_order_prompt(re_order, order_acc, cost_acc):
    if re_order.lower() == 'yes':
        type_of_order = input('Enter "r" if you would like to order a regular pizza; "c" if you would like to order a custom pizza: ')
        if type_of_order.lower() == 'r':
            return take_order('regular', order_acc, cost_acc)
        elif type_of_order.lower() == 'c':
            return take_order('custom', order_acc, cost_acc)
        else:
            print('See you next time!')
    else:
        return take_order('done', order_acc, cost_acc)

## FILTERS and SORTS:

def sublist(lst1, lst2):
    set1=set(lst1)
    set2=set(lst2)
    return set1.issubset(set2)   

def filter_toppings(toppings, menu):
    filtered_menu = {}
    for pizza in menu:
        if sublist(toppings, menu[pizza].toppings):
            filtered_menu[pizza] = menu[pizza]
    print('\n')
    for pizza in filtered_menu:
        print(pizza)
        print(filtered_menu[pizza])
        print('\n')  

def filter_crust(crust, menu):
    lop= [ ]
    for pizza in menu:
        if crust == menu[pizza].crust:
            lop.append(pizza)
    return lop

## INSERTION SORT:

def list_maker(menu):
    L = [ ]
    for pizza in menu:
        pair = [pizza, menu[pizza].price]
        L.append(pair)
    return L

# insertion sort:

def insert(L, index):
    while index > 0 and L[index][1] < L[index-1][1]:
        current = L[index]
        L[index] = L[index-1]
        L[index-1] = current
        index = index-1

def isort_menu(menu):
    lst=list_maker(menu)
    for index in range(1, len(lst)):
        insert(lst, index)
    return lst


# returns a graph representation of the optimal route from a given node to 
# all the nodes in the graph, and its corresponding 'cost'.

def optimize_route(graph, start):
    results = { }
    
    ### initializes the total costs, start node is at 0; 
    ### all the other nodes are set to a big number 
    ### (which will eventually be changed):
    
    for node in graph:
        if node==start:
            results[start]=[0, start]
        else:
            results[node]=[inf, ""]
            
    queue = {start:0}
    visited = [ ]
    
    ### main loop (this loop will stop once there isn't any nodes in queue)
    
    while queue != { }:
    
        
        ## find the max priority in the queue
        ## (i.e, node with the lowest cost)
    
        min_node_name = "" #placeholder
        min_node_val = inf #placeholder
        for node in queue:
            if queue[node] < min_node_val:
                min_node_name = node
                min_node_val = queue[node]
        
        visited.append(min_node_name)
        
        ## Examine the neighbours of this min_node
        ## we only want the neighbours who have not been visited
        
        del queue[min_node_name]
        visited.append(min_node_name)
        
        neighbours = graph[min_node_name]
        filtered = dict(filter(lambda x: x[0] not in visited, neighbours))
        
        ## now we want to traverse through the filtered neighbours
        
        for node in filtered:
            potential = results[min_node_name][0] + filtered[node]
            
            if potential < results[node][0]:
                results[node] = [potential, min_node_name]
                queue[node] = potential
            
            else:
                queue[node] = filtered[node]
        
    return results


# returns the optimal path from start to end (provided it exists) and its 
# corresponding 'cost', given an optimized graph/tree representation. 

def optimal_route(g, start, end):
    path = [ ] 
    queue = [start]
    dead_end = [ ]
    while queue!= [ ]:
        current = queue.pop()

        
        ## base case in the loop, if current node is the destination => DONE
        ## so add current to path
        
        if current==end:
            path.append(current)
            queue = [ ]
            
        else:
            
            ## we only care if the current is NOT in the path (i.e, not visited)
            if current not in path:
                path.append(current)
                ## we want to find all the nodes that have their last visited
                ## node as the current (this indicates that they are connected)
                neighbours = [ ]
                for node in g:
                    if g[node][1]==current and node!=current:
                        neighbours.append(node)
                        
                # TRAVERSING THROUGH THE NEIGHBOURS:
                
                ## this takes care of the 'dead end' case; if path is a dead-end
                ## we want to backtrack and remove the dead end
                if neighbours ==[ ]:
                    path.remove(current)
                    queue.append(g[current][1])
                    dead_end.append(current)
                    
                
                ## if the node in the neighbour is not in the path (i.e, we 
                ## haven't visited it), add it to the queue of nodes to visit
                for node in neighbours:
                    if node not in path:
                        queue.append(node)
            elif current!=start:
                neighbours = [ ]
                for node in g:
                    if g[node][1] == current:
                        neighbours.append(node)
                
                unvisited =[ ]
                for node in neighbours:
                    if node not in dead_end:
                        unvisited.append(node)
                        
                if unvisited == [ ]:
                    dead_end.append(current)
                    path.remove(current)
                    queue.append(g[current][1])
                
                        
    return [path, g[end][0]]

    
# MAIN FUNCTION

# prints the shortest path from orig to dest, and the total 'cost' of 
# the travel given a weighted graph representation of a map; 
# or error message if path does not exist.

def shortest_path(graph, orig, dest):
    if orig not in graph or dest not in graph:
        print(no_path.format(orig, dest))
    else:
        optimized_graph = optimize_route(graph, orig)
        optimized_path = optimal_route(optimized_graph, orig, dest)
        if optimized_path[1]==inf:
            print(no_path.format(orig,dest))
        else:
            path_str= " to ".join(optimized_path[0])
            print(path.format(orig, dest, optimized_path[1], path_str))

welcome()
