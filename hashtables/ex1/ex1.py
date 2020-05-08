def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    if length > 1:
        for i in range(length):
            l_w = limit - weights[i]
            new_tup = {l_w: weights[i]}
            cache.update(new_tup)
            #check keys for current value, if exists, answer found
            if weights[i] in cache.keys():
                first = cache[weights[i]]
                second = weights[i]
                # print(f'{limit} - {first} = {second}')
                # print(f'match {first} found at: {weights.index(first)}')
                # print(f'match {second} found at: {weights.index(second)}')
                answer = [weights.index(first), weights.index(second)]
                if answer[0] == answer[1]: #if indexes are the same, find second index
                    new_arr = weights[weights.index(second)+1:]
                    # print ('new array', new_arr)
                    answer[1] = (new_arr.index(second)+ 1)
                answer.sort(reverse = True)
                return answer
    # print(cache, limit)
    return None

# def xget_indices_of_item_weights(weights, length, limit):
#     for w in weights:
#         for x in weights:
#             if w + x == limit:
#                 arr = [weights.index(w), weights.index(x)]
#                 print(w, x, '=', limit)
#                 arr.sort(reverse = True)
#                 print(arr)
#                 return arr
#     print('None')
#     return None

    # a b c d e f g h i j
    # 0 1 2 3 4 5 6 7 9 10
    #     ^ 0 1 2 3 4 5 6
    #       1 2 3 4 5 6 7 (index+1)