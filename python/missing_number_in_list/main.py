

def solution(nums):
    s = set()
    for i in range (0, len(nums) + 1):
        s.add(i)

    for n in nums:
        s.remove(n)

    return s.pop()


nums = [3, 1, 0]
nums2 = [3, 1, 0, 12, 7, 4, 5, 9, 10, 11, 6, 2]

print(solution(nums))
print(solution(nums2))



