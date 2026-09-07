
def bfs(start, end):
    queue = [start]
    visited = {start}
    path = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            return path
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path[neighbor] = current
    return visited

def dfs(start, end):
    stack = [start]
    visited = {start}
    path = {}
    while stack:
        current = stack.pop();
        if (current == end):
            return path
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                path[neighbor] = current
    return visited