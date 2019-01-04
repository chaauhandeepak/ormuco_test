from cache import Cache
import random

if __name__ == '__main__':

    # Test the cache
    Keys = [i for i in range(7)]     # Entries
    sites = ['entry 1 ','entry 2 ','entry 3 ','entry 4 ' ]

    # Cache object using fucntion cache
    cache = Cache()

    print('_'*40)
    # Updating Cache with entries
    for i, key in enumerate(Keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(sites)])
            print('\t', value)
            cache.update(key, value)

        print("{0}.Iteration, #{1} cached entries" .format(i+1, cache.size()))

    # Cache List
    print('\n\n\t', '*'*10, ' CACHE LIST ', '*'*10)
    for k, v in cache.view().items():
        print("{0} : {1}".format(k, v))
    print('_' * 60)
