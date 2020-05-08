# from hashtable import HashTable

def finder(files, queries):
    result = []
    cache = {}
    cache2 = {}
    for f in files:
        fsplit = f.split("/")
        fname = fsplit[-1]
        # print(fname)
        if fname not in cache.keys():
            cache.update({fname: f})
        elif fname in cache.keys():    
            # print('duplicate', f)
            cache2.update({fname: f})
        # if fname == "file256":
        #     print('wtf', f)
        # htable.put(fname, f)
    for query in queries:
        # rvalue = htable.get(query)
        # if rvalue:
        #     print(rvalue)
        if query in cache.keys():
            # print('found', cache[query])
            result.append(cache[query])
            if query in cache2.keys():
                # print('found', cache2[query])
                result.append(cache2[query])
    # print(result, len(cache))
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
