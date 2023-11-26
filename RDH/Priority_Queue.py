def sort_pq(pq):
    n = len(pq)
    for i in range(0, n-1):
        for j in range(i, n):
            if pq[i][0] <= pq[j][0]:
                pq[i], pq[j] = pq[j], pq[i]  #swap

    return pq            


class Priority_queue:
    def __init__(self):
        self.pq = []
    
    def add(self, k, v):
        self.item = [k, v]
        # self.pq.append(self.item)
        # self.pq = sort_pq(self.pq)
        for i in range(len(self.pq)):
            if isinstance(self.pq[i][0], (int, float)):
                if k > self.pq[i][0]:
                    self.pq.insert(i, self.item)
                    return self.pq
        self.pq.append(self.item)
        return self.pq

    def first_item(self):
        return self.pq[0]
    
    def remove_first(self):
        return self.pq.pop(0)
    
    def remove_at(self, pos):
        pos -= 1
        return self.pq.pop(pos)
    
    def update_element(self, old_pos, new_pos):
        key, value = self.pq.pop(old_pos-1)
        self.the_item = [str(key), value]
        self.pq.insert(new_pos-1, self.the_item)
    
    def is_empty(self):
        return len(self.pq) == 0
    
    def get_length(self):
        return len(self.pq)
    
    def get_pq(self):
        return self.pq