def missionaries_and_cannibals():
   start_state = (3, 3, 'left', 0, 0)
   goal_state = (0, 0, 'right', 3, 3)
   queue = [(start_state, [])]
   visited = set()
   
   def is_valid(state):
       ml, cl, _, mr, cr = state
       if ml < 0 or cl < 0 or mr < 0 or cr < 0:
           return False
       if ml > 0 and ml < cl:
           return False
       if mr > 0 and mr < cr:
           return False
       return True
   
   while queue:
       state, path = queue.pop(0)
       if state in visited:
           continue
       visited.add(state)
       if state == goal_state:
           for p in path:
               print(p)
           return
       ml, cl, boat, mr, cr = state
       if boat == 'left':
           next_states = [
               (ml - 2, cl, 'right', mr + 2, cr),
               (ml, cl - 2, 'right', mr, cr + 2),
               (ml - 1, cl - 1, 'right', mr + 1, cr + 1),
               (ml - 1, cl, 'right', mr + 1, cr),
               (ml, cl - 1, 'right', mr, cr + 1)
           ]
       else:
           next_states = [
               (ml + 2, cl, 'left', mr - 2, cr),
               (ml, cl + 2, 'left', mr, cr - 2),
               (ml + 1, cl + 1, 'left', mr - 1, cr - 1),
               (ml + 1, cl, 'left', mr - 1, cr),
               (ml, cl + 1, 'left', mr, cr - 1)
           ]
       for next_state in next_states:
           if is_valid(next_state):
               queue.append((next_state, path + [next_state]))
   
   print("No solution found")
 
missionaries_and_cannibals()
