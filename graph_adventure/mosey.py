
# player.currentRoom.id = the current room id
# player.currentRoom.getExits() = list of exits possible for the current room
# player.travel(direction) = move player to next room

# rooms = nodes/vertexes
# directions = edges
# use a dictionary to track which nodes have been visited and how they're connected
# use DFT?? to traverse graph to all unvisited nodes (because we need the path, we can't jump around)
# end result is a list of the directions of the best possible path to reach all the rooms
////////////////////////////////////////////////////////////
    
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


#declare empty dictionary 
#declare variables
# traversalPath = []
# rooms = {}
# current_room = player.currentRoom.id
# current_exits = player.currentRoom.getExits()
# # what's THE THING and when should we do it??
# def Mosey():
#     #end point, stop when we've visited all the rooms
#     while len(rooms) < len(RoomGraph):
#         if current_room not in rooms:
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

/////////////////////////////////////////////////////////////////
# add a dictionary of rooms with ids and their exits
# def add_room(current_room, room_dictionary):
#     room_dictionary[current_room] = rooms
#     # if there is anything in exits, make it a question mark so we can find unvisited paths later
#     for direction in exits:
#         room_dictionary[current_room][direction] = '?'
#     print("room added", current_room)
#     return rooms
    
    
# # naive dfs
# def mosey(starting_room):
#     stak = Stack()
#     visited = []
#     stak.push(starting_room)
#     # while loop, stop when we've visited all the rooms
#     while len(rooms) < len(RoomGraph):
#         print("current room:", current_room) #infinite loop, doesn't leave room
#         # if we haven't been here, add it to the room dictionary
#         if current_room not in rooms:
#             add_room(current_room, rooms)
#         # random direction, loop through exits?
#         # for i in range(0, len(exits)):

#         # next_room = 
#         previous_room = traversalPath[-1]
#         if previous_room in rooms[current_room] and rooms[current_room][previous_room] == '?':
#             next_room = previous_room
#         else:
#             for direction in rooms[current_room]:
#                 if rooms[current_room][direction] == '?':
#                     next_room = direction
#                     print("", direction)
#                     break
#         if next_room is None:
#             # dead end, backtrack
#             reverse = stak.pop()
#             player.travel(reverse)
#             traversalPath.append(reverse)
#         else:
#             # travel in a direction
#             player.travel(next_room)
#             traversalPath.append(next_room)
#             stak.push(next_room)
#             rooms[current_room][next_room] = player.currentRoom
        
///////////////////////////////////////////////////////////////////

    #end point, stop when we've visited all the rooms
    #none of this will run if we have the same # of rooms in the dictionary and graph
# while len(rooms) < len(RoomGraph):
#     if current_room not in rooms:
#         print("cake")
#         rooms[current_room] = traversalPath

#         break
    # if dead end, bfs(current_room, destination room)
