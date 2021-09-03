F AStarSearch(start, end, barriers)
   F heuristic(start, goal)
      V D = 1
      V D2 = 1
      V dx = abs(start[0] - goal[0])
      V dy = abs(start[1] - goal[1])
      R D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
 
   F get_vertex_neighbours(pos)
      [(Int, Int)] n
      L(dx, dy) [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
         V x2 = pos[0] + dx
         V y2 = pos[1] + dy
         I x2 < 0 | x2 > 7 | y2 < 0 | y2 > 7
            L.continue
         n.append((x2, y2))
      R n
 
   F move_cost(a, b)
      L(barrier) @barriers
         I b C barrier
            R 100
      R 1
 
   [(Int, Int) = Int] G
   [(Int, Int) = Int] f
 
   G[start] = 0
   f[start] = heuristic(start, end)
 
   Set[(Int, Int)] closedVertices
   V openVertices = Set([start])
   [(Int, Int) = (Int, Int)] cameFrom
 
   L openVertices.len > 0
      (Int, Int)? current
      V currentFscore = 0
      L(pos) openVertices
         I current == N | f[pos] < currentFscore
            currentFscore = f[pos]
            current = pos
 
      I current == end
         V path = [current]
         L current C cameFrom
            current = cameFrom[current]
            path.append(current)
         path.reverse()
         R (path, f[end])
 
      openVertices.remove(current)
      closedVertices.add(current)
 
      L(neighbour) get_vertex_neighbours(current)
         I neighbour C closedVertices
            L.continue
         V candidateG = G[current] + move_cost(current, neighbour)
 
         I neighbour !C openVertices
            openVertices.add(neighbour)
         E I candidateG >= G[neighbour]
            L.continue
 
         cameFrom[neighbour] = current
         G[neighbour] = candidateG
         V H = heuristic(neighbour, end)
         f[neighbour] = G[neighbour] + H
 
   X RuntimeError(‘A* failed to find a solution’)
 
V (result, cost) = AStarSearch((0, 0), (7, 7), [[(2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)]])
print(‘route ’result)
print(‘cost ’cost)