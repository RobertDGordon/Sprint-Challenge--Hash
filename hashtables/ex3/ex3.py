def intersection(arrays):
    result = []
    allrays = []
    cache = {}
    for n in arrays[0]:
        cache.update({n: n})
    for arr in arrays[1:]:
        for n in arr:
            if n in cache:
                # print('intersection found', n)
                if n not in result:
                    result.append(n)
    # for i in range(len(arrays)):
    #     # print (i)
    #     allrays.extend(arrays[i])
    # for n in allrays:
    #     if n in cache.keys():
    #         # print('intersection found', n)
    #         if n not in result:
    #             result.append(n)
    #     else:
    #         cache.update({n: 0})
    # for arr in arrays:
    #     # print(len(arr))
    #     for n in arr:
    #         if n in cache.keys():
    #             # print('intersection found', cache[n])
    #             if n not in result:
    #                 result.append(n)
    #             # print(result)
    #         else:
    #             cache.update({n: n})
    #             # print(cache)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
