def has_negatives(a):
    result = []
    cache = {}
    # for i in a:
    #     if abs(i) not in cache.values():
    #         cache.update({i: abs(i)})
    #     else:
    #         result.append(abs(i))
    # for i in a:
    #     cache.update({abs(i): i})
    # for i in a:
    #     if i in cache.keys():
    #         result.append(abs(i))
    for i in a:
        if abs(i) not in cache.keys():
            cache.update({abs(i): i})
        else:
            result.append(abs(i))

    # for i in a:
    #     if abs(i) in cache.keys():
    #         print('dup found', abs(i))
    #         result.append(abs(i))
    #     else:
    #         cache.update({i: abs(i)})
    # print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
