import datetime


class Cache:

    def __init__(self):
        # Constructor
        self.cache = {}
        self.MaxSize = 5

    def empty(self):
        # checking, whether cache is Empty
        return self.cache == {}

    def size(self):
        # Returns total size of cache
        return len(self.cache)

    def __contains__(self, key):
        # Returns Boolean value, whether key is in the cache
        return key in self.cache

    def view(self):
        # Returns cache dictionary
        return self.cache

    def update(self, key, value):
        # Update cache and remove oldest item, when size reaches maximum
        if key not in self.cache and len(self.cache) >= self.MaxSize:
            self.delete()

        self.cache[key] = {'Addition time': datetime.datetime.now().isoformat(),
                           'entry value': value}

    def delete(self):
        # Remove oldest item from cache
        old = None
        for key in self.cache:
            if old is None:
                old = key
            elif self.cache[key]['Addition time'] < self.cache[old]['Addition time']:
                old = key
        self.cache.pop(old)
