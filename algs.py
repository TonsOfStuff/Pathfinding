
def bfs(start, end):
    queue = [start]
    visited = {start}
    path = {}
    order = [start]
    while queue:
        current = queue.pop(0)
        if current == end:
            return path, order
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path[neighbor] = current
                order.append(neighbor)
    return None, order

def dfs(start, end):
    stack = [start]
    visited = {start}
    path = {}
    order = [start]          
    if start == end:
        return path, order
    while stack:
        current = stack.pop()
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                path[neighbor] = current
                order.append(neighbor)     
                if neighbor == end:
                    return path, order
                stack.append(neighbor)
    return None, order

