from collections import deque

class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #Get fonksiyonları
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    #Set fonksiyonları
    def set_x(self,new):
        self.x = new
    def set_y(self,new):
        self.y = new

class Character:
    def __init__(self,c_name,c_type,c_loc):
        self.name = c_name
        self.type = c_type
        self.loc = c_loc
    #Get fonksiyonları
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
    def get_loc(self):
        return self.loc
    #Set fonksiyonları
    def set_name(self,new):
        self.name = new
    def set_type(self,new):
        self.type = new
    def set_loc(self,new):
        self.loc = new

    # BFS Algoritması:
    def bfs(start, goal, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        queue = deque([(start.x, start.y, [])])  # Başlangıç noktasından sıraya alıyoruz
        visited = set()
        visited.add((start.x, start.y))
        
        while queue:
            x, y, path = queue.popleft()
            
            # Hedefe ulaştıysak
            if (x, y) == (goal.x, goal.y):
                return path  # En kısa yolu döndürüyoruz
            
            # Komşu hücrelere git
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, path + [(nx, ny)]))
        
        return []  # Hedefe ulaşamazsa boş liste döndür

# Oyuncu Class'ları
class MasterYoda(Character):
    def __init__(self, c_name, c_type, c_loc, heart):
        super().__init__(c_name, c_type, c_loc)
        self.heart = heart

    def get_heart(self):
        return self.heart
    def set_heart(self,new):
        self.heart = new

class LukeSkywalker(Character):
    def __init__(self, c_name, c_type, c_loc, heart):
        super().__init__(c_name, c_type, c_loc)
        self.heart = heart

    def get_heart(self):
        return self.heart
    def set_heart(self,new):
        self.heart = new

# Düşman Class'ları


class DarthVader(Character):
    # Darth Vader için BFS algoritması (Yalnızca ilerlediği yoldaki duvarları yıkar)
    def bfs(start, goal, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Yukarı, Aşağı, Sol, Sağ
        queue = deque([(start.x, start.y, [])])  # Başlangıç noktası
        visited = set()
        visited.add((start.x, start.y))

        while queue:
            x, y, path = queue.popleft()

            # Hedefe ulaştıysak
            if (x, y) == (goal.x, goal.y):
                return path  # En kısa yolu döndür

            # Komşu hücreleri kontrol et
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Sınırları aşmadığımızdan emin olalım
                if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited:
                    visited.add((nx, ny))

                    # Eğer bu kare bir duvarsa ve Darth Vader buraya gitmek zorundaysa, duvarı yık
                    if grid[ny][nx] == 0:
                        queue.append((nx, ny, path + [(nx, ny)]))  # Önce duvarı yıkıp devam et
                    if grid[ny][nx] == 1:
                        queue.append((nx, ny, path + [(nx, ny)]))  # Normal şekilde devam et

        return []


class KyloRen(Character):
    pass

class Stormtrooper(Character):
    pass