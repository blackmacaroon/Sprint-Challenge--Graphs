from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
world = World()
player = Player("Name", world.startingRoom)
# player.currentRoom.id = the current room id
# player.currentRoom.getExits() = list of exits possible for the current room
# player.travel(direction) = move player to next room

# rooms = nodes/vertexes
# directions = edges
# use a dictionary to track which nodes have been visited and how they're connected
# use DFT?? to traverse graph to all unvisited nodes (because we need the path, we can't jump around)
# end result is a list of the directions of the best possible path to reach all the rooms

#declare empty dictionary 
#declare variables
traversalPath = []
rooms = {}
current_room = player.currentRoom.id
current_exits = player.currentRoom.getExits()
# what's THE THING and when should we do it??
def Mosey():
    #end point, stop when we've visited all the rooms
    while len(rooms) < len(RoomGraph):
        if current_room not in rooms:
# def dft(starting_node, graph):
#     stak = Stack()
#     visited = {}
#     stak.push([starting_vertex])
#     while stak.size() > 0:
#         path = stak.pop()
#         vertex = path[-1]
#         if vertex not in visited:
#             visited[vertex] = path
#             for next_room in graph:
#                 new_path  = path.copy()
#                 new_path.append(next_room)
#                 stak.push(new_path)

# def bft(starting_node, graph):
#     qq = Queue()
#     visited = {}
#     qq.enqueue([starting_node])
#     while qq.size > 0:
#         path = qq.dequeue()
#         #build a path of how we got to this point, then continue on
#         vertex = path[-1]
#         #if this point is not yet visited:
#         if vertex not in visited:
#             visited[vertex] = path
#             for next_room in graph:
#                 new_path = path.copy()
#                 new_path.append(next_room)
#                 qq.enqueue(new_path)
            
            
#             # for direction in current_exits:
#             #     player.travel(direction)
#             #     new_path = list(path)
#             #     new_path.append(node)
#             #     qq.enqueue(new_path)
#             #     print("hmm", path)
#             #     return new_path
#     return visited

    
#get starting room
#check directional exits
#mark as visited
#choose random direction in exits
#travel that way
#get room id
# direction = random.randint(0)
# #travel, add to path
# player.travel(direction)
# #update visited
# if current_room not in visited:
#     visited.add(current_room)
# else, find nearest unexplored room
