from collections import deque as cdeque


class LRUCache:

    def __init__(self, limit=10):
        self.limit = limit
        self.deque = cdeque(maxlen=limit)

    def set(self, key, value):
        if self.limit == 0:
            return 0
        keys_list = [key for key, value in self.deque]
        if key not in keys_list:
            self.deque.append((key, value))
            return True
        index = keys_list.index(key)
        old_key_and_val = self.deque[index]
        self.deque.remove(old_key_and_val)
        self.deque.append((key, value))
        return False

    def get(self, key):
        keys_list = [key for key, value in self.deque]
        try:
            index = keys_list.index(key)
            key_and_val = self.deque[index]
            self.deque.remove(key_and_val)
            self.deque.append(key_and_val)
            return key_and_val[1]
        except ValueError:
            return None

    def __len__(self):
        return len(self.deque)

    def __getitem__(self, index):
        return self.deque[index][1]
