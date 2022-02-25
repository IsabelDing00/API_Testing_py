# Separate numbers and letters in a string
# “abc123d” → [[‘a’,’b’,’c’,’d’],[1,2,3]]

example = 'sfafjkae'

def sep(s):
    result = []
    num = []
    let = []
    if len(s) == 0:
        return result

    for i in range(len(s)):
        if s[i].isdigit():
            num.append(s[i])
        else:
            let.append(s[i])

    result.append(num)
    result.append(let)
    return result

# e = sep(example)
# print(e)

#
# // Given a sorted array and K, return the number of pairs that elements in the array added up to K.
# // The array values are distinct. If there’s no paris, return -1
# // [1,2,4,5,7,8], K=9 → 3
test2 = [2,4,6,7,8,10,12]
k = 10

def findPairs(nums, k):
    l, r = 0, len(nums)-1
    pair = 0
    if len(nums) < 2:
        return -1

    while l < r:
        diff = k - nums[l]
        if diff > nums[r]:
            l += 1
        elif diff == nums[r]:
            pair += 1
            l += 1
            r -= 1
        else:
            r -= 1
    if pair == 0:
        return -1
    return pair

res = findPairs(test2, k)
print(res)






