from graph_class import Graph

##############
### GRAPHS ###
##############

A_graph = Graph({1:{2}, 2:{1,3}, 3:{2,4,5,8}, 4:{3,5,6,7,8}, 5:{3,4,6,7,8}, 6:{4,5,7,8}, 7:{4,5,6,8}, 8:{3,4,5,6,7}})
Edgy = Graph({0:{1},1:{0}})
K3x3 = Graph({1:{4,5,6}, 2:{4,5,6}, 3:{4,5,6}, 4:{1,2,3}, 5:{1,2,3}, 6:{1,2,3}})
Test_disconnected_graph = Graph({1:{2,3}, 2:{1,3}, 3:{1,2}, 4:{5,6,7}, 5:{4,6,7}, 6:{4,5,7}, 7:{4,5,6}})
Triangle = Graph.Complete_graph(3)
K5 = Graph.Complete_graph(5)
Complete100 = Graph.Complete_graph(100)
Petersen_graph = Graph.Generalized_Petersen_graph(5,2)
Cycle7 = Graph.Cycle(7)

brock200_2	=	Graph('brock200-2','stb')
brock200_4	=	Graph('brock200-4','stb')
brock400_2	=	Graph('brock400-2','mtx')
brock400_4	=	Graph('brock400-4','stb')
C125_9		=	Graph('C125-9', 'stb')
C250_9		=	Graph('C250-9','stb')
C500_9		=	Graph('C500-9','mtx')
C1000_9		=	Graph('C1000-9','mtx')

####################
### CODE FOR CVC ###
####################

G = C250_9  # you can change graph here
iterations = 1

CVC = G.GRASP_CVC_star(iterations)
print('The algorithm found a CVC with',len(CVC),'vertices')

help(Graph)

