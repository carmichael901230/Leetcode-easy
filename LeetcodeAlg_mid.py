from typing import *
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class GraphNode:
    def __init__(self, val: int = 0, neighbors: 'List[Node]' = None) -> None:
        self.val = val
        self.neighbors = neighbors
        
# 1.2 Add Two Numbers ============================================================ https://leetcode.com/problems/add-two-numbers/
# Problem: Given two non-empty linked list [l1], [l2]. Two linked lists represent two non-negative integers, where each digit is 
#          stored as node in reverse order. Sum up both linked list and return the sum as a linked list.
#          Ex 342+456 = 807
#             [2] -> [4] -> [3] == [7] -> [0] -> [8]
#             [6] -> [5] -> [4] 
# Description: Create a dummy node to store the sum. Iterate throught [l1] and [l2], keep tracking current node of [l1] and [l2]
#              and [carry]. If [l1], [l2] or carry are not zero or not None, means result has more digit, then create a now node
#              one result linked list to store the sum of [l1], [l2] and carry. The value of new node is [sum]%10, and value of 
#              carry is [sum]//10
# Time complexity: O(n)
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    head = cur = ListNode()
    while l1 or l2 or carry:
        cur.next = ListNode()
        if l1:
            cur.next.val += l1.val
            l1 = l1.next
        if l2:
            cur.next.val += l2.val
            l2 = l2.next
        cur.next.val += carry
        carry = cur.next.val//10
        cur.next.val %= 10
        cur = cur.next
    return head.next

# 2.3 Longest Substring Without Repeating Characters ======================= https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Problem: Given a string [s], find the length of "longest substring" without repeating character
#          Ex: "abcadcbb" => "bcad" length = 4
# Description: Maintain dictionary [track], that tracks latest index of each character. [start] tracks the beginning of the current substring.
#              [max_length] tracks the result length. 
#              Iterate through character in [s]. If a character is not in [track], record the character and its index, and update [max_length]
#              with current length "i-start+1". If a character is already in [track] and [start] comes before the last occurance of the character,  
#              means current substring has duplicates. Set [start] to the next index of the duplicate to start a new substring. For every character
#              record index of latest occurrence
# Time complexity: O(N)
def lengthOfLongestSubstring(s: str) -> int:
    track = {}
    max_length = start = 0          # [start] represent the starting index of current substring
    for i, c in enumerate(s):
        # duplicate detected in current substring
        if c in track and start <= track[c]:                
            start = track[c] + 1                   # start a new substring right after last occurence of [c]
        # no duplicate so far
        else:                                                         
            max_length = max(max_length, i - start + 1)     # calculate current length and update [max_length]
        track[c] = i                  # record latest occurrence of each character   
    return max_length

# 3.5 Longest Palindromic Substring ===================================== https://leetcode.com/problems/longest-palindromic-substring/
# Problem: Given a string [s], return the longest substring that is a palindrome
# Description: Iterate through every character in [s] with index [i]. Use [i] as middle of palindrome substring, and expand on both sides of [i], 
#              if character on both side of [i] are same, then expand more. Stop expanding and return the palindrome when character on both sides
#              are differernt or hit end of [s]. Maintain [res] as longest palindrome substring, and compare with returned substring.
# Time compleixty: O(n^2)
def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # substring starts with single character, and check odd length substrings
        temp = longestPalindrome_help(s, i, i)
        res = temp if len(temp)>len(res) else res
        # substring starts with two characters, and check even length substrings
        temp = longestPalindrome_help(s, i, i+1)
        res = temp if len(temp)>len(res) else res
    return res

def longestPalindrome_help(s, l, r):
    while l>=0 and r<len(s) and s[l] == s[r]:   
        i, j = l-1, r+1     # expand substring on both sides
    return s[i+1: j]            # return the last valid palindrome

# 4.6 ZigZag Conversion ====================================================== https://leetcode.com/problems/zigzag-conversion/
# Problem: Given a string [s], and an integer [numRows]. Display the [s] in ZigZag pattern with [numRows] rows. Return the a 
#          string that extract the pattern row by row. 
#          Example: "PAYPALISHIRING" numRows=4, returns "PINALSIGYAHRPI"
#                   P       I       N
#                   A     L S    I  G
#                   Y  A    H  R
#                   P       I
# Description: Maintain a string list [res] of size [numRows], each element in [res] represents a row in zigzag pattern. Track
#              [index] and [step], that correspondingly represent the index of [res] and the direction that [index] moves in [res].  
#              If [index] hit first row or last row of pattern(index == 0 or index == numRows-1), change direction by negate 
#              [step]
# Time complexity: O(n)
# Space complexity: O(n)
def convert(s: str, numRows: int) -> str:
    res = [""]*numRows          # create list, each element represent a row in pattern
    index, step = 0, 1
    for c in s:
        res[index] += c
        index = (index+step)%numRows        # move to next [index]
        if index == 0 or index == numRows-1:
            step *= -1                      # negate step, if [index] hit top/bottom boundary
    return "".join(res)

# 5.8 String to Integer ======================================================= https://leetcode.com/problems/string-to-integer-atoi/
# Problem: Given a string [s], convert it to a 32-bit signed integer. The leading and tailling space should be ignored, the string 
#          may have sign '-' or '+' at beginning, any alphabets and special characters that doesn't form valid integer will end the
#          convertion and the rest of string is ignored. If the result is between [-2**31, 2**31-1], return result. If result is less
#          than -2**31, return -2**31. If result is larger than 2**31-1, return 2**31-1.
# Description: Strip the leading and tailing spaces from [s]. Maintain a [res] to store converted integer number, and [sign] to store
#              negative or positive sign. Iterate through characters in [s]. If a char is number "isnumeric()", add it to [res]. If a 
#              char is not number, and it is '-' or '+' at index 0, then change [sign] accordingly. If the char is not at index 0, 
#              then stop iteration. Compare [res] with "-2**31" and "2**31-1" and return accordingly
def myAtoi(self, s: str) -> int:
    if len(s)<=0:
        return 0
    s = s.strip()           # strip leading and tailing spaces
    res, sign = 0, 1
    for i in range(len(s)):
        if s[i].isnumeric():
            res *= 10
            res += ord(s[i]) - 48
        else:
            if i==0:
                if s[i] == '-': 
                    sign = -1
                elif s[i] == '+': 
                    sign = 1   
                else:
                    break
            else:
                break
    res = int(res)*sign         # get converted integer
    if res > 2**31-1:           # compare with 32-bit integer boundary
        return 2**31-1
    elif res < -2**31:
        return -2**31
    else:
        return res

# 6.11 Container with most water ================================================ https://leetcode.com/problems/container-with-most-water/
# Problem: Given a list [height] with non-negative integers. Each integer represent a thin wall with given height. Find two walls that if 
#          a horizontal line forms a container, such that the container contains the most water
#          Ex: [1,8,6,2,5,4,8,3,7], draw the horizontal line between index 1 and index 8, with height = 7. Maximum amount = 7*7 = 49
# Description: Maintain two pointers [left] and [right], start from both end of the list. Compare height of height[left] and heifht[right],
#              move the smaller point towards middle. Maintain the maximum size of container [res]. Calculat the size of container, where
#              size = min(left, right) * (right-left). Update [res] according to calculated size
# Time complexity: O(N), N=len(height)
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height)-1
    res = min(height[left], height[right])*right
    while left<right:
        if height[left]<height[right]:
            left += 1
        else:
            right -= 1
        res = max(res, min(height[left], height[right])*(right-left))
    return res

# 7.12 Integer to Roman ======================================================== https://leetcode.com/problems/integer-to-roman/
# Problem: Given an integer convert it to a string of Roman number. The char of convertion is below
#          I:1 V:5 X:10 L:50 C:100 D:500 M:1000
#          Note, If a smaller symbol comes before a larger, means subtraction. IV:4 IX:9 XL:40 XC:90 CD:500 CM:900
# Description: Maintain a "reversed" roman string [res] as result, maintain two lists contain Roman number of [ones](I, X, C, M) and 
#              number of [fives](V, L, D). Track index [i] of [ones], where start from "I". Retrieve numbers from lowest digit by %10. 
#              every mod by 10 remove one digit from [num] thus increase [i] by 1. The module is denoted as [cnt]
#              If [cnt] is less than 4, add "ones[i]"*[cnt] to [res]. 
#              If [cnt] is equals to 4, add "ones[i]" and "fives[i]" to construct 4.
#              If [cnt] greater than 4 and less than 9, add a "fives[i]" and "ones[i]" * (cnt-5)
#              If [cnt] is equals to 9, add "ones[i]" and "ones[i+1]" to construct 5
#              Each iteration, [num] is decreased by 10 times, and [i] is increased by 1, At the end, reverse [res] and return
# Time complexity: O(lg(n))
def intToRoman(num: int) -> str:
    ones = ["I", "X", "C", "M"]
    fives = ["V", "L", "D"]
    res, i = [], 0
    while num > 0:
        cnt = num%10
        if cnt < 4:
            res.append(cnt*ones[i])
        elif cnt == 4:
            res.append(ones[i]+fives[i])
        elif 4<cnt<9:
            res.append(fives[i]+ones[i]*(cnt-5))
        else:
            res.append(ones[i]+ones[i+1])
        i+=1
        num//=10
    return "".join(res[::-1])

# 8.15 3SUM ====================================================================== https://leetcode.com/problems/3sum/
# Problem: Given an array of integers [nums], Find three unique elements in the array such that their sum is Zero. For each 
#          combination an element can be used no more than once. Return all unique triplets in the array that sum up to zero. 
#          The result can NOT contain dulicate triplets
# Description: Sort array, iterate every element in sorted array. In each iteration nums[i], need to find two elements that 
#              sum up to "-nums[i]" denote as [target]. In order to find such two number, use two pointers [left] and [right] 
#              that [left] starts from [i+1], [right] starts from right-end of array. Since the array is sorted, move [left] 
#              to right if their sum is smaller than [target]. If sum is larger than [target], then move [right] to left.
#              If sum equals to [target], means a combination is found, three numbers are [i], [left] and [right]. Add the
#              triplet to [res] list.
#              This manner can avoid using same element multiple times, but can't avoid using duplicate elements in the list.
#              Thus, we need to skip duplicate elements for [i], [left] and [right]. If [i] == [i-1], skip [i]. If [left] ==
#              [left-1], skip [left]. If [right] == [right+1], skip [right]
# Time complexity: O(n^2)
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    length = len(nums)
    for i in range(length-2):
        if i>0 and nums[i]==nums[i-1]:          # skip duplicates on [i]
            continue
        left, right = i+1, length-1
        target = -nums[i]
        while left < right:                     # find [left] and [right] that sum up to target
            s = nums[left] + nums[right]
            if s<target:
                left+=1
            elif s>target:
                right-=1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left<right and nums[left] == nums[left+1]:        # skip duplicates on [left]
                    left+=1
                while left<right and nums[right-1] == nums[right]:      # skip duplicates on [right]
                    right-=1
                left+=1
                right-=1
    return res

# 9.16 3Sum Closest ================================================================= https://leetcode.com/problems/3sum-closest/
# Problem: Given a list of integers [nums], and a integer number [target]. Find three number is [nums] that their sum is closest
#          to [target]. Return the sum of the three numbers.
# Description: Use similar strategy as "3Sum". Sort [nums] and iterate through it, For each iteration with index [i], maintain 
#              two pointers [j] and [k], that start from [i+1] and [length-1] respectely. Sum up [i], [j], [k] and compare with
#              [target]. If [sum]<[target], move [j] to right to increase [sum]. If [sum]>[target], move [k] to left to decrease
#              [sum]. If [sum]=[target], then return [sum] since it is the closest. For each combination of [i], [j], [k], track
#              the smallest difference between [target] and [sum], and maintain [sum]
# Time complexity: O(n^2)
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    res, diff = sum(nums[0:3]), float("inf")
    length = len(nums)
    for i in range(len(nums)):
        j, k = i+1, length-1
        while j<k:
            s = nums[i] + nums[j] + nums[k]
            if s<target:
                j+=1
            elif s>target:
                k-=1
            else:
                return target
            if abs(s-target)<diff:
                res = s
                diff = abs(target-s)
    return res
        
# 10.17 Letter Combinations of a Phone Number ====================== https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Problem: Consider a cell phone keyboard, numbers from 2 to 9 have alphabets binded to them, where 2="abc", 3="def", 4="ghi", 5="jkl",
#          6="mno", 7="pqrs", 8="tuv", 9="wxyz". Given a string with [digits] from 2 to 9, construct a list contains all possible 
#          combinations that [digits] can represent
#          Ex: "23", 2="abc" 3="def" ===> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Description: Use DFS backtrack. Create a [letters] list which convert number to its corresponding alphabets, create a list [res]
#              as result list. The recursive method takes [digits], [letters], [path], and [res] as parameter, where [path] maintains 
#              the characters in a single path down the DFS tree. Each recursive call take the first number in [digits], and iterate 
#              through characters in its corresponding alphabets. Each iteration calls the recursive method to construct back-track
#              pass result of [digits] as parameter, and append current charater to [path]. When no more number left in [digits], append
#              [path] to [res]
# Time complexity: O(4^n), n=len(digits). Each number in [digits] will trigger 3 or 4 recursive calls depending on number of alphabets 
# Space complexity: O(4^n)                associated with them. Thus 4^n
def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]         # a number-letter conversion, 0 and 1 are not used
    res = []
    letterCombinations_helper(digits, letters, "", res)
    return res

def letterCombinations_helper(digits, letters, path, res):
    if not digits:                      # no more digits left, a full path is constructed
        res.append(path)
    else:
        for c in letters[int(digits[0])]:   
            letterCombinations_helper(digits[1:], letters, path+c, res)     # each recursive call take a character and add to path

# 11.18 4Sum ========================================================================================= https://leetcode.com/problems/4sum/
# Problem: Given an integer aray [nums], and an integer [target]. Find four numbers in [nums], such that their sum equals to [target]. 
#          Find all unique quadruplets and return as 2D array, where each quadruplet is a sub-array
# Description: Recursively reduce "4sum" to "3sum" and furture reduce to "2sum". Use back-track recursion apply DFS, maintain a list [temp] 
#              that store numbers on DFS path, track [target] of current level and [N] representing how many numbers need to pick. 
#              For each recursive call, add first number in [nums] to [temp] to construct DFS tree. Subtract nums[0] from [target], since
#              nums[0] is picked and new [target] shoud exclud it. Reduce [N] by 1 since nums[0] is picked. Pass rest of list nums[1:] to next 
#              recursion.
#              When N=2 invoke "2sum", maintain 2 pointers [left] and [right], which start at beginning and end of list. Keep moving [left]
#              and [right] to middle and compare their sum with [target](target here is reduced). When their sum equals to [target], add
#              nums[left] and nums[right] along with [temp] into result list [res].
# Time complexity: O(n^3)
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    def NSum(nums, target, N, temp, res):
        # Early ternimation improve performance
        #   when there's no enough elements in list
        #   when the elements in list are too small or too large to reach target
        if len(nums) < 2 or target < nums[0]*N or target > nums[-1]*N:  
            return
        # Perform twoSums
        if N == 2:
            left, right = 0, len(nums)-1
            while left<right:
                s = nums[left]+nums[right]
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    res.append(temp+[nums[left], nums[right]])
                    while left<right and nums[left] == nums[left-1]:        # skip duplicates on [left]
                        left += 1
                    while left<right and nums[right-1] == nums[right]:      # skip duplicates on [right]
                        right -= 1
                    left += 1
                    right -= 1
        # reduce N
        else:
            for i in range(len(nums)-N+1):
                if i==0 or nums[i-1] != nums[i]:            # skip duplicates on [i], but invoke at least once 
                    NSum(nums[i+1:], target-nums[i], N-1, temp+[nums[i]], res)
    res = []
    NSum(sorted(nums), target, 4, [], res)
    return res

# Description: Create a dictionary [record], Iterate [nums] with pointer [i] and [j], maintain pairs of numbers from and their sum.
#              Specificall, the "value" is collection of pairs of number index (multiple pairs might sum up tp same number),
#              the "key" is how much more do numbers needed to reach [target]. Iterate [nums] again with pointer [i] and [j],
#              search for their sum [s] = nums[i]+nums[j]. That pairs in [record] can be paired with nums[i] and nums[j] to sum
#              up to [target]. There can have multiple pairs in "record[key]", iterate though "record[key]" and construct a 
#              result by appending nums[i] and nums[j] after existing pairs. Ensure [i] and [j] comes after exsting pairs, to 
#              eliminate duplicates. Add each result to [res] set, and convert it to list before returning
# Time Compleixty: O(n^2)
import collections
def fourSum_2(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    # eliminate corner cases
    if len(nums) < 4 or 4*nums[0] > target or 4*nums[-1] < target: return []    
    # create dictionary where "value" is set() of tuples (index_1, index_2), "key" is target-nums[i]-nums[j]
    record = collections.defaultdict(set)           
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)):
            need = target-nums[i]-nums[j]
            record[need].add((i,j))

    res = set()
    # iterate [nums] again, find other two numbers that can sum up to "key" of dictionary
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            s = nums[i]+nums[j]
            if s in record:                 # find other two numbers can pair with the two numbers in dictionaray
                for pair in record[s]:          # there are multiple pairs in record[s]
                    if pair[1]<i:                       # new pair should comes after existing pairs 
                        res.add((nums[pair[0]], nums[pair[1]], nums[i], nums[j]))
    return [list(e) for e in res]                       # convert set() to list() before returning

# 12.19 Remove Nth Node From End of List ========================================== https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Problem: Given the head of a linked list [head], and an integer [n]. Remove [n]th node from end of list, and return the head.
#          Ex 1 -> 2 -> 3 -> 4 -> 5, n=2  ====> remove second last element "4", 1 -> 2 -> 3 -> 5
# Descrption: Use two pointers [fast] and [slow], where [slow] start from head, [fast] start [n] nodes after head. Both node traverse at same pace,
#             when [fast] hit the end, [slow] points to the node need to be removed. Insert a dummy header before [head], and return [dummy.next]
#             eventually. Traverse [fast] and [slow], when [fast.next] is None, then [slow] is pointing to the node before the node need to be 
#             removed. Assign [slow.next] to [slow.next.next] to remove the node
# Time complexity: O(n)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

# 13.22 Generate Parentheses =========================================================== https://leetcode.com/problems/generate-parentheses/
# Problem: Generate [n] pairs of parentheses, return all valid combinantions of well-formed parentheses.
# Description: Maintain a string [temp] representing a valid parentheses with [n] pairs. During the construction of [temp], maintain [open]
#              and [close] represent number of opening and closing parentheses in [temp]. Keep constructing [temp] by adding opening or 
#              closing parentheses to [temp], and increase count of [open] and [close] accordingly. [close] can exceed [open] otherwise 
#              the combination is not valid. When [open]==[close]==[n], means a completed and valid combination is formed, append [temp] 
#              to result list. 
# Time complexity: O((2n choose n)/(n+1)) aka Catalan number
def generateParenthesis(n: int) -> List[str]:
    def generateParenthesis_helper(open, close, temp, res):
        if open == close == n:                  # completed well-formed parentheses, add it to [res]
            res.append(temp)
            return
        if close > open:                # more closing than opening, it is invalid and terminate this path
            return
        if open < n:
            generateParenthesis_helper(open+1, close, temp+"(", res)        # add an opening parenthesis
        if close < n:
            generateParenthesis_helper(open, close+1, temp+")", res)        # add a closing parenthesis
    res = []
    generateParenthesis_helper(0, 0, "", res)       # initially zero opening and closing parentheses 
    return res

# 14.24 Swap Nodes in Pairs =============================================================== https://leetcode.com/problems/swap-nodes-in-pairs/
# Problem: Given the [head] of a linked list, sap position of every adjacent nodes and return the head
#          Ex: 1->2->3->4->5  ====>   2->1->4->3->5
# Description: Maintain three pointers [first], [second], and [third], where [second] and [third] are being swapped, and [first] is the anchor
#              to link [second] and [third] back to list after swapping. After each swap, move [first] two position forward, and reassign both
#              [second] and [third], until remaining list has less than 2 nodes. Consider the size of given linked list is smaller than 2, 
#              no swap is  neede, return [head] directly
# Time complexity: O(n)
def swapPairs(head: ListNode) -> ListNode:  
    if not head or not head.next:               # less than 2 nodes in list
        return head
    dummy = first = ListNode(0, head)
    while first.next and first.next.next:       # swap until remaining nodes is less than 2
        second = first.next
        third = second.next
        second.next = third.next
        first.next = third
        third.next = second
        first = first.next.next
    return dummy.next

# 15.29 Divide Two Integers ================================================================= https://leetcode.com/problems/divide-two-integers/
# Problem: Given two integers [dividend] and [divisor], divide two integers without using multiplication, division or mod operations. Return the
#          quotient after dividing [dividend] by [divisor], truncate fraction/decimal part if any. If result is out of bound of 32-bit integer,
#          return the value of bound -2^31 or 2^31-1
# Description: Check the sign of quotient, by comapring signs of [dividend] and [divisor]. If they have same sign, then quotient is positive, 
#              otherwise quotient is negative. Use "abs()"" to make [dividend] and [divisor] positive, then subtract [divisor] from [dividend] 
#              in a loop, until [dividend] is less than [divisor], and count how many [divisor] are subtracted with [cnt]. Meanwhile, double
#              [divisor] by "divisor<<=1" to reduce number of iterations. Also, since [divisor] is douled, [cnt] shoule be doubled every 
#              iteration by "cnt<<=1", because double amount of [divisor] is subtracted. At the end of loop, add "sign" to [res], and compare
#              [res] with boundary then return 
# Time complexity: O(log(dividend, divisor)^2), outter and innter loop both O(log(dividend, divisor))
def divide(dividend: int, divisor: int) -> int:
    positive = (dividend < 0) == (divisor < 0)          # extract sign of result
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:              # outter loop keep subtracting [divisor] until [dividend] is smaller than [divisor]
        temp, cnt = divisor, 1                  # rest current divisor, and cnt
        while dividend >= temp:                 # inner loop that double [divisor] every iteration
            dividend -= temp
            res += cnt
            cnt <<= 1
            temp <<= 1          
    if not positive:                        # assign "sign" to result
        res = 0-res
    return min(max(-2147483648, res), 2147483647)       # compare with 32-bit boundary

# 16.31 Next Permutation ====================================================================== https://leetcode.com/problems/next-permutation/
# Problem: Given a list of integers [nums], rearrange order of integers the generate next greater permutation, aka a number that contains exact 
#          digits, new number is greater than [nums] and no other possible permutation is smaller than new number and larger than [nums]. 
#          Rearrange [nums] in-place
# Description: The next permutation is slightly larger. Find the last ascending between adjacent digits, swap the ascending number with a 
#              number that is slightly larger than it can make the number larger. Reverse the descending part which comes after the swapped 
#              number, this will make that part become the smallest permutation. Since the higher digit is larger than before, and the rest 
#              digits are the smallest possible, the new number is the next permutation
#              Maintain a pointer [i] starts from end of list, iterate towards front and find the last ascending position that "[i-1]<[i]".
#              Maintain another pointer [j] starts from end of list, iterate towards front and find the digit that is slightly larger than
#              [i-1]. Swap [i-1] and [j], and reverse all digits after [i-1].
# Time complexity: O(n), n=len(nums)
def nextPermutation(nums: List[int]) -> None:
    i = j = len(nums)-1
    while i>0 and nums[i-1]>=nums[i]:
        i -= 1
    if i==0:                # [nums] is the last permutation, reverse all digits
        nums.reverse()
        return
    while nums[i-1]>=nums[j]:       # find the digit slightly larger than [i-1]
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]     # swap 
    nums[i:] = reversed(nums[i:])             # reverse digits after [i-1]

# 17.33 Search in Rotated Sorted Array ========================================= https://leetcode.com/problems/search-in-rotated-sorted-array/
# Problem: Given an integer array [nums], which sorted in ascending order. However, the elements are shifted/rotated by "k" time, value of "k"
#          is unknown. Ex [1,2,3,4,5,6,7] is rotated by 4 and become [4,5,6,7,1,2,3]. Given the integer array [nums] and an integer [target],
#          find and return the index of [target] in [nums], if [target] is not presented return -1
# Description: Use binary search. Maintain [l] and [r] as two ends of list, [m] as middle index of list. 
#              If [mid] == target, [target] is found and return [mid].
#              If [l] <= [mid], means sublist from [l] to [mid] are sorted in ascending order. 
#                   If [target] is located between [l] and [mid], just need to apply regular binary search to find [target]
#                   Else, [target] is located between [mid] and [r], reassign 'l=mid+1" to look for sorted sublist
#              Else, sublist between [mid] and [r] are sorted in ascending order.
#                   If [target] is located between [mid] and [r], apply regular binary search to find [target]
#                   Else. [target] is located between [l] and [mid], reassgin "r=mid-1" to look for sorted sublist
# Time complexity: O(logN), N=len(nums)
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:                 # target is found
            return mid  
        elif nums[l] <= nums[mid]:              # left half is sorted
            if nums[l] <= target <= nums[mid]:      # target is in the sorted half
                r = mid-1
            else:                                   #  target is not in the sorted half
                l = mid+1
        else:                                   # right half is sorted
            if nums[mid] <= target <= nums[r]:      # target is in the sorted half
                l = mid+1
            else:                                   # target is not in the sorted half
                r = mid-1
    return -1

# 18.34 Find First and Last Position of Element in Sorted Array ==== https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Problem: Given a sorted integer list [nums], Given a integer [target]. Find the starting and ending index of [target] in [nums]. 
#          Return starting and ending indices as list [s, e]. If [target] is not presented return [-1, -1]
# Description: Implement "bisect_left" and "bisect_right" to find insert index of target. After find insertion index [l] and [r], 
#              reduce [r] by 1 since we need to find the last index of [target] instead of insertion index. Validate [l] and [r]
#              that they should not be out of bound. Elements of index [l] and [r] should both equal to [target]. If any validation
#              is false, should return [-1, -1].
def searchRange(nums: List[int], target: int) -> List[int]:
    l = insertLeft(nums, target)
    r = insertRight(nums, target)-1             # minus 1 to get last index of [target]
    if 0<=l<len(nums) and 0<=r<len(nums) and nums[l] == nums[r] == target:      # validate [l] and [r]
        return [l,r]
    else:
        return [-1, -1]

def insertLeft(a, x):       # bisect_left
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def insertRight(a, x):      # bisect_right
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

# 19.36 Valid Sudoku ================================================================================= https://leetcode.com/problems/valid-sudoku/
# Problem: Given a 9*9 list representing a sudoku board. Some cells are filled with number strings, some cells are dots "." as they are not filled.
#          Validate the given sudoku [board] return True or False with following rules
#          1. each row must contain digits 1-9 without duplicates
#          2. each column must contain digits 1-9 without duplicates
#          3. each 3*3 sub-box must contain 1-9 without duplicates
# Description: Maintain a set [record] to record occurrence of each cell, where "(2)1" means "2" appears at column 1, "1(2)" means "2" appears at
#              row 1, "0(2)2" means top-right square contains "2". Iterate though each cell of [board] and each cell will add 3 records to [record].
#              If any cell adds less than 3 records, means there are duplicates then return False. 
# Time complexity: O(n), n=81
def isValidSudoku(board: List[List[str]]) -> bool:
    record = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":                  # only check filled cells and skip empty cells
                prevSize = len(record)
                row = str(i)+"("+board[i][j]+")"                    # row record
                col = "("+board[i][j]+")"+str(j)                    # col record
                square = str(i//3)+"("+board[i][j]+")"+str(j//3)    # square record
                record.add(row)
                record.add(col)
                record.add(square)
                if len(record)-prevSize != 3:           # must add 3 records otherwise there are duplicates
                    return False
    return True

# 20.39 Combination Sum =========================================================================== https://leetcode.com/problems/combination-sum/
# Problem: Given a list of "unique" integers [candidates] and a integer [target]. Pick numbers from [candidates] to sum up to [target]. A number in
#          [candidates] can be used as many times. Return all unique combinations of numbers from [candidates] that sum up to [target].
# Description: Dynamic programming, Create a lsit [dp] that index [t] store combinations that sum up to [t]. In order to find combination that
#              sum up to [t+c], just need to grab all combination of dp[t] and append [c] after them.
#              Sort [candidates] in ascending order. Iterate though [t] from 1 to target+1, find combination that sum up to [t], and store them 
#              in dp[t]. For each [t], iterate though [candidates]. For each [c] of [candidates], if [c]>[t], means the rest of [candidates] 
#              all greater than [t], not need to continue. If [c]==[t], means [c] itself sum up to [t], append [c] into dp[t]. Else, find complement
#              of [c] which is dp[t-c], append [c] after combinations in dp[t-c] and store at dp[t].
#              The combination that sum up to [t] are stored in the last element of [dp], return dp[-1] at the end
# Time complexity: O(target^2*n), n=len(candidates) OR O(nlogn), if len(candidate) is very large
# Space complexity: O(target*3), len(dp) == len(dp[i]) == len(dp[i][i]) == target
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    dp = [[] for _ in range(target+1)]
    for t in range(1, target+1):                #dp[t] saves all combinations have t sum
        for c in candidates:
            if c > t: break                         #from now on, all sum > t, break out
            if c == t: dp[t].append([c]); break         #the element value equals to current target t
            # to ensure no duplicate, the later coming item should be strictly greater than previous ones, make the result a asc sequence. 
            for path in dp[t-c]:
                if c>=path[-1]:
                    dp[t].append(path+[c])
    return dp[-1]

# Description: Create a list [dp], where each index [i] is a list of combinations that sum up to [i]. Iterate though each [candidate], find 
#              all possible sums that can be achieved by adding other candidates to [candidate], and record the combination in dp[i]. By  
#              iterate though from [candidate] to [target], we can find the combination that has [candidate] involved.
def combinationSum_2(candidates: List[int], target: int) -> List[List[int]]:
    dp = [[[]] for _ in range(target+1)]
    for candidate in candidates:
        for i in range(candidate, target + 1):
                if i-candidate == 0:
                    dp[i].append([candidate])
                else:
                    for sublist in dp[i-candidate]:
                        if sublist:
                            dp[i].append(sublist+[candidate])
    return [comb for comb in dp[target] if comb]

# 21.40 Combination Sum II ==================================================================== https://leetcode.com/problems/combination-sum-ii/
# Problem: Given a list of integer [candidates] (may have duplicates), and an integet [target]. Find all unique combinations where combinations
#          sum up to [target]. Each number in candidates can be used no more than once.
# Description: DFS backtrack, on a sorted [candidates]. Each iteration track the starting index [start], and maintain [candidates] in recursion.
#              skip dupliate elements if "candidates[i]==candidates[i-1]". Deduct [target] when "candidates[i]" is added to a combination. If
#              [target]==0, the sum is reached and add current combination to result. If target<0, the sum is exceeded and return to stop 
#              recursion. 
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    combinationSum2_helper(sorted(candidates), 0, target, [], res)          # [candidates] must be sorted
    return res

def combinationSum2_helper(pool: List[int], start: int, target: int, comb: List[int], res: List[int]):
    if target==0:               # find a combination sum up to [target]
        res.append(comb)
        return
    if target>0:                # combination exceeded [target]
        return
    for i in range(start, len(pool)):
        if start!=i and pool[i]==pool[i-1]:
            continue
        if pool[i]>target: break            # early ternimation
        combinationSum2_helper(pool, start+1, target-pool[i], comb+[pool[i]], res)

# 22.43 Multiply Strings ==================================================================== https://leetcode.com/problems/multiply-strings/
# Problem: Given two non-negative integer strings [num1] and [num2]. return the product of them as string.
# Description: Maintain a integer list [res] has same length of total length of [num1] and [num2], all elements in [res] are "0" initially.
#              Iterate [num1] and [num2] reversely in nested loop, because multiplication is done by multiplying a digit in [num1] with 
#              every digit in [num2]. Track index of [num1] and [num2] while multiplying to maintain index of [res] to store the "produect"
#              and "carry". After looping, truncate leading "0", and return reversed [res] with every element casted to string
# Time complexity: O(n*m), n=len(num1) m=len(num2)
def multiply(num1: str, num2: str) -> str:
    res = [0]* (len(num1) + len(num2))          # initial [res] with all "0"s
    for i, e1 in enumerate(reversed(num1)):
        for j, e2 in enumerate(reversed(num2)):
            res[i+j] += (ord(e1)-48) * (ord(e2)-48)           # convert string to int, and get product
            res[i+j+1] += res[i+j]//10                      # add carry to next digit
            res[i+j] %= 10                                  # get number for current digit

    while len(res) > 1 and res[-1] == 0: res.pop()          # truncate leading "0"
    return ''.join( map(str,res[::-1]) )                    # use "map(str, iterable)" to cast element to string

# 23.45 Jump Game II =========================================================================== https://leetcode.com/problems/jump-game-ii/
# Problem: Given a list of non-negative integers [nums], each element represent how many index you can jump from that location. For example,
#          nums[0] = 3 then from nums[0], can jump to nums[1], nums[2] or nums[3]. Assume you start from index 0, return the minimal [jumps] 
#          to reach the end of [nums]
# Description: Greedy. Iterate through elements in [nums]. Maintain [furthest] as the furthest index reached so far, which is update for 
#              element in [nums] to be max(furthest, i+nums[i]). Maintain [lastJump] as the index reached in last jump, when iteration 
#              reaches [lastJump], update [lastJump] as [furthest] to make another jump. After making a new jump, increase [jumps] by 1.
#              If [furthest] touches or exceeds the end of [nums], return [jumps]
# Time Complexity: O(n), n=len(nums)
def jump(nums: List[int]) -> int:
    if len(nums)<=1:                                # corner case, no need to jump, already start at the end of [nums]
        return 0
    furthest = lastJump = jumps = 0
    for i in range(len(nums)):
        furthest = max(furthest, i+nums[i])         # update [furthest] for every elements
        if i == lastJump:                           # when [i] touches last jump location, make a jump to [furthest]
            lastJump = furthest
            jumps+=1
        if lastJump >= len(nums)-1:                 # reaches the end of [nums] return [jumps]
            return jumps    

# 24.46 Permutations ============================================================================== https://leetcode.com/problems/permutations/
# Problem: Given a list of "distinct" integers, return all possible permutations in an array
# Description: DFS backtracking. Use recursive function, maintain [pool] as integers that are not added to permutation yet, maintain [temp] as 
#              current permutation, maintain [res] as the result list where each element is a permutation. In back track, extract an integer
#              a time from [pool] to [temp]. Pass the rest [pool] to next recursive call, and append extracted integer to [temp]. If [pool]
#              is empty, means all integer are added to [temp], then append [temp] to [res]
# Time complexity: O(n!)
def permute(nums: List[int]) -> List[List[int]]:
    res = []
    permute_helper(nums, [], res)
    return res
    
def permute_helper(pool, temp, res):
    if pool == []:
        res.append(temp)
    else:
        for i in range(len(pool)):
            permute_helper(pool[:i]+pool[i+1:], temp+[pool[i]], res)

# 25.47 Permutations II ========================================================================== https://leetcode.com/problems/permutations-ii/
# Problem: Given a list of integers [nums] with duplicates. Return all possbile "unique" permutations in a list.
# Description: Back track on keys of Counter(nums) as [counter]. [counter] doesn't have duplicate keys, back track on Counter(nums) helps get rid 
#              of duplicates. Maintain a list [temp] holding current perumutation, and [res] as result list holding permutations. Each recursion 
#              iterate though key of [counter], if counter[key] > 0, append [key] to [temp], reduce counter[key] by 1. Then pass the reduced 
#              [counter] and appended [temp] to next recursion. After each recusive call, restore counter[key] by adding 1 back to it, and 
#              pop last integer added before recursive call. When [temp] has same length of [nums], means all integer is added to [temp], so
#              append [temp] to [res]
# Time complexity: O(n^2)
from collections import Counter
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    permuteUnique_helper(Counter(nums), len(nums), [], res)
    return res

def permuteUnique_helper(counter, length, temp, res):
    if len(temp) == length:
        res.append(temp[:])         # append deep copy of [temp], since [temp] will be modified along the recursion
    for n in counter:
        if counter[n]>0:            # counter[n]>0, means there is "n" that can be inserted to [temp]
            temp.append(n)              # append [n] to [temp] and reduce [counter] of "n"
            counter[n] -= 1
            permuteUnique_helper(counter, length, temp, res)
            counter[n] += 1             # restore [counter] and [temp]
            temp.pop()

# 26.48 Rotate Image =============================================================================== https://leetcode.com/problems/rotate-image/
# Problem: Given a "n*n" [matrix], rotate the matrix by 90 degree clockwise. Modify the [matrix] "in-place"
# Description: Rotate a matrix layer by layer, since top row is rotated to right-most column, right-most column is rotated to buttom row, buttom
#              row is rotated to left-most column, left-most column is rotated to top row. Consider there two row and two column as outter-most 
#              layer. A "n*n" matrix contains "n//2" layers, say the outter-most layer is "0"th layer. For "i"th layer, the element are from 
#              column "i" to column "n-i-1". When rotate an element, other three elements of other side of layer are also involved, where top 
#              [i][j] moves to right [n-1-j][i], right [n-1-j][i] moves to buttom [n-1-i][size-1-j], buttom [n-1-i][n-1-j] moves to left [j][n-1-i].
#              Repeat the four-switches for elements in top row of a layer, and repeat for every layer
# Time compleixty: O(n^2), n=len(matrix)
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp

# 27.49 Group Anagrams =========================================================================== https://leetcode.com/problems/group-anagrams/
# Problem: Given an array of strings [strs], group the "anagrams" together.
#          Anagarms: are words that contain same characters.
#          Ex: ["eat","tea","tan","ate","nat","bat"] ===> [["bat"],["nat","tan"],["ate","eat","tea"]]
# Description: For each word in [strs], create an integer array [num_list] with 26 zeros, representing 26 alphates. Iterate characters in [word], 
#              add one to corresponding element in list. Convert [num_list] to "tuple" and use it as "key" of dictionary [record], and append 
#              [word] to the value of record[key]. Return the value of [record] at the end
# Time complexity: O(NK), N=len(strs) K=length of each word
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    record = defaultdict(list)              # maintain dictionary, the value is "list"
    for s in strs:
        num_list = [0]*26                   # creact list of 26 elements
        for c in s:
            num_list[ord(c)-97] += 1            # convert character to corresponding index in [num_list]
        record[tuple(num_list)].append(s)   # convert to "tuple" as key in dictionary
    return record.values()

# 28.50 Pow(x, n) ==================================================================================== https://leetcode.com/problems/powx-n/
# Problem: Implement pow(x, n), which calculate [x] raised to power [n]. It is possible that "n<0", Ex: pow(2, -10) = 1/1024
# Description: Recursion. Because of x^n == x^(n/2) * x^(n/2), then continuously reduce [n] by half, and multiply two halves. If [n] is odd,
#              x^n == x^(n/2) * x^(n/2) * x, then reduce [x] by half, and multiply two halves and an extra [x]. When [n] hit zero n==0,
#              return 1, because any number x^0 == 1
# Time compleixty: O(logN)
def myPow(x: float, n: int) -> float:
    if n>0:
        return myPow_helper(x, n)
    else:
        return 1/myPow_helper(x, -n)
    
def myPow_helper(x, n):
    if n == 0:
        return 1
    half = myPow_helper(x, n//2)            # reduce [n] by half
    if n%2==0:
        return half*half                    # if n is even, multiply two halves
    else:
        return half*half*x                  # if n is odd, multiply two halves and an extra [x]

# 29.54 Spiral Matrix ============================================================================= https://leetcode.com/problems/spiral-matrix/
# Problem: Givne a "m*n" matrix, return all elements in "sprial order".
#          Ex [[1, 2, 3]    ===>  [1, 2, 3, 6, 9, 8, 7, 4, 5]
#              [4, 5, 6]    
#              [7, 8, 9]]   
# Description: Define four boundaries [top], [bottom], [left], [right]. Bring down [top] by 1, after traversing a row on top. Move [right] to 
# #            left by 1, after traversing a column on right side. Raise up [bottom] by 1, after traversing a row at bottom. Move [left] to 
#              right by 1, after traversing a column on left side. When traversing a row, traverse elements between [left] and [right], when
#              traversing a column, traverse elements between [top] to [bottom]. Check if boundary overlap after traversing a row or column, 
#              exit loop if any boundaries overlaps each other
# Time complexity: O(n*m)
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1        # define 4 boundaries
    res = []                
    while True:
        for i in range(left, right+1):              # traverse top row
            res.append(matrix[top][i])
        top+=1                                          # lower [top]        
        if top>bottom: return res                       # check boundary overlap
        for j in range(top, bottom+1):              # traverse right column
            res.append(matrix[j][right])
        right-=1                                        # move [right] to left
        if left>right: return res                       # check boundary overlap
        for i in reversed(range(left, right+1)):    # traverse bottom row
            res.append(matrix[bottom-1][i])
        bottom-=1                                       # raise [bottom]
        if top>bottom: return res                       # check boundary overlap
        for j in reversed(range(top, bottom)):      # traverse left column
            res.append(matrix[j][left])
        left+=1                                         # move [left] to right
        if left>right: return res                       # check boundary overlap

# 30.55 Jump Game =================================================================================== https://leetcode.com/problems/jump-game/
# Problem: Given a non-negative integer list [nums], where each element represent maximum indeices you can jump from there. Starting from index
#          zero, determine if you are able to reach the last index.
# Description: Greedy. Maintain a [furthest] represent the maximum index can be reached so far. Iterate though [nums], the furthest can reach 
#              is "i+nums[i]", update [furthest] if any larger index can be reached. If "i > furthest" for any index, meaning index [i] can't
#              be reached, return False. If iteration hit the end of [nums], meaning the end is reached, return True
# Time complexity: O(n), n=len(nums)
def canJump(nums: List[int]) -> bool:
    furthest = 0
    for i in range(len(nums)):
        if furthest<i:
            return False
        furthest = max(furthest, i+nums[i])
    return True

# 31.56 Merge Intervals ======================================================================== https://leetcode.com/problems/merge-intervals/
# Problem: Given a 2D array [intervals], where each element represents an interval [start, end], merge all overlapping intervals, and return an
#          array of non-overlapping intervals 
#          Ex: [[2,6],[1,3],[15,18],[8,10]] ===> [[1,6],[8,10],[15,18]]
#          [1,3] and [2,6] overlaps, can be merged
# Description: Sort [invertals] by "starting boundary" in ascending order. Maintain a [res] array as result initial with "intervals[0]" in it.
#              Iterate through element in [intervals], let [prev] be the last element in [res] and [cur] the element of current interation. If
#              "prev[1] >= cur[0]", then [prev] and [cur] overlaps. Extends the "end" of [prev] in [res] to be max(prev[1], cur[1]). If there 
#              is no overlap between [cur] and [prev], append [cur] to [res] directly
# Time complexity: O(NlogN), N=len(intervals)
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda ele:ele[0])       # sort by "starting boundray"
    res = [intervals[0]]                        # [res] array initial with first element of [intervals]
    for cur in intervals[1:]:
        prev = res[-1]                      
        if prev[1]>=cur[0]:                 # detect overlap of [prev] and [cur]
            prev[1] = max(cur[1], prev[1])      # extend "end" of [prev]
        else:
            res.append(cur)                 # no overlap, add [cur] directly
    return res

# 32.57 Insert Interval ========================================================================= https://leetcode.com/problems/insert-interval/
# Problem: Given a set of non-overlapping [intervals], insert a new interval [neInterval], merge overlap after inserting if any.
#          The given [intervals] is sorted initially in ascending order by their "starting"
# Descrption: If [newInterval] overlaps with elements in [intervals], there must exist that "newInterval[0] <= intervals[i][1]", where 
#             [newInterval] starts from "intervals[i]". Or there must exist that "newInterval[1] < intervals[j][0]", where [newInterval]
#             end with "intervals[j-1]". Thus, every intervals between [i] and [j] should be merged.
#             Use binary search to find [i] and [j]. And decide the boundary of merged intervals [merge_start] and [merge_end], where
#             "[merge_start] = min(intervals[i][0], newInterval[0])", and "[merge_end] = min(intervals[j][1], newInterval[1])". Combien
#             [merged] with the rest of [intervals] and return
# Time complexity: O(N), N=len(intervals) combine [merged] with rest of [intervals] takes O(N)
def insert(intervals, newInterval):
    if len(intervals) == 0:                     # corner case
        return [newInterval]
        
    if newInterval[1] < intervals[0][0]:        # corner case
        return [newInterval] + intervals
    
    if newInterval[0] > intervals[-1][1]:       # corner case
        return intervals + [newInterval]
    
    first = insert_helper(intervals, newInterval[0], True)          # find starting point of merge
    second = insert_helper(intervals, newInterval[1], False)        # find ending point of merge
    
    merge_start = min(intervals[first][0], newInterval[0])
    merge_start = max(intervals[second-1][1], newInterval[1])
    merged = [merge_start, merge_start]                             # get [merged] interval
    return intervals[:first] + [merged] + intervals[second:]        # combine [merged] with rest of [intervals]

def insert_helper(intervals, target, findLeft=True):
    left = 0
    right = len(intervals) 
    if findLeft:                                # bisect_left
        while left < right:
            mid = left + (right - left) // 2
            if intervals[mid][1] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    else:                                       # bisect_right
        while left < right:
            mid = left + (right - left) // 2
            if intervals[mid][0] > target:
                right = mid
            else:
                left = mid + 1
        return left

# 33.59 Spiral Matrix II ====================================================================== https://leetcode.com/problems/spiral-matrix-ii/ 
# Problem: Given a positive integer [n], generate a "n*n" matrix fill with integers start from 1 to n^2 in sprial order
#          Ex n = 3  ==>  1 -> 2 -> 3
#                                   |
#                         8 -> 9    4
#                         |         |
#                         7 <- 6 <- 5
# Description: Track boundary [left], [right], [top], [bottom]. While [left]<[right] and [top]<[bottom], traval along the boundary and fill 
#              numbers. Shrink boundary while traveling. After travel "left" to "right", reduce [top]. After travel "top" to "bottom", reduce
#              [right]. After travel from "right" to "left", reduce [bottom]. After travel from "bottom" to "top" reduce [left]
# Time complexity: O(n*n)
def generateMatrix(n: int) -> List[List[int]]:
    res = [[0 for j in range(n)] for i in range(n)]     # create a empty n*n matrix initially
    left, right, top, bottom = 0, n, 0, n               # initialize boundary
    n = 1                                               # initialize number to be filled
    while left<right and top<bottom:
        for col in range(left, right):                      # left to right
            res[top][col] = n
            n+=1
        top += 1
        if top == bottom: return res
        for row in range(top, bottom):                      # top to bottom
            res[row][right-1] = n
            n+=1
        right -= 1
        if left == right: return res
        for col in reversed(range(left, right)):            # right to left
            res[bottom-1][col] = n
            n+=1
        bottom -= 1
        if top == bottom: return res
        for row in reversed(range(top, bottom)):            # bottom to top
            res[row][left] = n
            n+=1
        left += 1
        if left==right: return res
    return res

# 34.61 Rotate List ================================================================================= https://leetcode.com/problems/rotate-list/
# Problem: Given a [head] of a linked list, and a positive integer [k]. Rotate elements in linked list to the right by [k] places
#          Ex: 1->2->3->4->5, k=3
#              rotate once: 5->1->2->3->4 
#              rotate twice: 4->5->1->2->3
#              rotate triple: 3->4->5->1->2
# Description: Iterate though the list to get [size]. Get actual [rotates] need by [k%size]. Find the [rotates]th last element from end of list,
#              Disconnect elements [rotates] and [rotates+1], make [rotates+1] the new [head], and connect [tail] element to old [head]
# Time Complexity: O(N)
def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head:
        return None
    size = 1
    cur = head
    while cur.next != None:                 # Record [size]
        size += 1   
        cur = cur.next
    tail = cur
    rotate = k%size                         # Get [rotate] from [k%size]
    if rotate == 0:
        return head
    else:
        tail.next = head                    # connect [tail] to old [head]
        cur = head
        for _ in range(size-rotate-1):      # find [rotate]th last element
            cur = cur.next
        head = cur.next                     # let [rotate+1] be the new head
        cur.next = None                     
        return head

# 35.62 Unique Paths ====================================================================================== https://leetcode.com/problems/unique-paths/
# Problem: Given a m*n grid, a robot starts from top-left corner. The robot can only move down or right, how many possible unqiue path to go to bottom
#          right corner.  1 <= m, n <= 100
# Description: Permutation with duplicates. The problem can be converted to permutation of (m-1) downs and (n-1) rights. According to the formula of 
#              permutation with duplications: [(m-1)+(n-1)]! / [(m-1)! * (n-1)!]
# Time compleixty: O(m+n)
import math
def uniquePaths(m: int, n: int) -> int:
    m -= 1
    n -= 1
    return math.factorial(m+n)//math.factorial(m)//math.factorial(n)

# Description: Dynamic Programming, Maintain a 2d matrix that each element dp[i][j] represents number of unique path to goto [i][j]. In order to goto 
#              [i][j], the robot can only move from [i][j-1] or from [i-1][j]. Thus, the value of [i][j] is the sum of [i-1][j] and [i][j-1]. The first
#              row and first column are all "1"s, since there is only one unique path along first row and first column. Return dp[-1][-1] at the end
def uniquePaths_2(m: int, n: int) -> int:
    dp = [[1 for i in range(n)] for j in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r][c-1] + dp[r-1][c]
    return dp[-1][-1]

# 36.63 Unique Paths II ================================================================================== https://leetcode.com/problems/unique-paths-ii/
# Problem: Given a [m*n] array represents a grid, where "0" element represent a available path, and "1" represent a obstacleG that robot can not pass
#          The robot start from top-left corner and try to reach bottom-right corner, the robot only moves down or right. Find how many unique paths
#           would there be
# Description: Dynamic programming. Maintain a [m*n] matrix that each element dp[i][j] represent number of unique path to reach [i][j]. In order to 
#              goto [i][j], the robot can move from [i][j-1] or from [i-1][j]. Thus, the value of [i][j] is the sum of [i-1][j] and [i][j-1]. However,
#              if [i][j] is an obstacle, then there is no path, meaning [i][j] = 0.  Mutiply (1-obstacleGrid[i][j]) to test if [i][j] is obstacle
#              The first row and first column should all be "1"s, unless obstacle, since there is only an unique path along first row and first column. 
#              Return dp[-1][-1] at the end
# Time complexity: O(m*n)
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int: 
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:            # early terminate when start or end element is obstacle
        return 0
    obstacleGrid[0][0] = 1                                              # the top-left element is always 1 if it is not obstacle
    for i in range(1, len(obstacleGrid)):                                   # set value for first row
        obstacleGrid[i][0] = obstacleGrid[i-1][0]*(1-obstacleGrid[i][0])
    for i in range(1, len(obstacleGrid[0])):                                # set value for first column
        obstacleGrid[0][i] = obstacleGrid[0][i-1]*(1-obstacleGrid[0][i])

    for i in range(1, len(obstacleGrid)):                # number of path of [i][j] is sum of [i-1][j] and [i][j-1], if [i][j] is not obstacle
        for j in range(1, len(obstacleGrid[0])):            
            obstacleGrid[i][j] = (obstacleGrid[i-1][j]+obstacleGrid[i][j-1]) * (1-obstacleGrid[i][j])
    return obstacleGrid[-1][-1]

# 37.64 Minimum Path Sum ============================================================================ https://leetcode.com/problems/minimum-path-sum/
# Problem: Given a [m*n] grid filled with non-negative integers, where each element of grid represent to cost to go through that cell. Find a path
#          from top-left corner to bottom-right corner with minimal cost, and return the minimal cost. You can only move down or right for each step
# Description: Dynamic Programming. Maintain a [m*n] matrix that each element dp[i][j] represent the minimal cost to reach that cell. In order to 
#              go to bottom-right corner, and only move down or right, you can either move from [i-1][j] to [i][j] or move from [i][j-1] to [i][j].
#              Thus, [i][j] = min([i-1][j], [i][j-1]) + [i][j]. Return dp[-1][-1] at the end
# Time complexity: O(m*n)
def minPathSum(grid: List[List[int]]) -> int:
    m,n = len(grid), len(grid[0])
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

# 38.71 Simplify Path ============================================================================ https://leetcode.com/problems/simplify-path/
# Problem: Given a string [path], which is a "absolute path" to a file or dirctory in a Unix-style file system, convert it to simplified 
#          "canonical path". In Unix-style file system, a period "." refer to current directory, a double period ".." refers to directory up a
#          level, multiple slashes "//" are treated as single slash "/". Any other format are treated as file/directory name.
#          A "Canonical path" should have following format
#          1. path starts with a slash "/"
#          2. any two directories are separated by a slash "/"
#          3. path does not end with slash "/"
#          4. the path only contains directories on the path from root directory to current file/directory
#          Ex: "/a/./b/..//../c/"  ==>  "/c"
# Description: Use a "stack" to track history of direcories. Split [path] by slash "/". Maintain a [stack] and iterate the splited array, 
#              if ".." pop last element from stack, if "." or empty string "", do nothing and move on to next, else append element to stack.
#              The [stack] contains the "canonical path" as an array. Combine elements in array to a string with slash between each element, 
#              and add one more slash at beginning. Return the constructed string
def simplifyPath(path: str) -> str:
    stack = []                  # maintain a stack to track directory history
    path = path.split("/")
    for direcotry in path:
        if direcotry == "..":           # move up level if ".."
            if stack:
                stack.pop()
        elif direcotry == "." or direcotry == "":       # do nothing if "." or empty string
            continue
        else:                               # add directory to stack
            stack.append(direcotry)
    return "/"+"/".join(stack)              # combine elements of stack to build canonical path

# 39.73 Set Matrix Zeroes ========================================================================== https://leetcode.com/problems/set-matrix-zeroes/
# Problem: Given a "m*n" [matrix]. If a element in matrix is "0", then set its entire row and column to "0" in-place
#          Consider solve the problem with constant space
# Description: Use first row and first column as "marker" to denote which row/coulmn need to be set to "0".Iterate through the elements in [matrix], 
#              if the element at [i][j] is "0", set the [i][0] and [0][j] to "0". [i][0] and [0][j] will be the marker to set entire [i]th row and 
#              entire [j]th column to "0" in the second iteration. Iterate the elements in [matrix] the second time, for element [i][j], if [i][0] 
#              or [0][j] equals to "0", meaning [i][j] is on the row or column to be set to "0". Since we use first row and first column as "marker",
#              need to set first row/column separately. Use two booleans [firstRowZero] and [firstColZero], detect if first row/column has "0", and 
#              set entire corresponding row/column to "0"
# Tiem compleixty: O(m*n)
def setZeroes(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    # detect "0" in first row and first column
    firstRowZero = firstColZero = False     
    for i in range(m):
        if matrix[i][0] == 0:
            firstColZero = True
            break
    for j in range(n):
        if matrix[0][j] == 0:
            firstRowZero = True
            break
    # find "0" and set corresponding first row/column to "0" as marker
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    # set entire row/column to "0", if marker is "0"
    for i in range(1, m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # set entire first row/column to "0", if there exist "0" originally
    if firstRowZero:
        matrix[0] = [0]*n
    if firstColZero:
        for j in range(m):
            matrix[j][0] = 0

# 40.74 Search a 2D Matrix ============================================================================ https://leetcode.com/problems/search-a-2d-matrix/
# Problem: Given a "m*n" [matrix], where numbers in a row are sorted, and the first element of each row is alway larger than the last element of previous
#          row. Given a number [target], check if [target] exists in [matrix], return True or False accordingly
# Description: Treat the [matrix] as a sorted list, and use binary search. The first element is index 0 and last element is index "m*n-1". For element at
#              index [i], its index in [matrix] is [i//n][i%n]. Because [i//n] is the row index and [i%n] is the column index. Use binary search and get
#              [mid] element and compare it with [target], swap index [left] and [right] with [mid] accordingly
# Time compleixty: O(log(m*n))
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m,n=len(matrix), len(matrix[0])
    left, right = 0, m*n-1              # binary search, [left] starts from top-left, [right] starts from bottom-right
    while left<=right:
        mid = (left+right)//2
        num = matrix[mid//n][mid%n]     # convert [mid] to the row and column of matrix
        if num < target:
            left = mid+1
        elif num > target:
            right = mid-1
        else:
            return True
    return False

# 41.75 Sort Colors ========================================================================================= https://leetcode.com/problems/sort-colors/
# Problem: Given a list of integers, and each element can only be 0, 1 or 2, where 0 is "red", 1 is "white", 3 is "blue". Sort the list in-place, so that 
#          "red" come before "white", "white" come before "blue". Consider a solution with O(n) time complexity and O(1) space complexity
# Description: Dutch national flag problem, which is a problem to partition a list into three groups. Maintain pinters [red] and [blue]. [red] starts from
#              index 0 to represent the boundary between [red] and [white], meaning index [0, red) are "red" elements. [blue] starts from last index
#              to represent to boundary between [white] and [blue], meaning index (blue, len-1] are "blue" elements. Maintain another pointer [cur], 
#              move [cur] from index 0 towards the end of list. 
#              If [cur] is "red", swap [red] with [cur] make [red] contains "red" element and increase both of them, since element on [red] must be "white"
#              If [cur] is "white", no swap and increase [cur]
#              If [cur] is "blue", swap [blue] with [cur] make [blue] coontains 'blue" element and decrease [blue], no increament on [cur], since the 
#              element swap to [cur] is unknown
# Time Compelexity: O(n)
# Space complexity: O(1)
def sortColors(nums: List[int]) -> None:
    red, blue = 0, len(nums)-1      # maintain index boundary of "red", "white" and "blue"
    cur = 0
    while cur<=blue:                # stop when [cur] hit [blue] because element after [blue] are all "blue"s
        if nums[cur] == 0:              # hit "red" element
            nums[cur], nums[red] = nums[red], nums[cur]
            cur += 1
            red += 1
        elif nums[cur] == 1:            # hit "white" element
            cur += 1
        else:                           # hit "blue" element
            nums[cur], nums[blue] = nums[blue], nums[cur]
            blue -= 1

# 42.77 Combinations =========================================================================================== https://leetcode.com/problems/combinations/
# Problem: Given two integers [n] and [k], return all combinations with length of [k], and consists of number of from [1, n]
# Description: DFS. Create a helper function, that takes three parameters [cur], [temp] and [res]. [cur] start from 1 and increases up to [n],
#              representing the current number need to be added to a combination. [temp] tracks the current combination sub-list. [res] is the result
#              2D list contains all combinations. If len(temp) is [k], current combination is finished and append [temp] to [res], return to stop this 
#              DFS. Recusive case, use a "for-loop" iterate from 1 to [n] and invoke "helper" function, the invoked "helper" function take i+1 as [cur],
#              append [i] tp [temp], and pass down [res].
# Time complexity: O(n^k)
def combine(n: int, k: int) -> List[List[int]]:
    def combine_helper(cur, temp, res):
        if len(temp) == k:                          # append [temp] to [res] when size is achieved
            res.append(temp)
            return
        for i in range(cur, n+1):
            combine_helper(i+1, temp+[i], res)      # increase [cur] by 1, append [i] to [temp]
    res = []
    combine_helper(1, [], res)
    return res
    
# 43.78 Subsets ============================================================================================== https://leetcode.com/problems/subsets/
# Problem: Given a list of unique integers [nums], return all possible subsets (power set) as 2d list. The solution should not contain duplication.
# Description: DFS, create a helper function that tracks [pool] as the element need to be appended to a subset, and [temp] represent the current 
#              subset. Invoke the helper function in a "for-loop" that itarete through elements in [pool] to form DFS. Each invoke of helper function, 
#              append [temp] to [res], since every [temp] is a valid subset, and remove the first element from [pool] and insert it into [temp]. If no 
#              more element left in [pool], return to stop the dfs path
# Time complexity: O(2^n)
def subsets(nums: List[int]) -> List[List[int]]:
    def subsets_helper(pool, temp, res):
        res.append(temp)                                    # append [temp] to [res], since every [temp] is a subset
        for i in range(len(pool)):
            subsets_helper(pool[i+1:], temp+[pool[i]], res)     # remove first element from [pool], append first element to [temp]
    res = []
    subsets_helper(nums, [], res)
    return res

# Description: Dynamic Programming, start with only an empty set "[]" in [res]. For every element in [nums], we can either add it to every existing 
#              subsets or leave the subsets as they are. For the first element, if we add the element we have [ele_1] as a new subset, and if we don't 
#              add the empty set remain the same. Now we have [res] = [[], [ele_1]]. For the second element [ele_2] to every existing subsets, we 
#              have [ele_2], [ele_1, ele_2], if we don't add, subsets remain same, then [res] = [[], [ele_1], [ele_2], [ele_1, ele_2]]. Do this for 
#              every elements in [nums].
# Time compleixty: O(2^n)
def subsets_2(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for n in nums:
        # take every existing subsets in [res] append with [n]
        # take every existing subsets in [res] but don't add [n]
        # concatenate "added" and "not added" subsets
        res += [subset + [n] for subset in res]     
    return res

# 44.79 Word Search ====================================================================================== https://leetcode.com/problems/word-search/
# Prolem: Given a "m*n" grid [board] with English characters, and a string [word]. Determine if [word] can be constructed from characters from [grid]
#         by connecting adjacent cells horizontally or vertically, where a cell can only be used once. Return True if [word] is constructed, otherwise
#         return False
# Description: DFS, iterate through every cell of [grid] that make each cell as the starting point to find [word]. Create a "helper function" use DFS
#              to find [word]. "helper function" maintain the current index [i] and [j], if [i] and [j] are within the range of [board], check the 
#              char in cell [i][j]. If the char is same as first char of [word]. Remove the first char of [word] to search for next char,  mark char
#              at [i][j] to "#" as it can not be used twice. Continue DFS on upper, bottom, left, and right cell by changing parameter of [i] and [j],
#              pass the modified [board] and [word] to new recursive calls. Restore value of [i][j] after all four recursive calls, return value of 
#              four recursive calls with OR gate. "helper function", return True when [word] is empty, meaning [word] is found in [board]
# Time complexity: O((n*m)^2)
def exist(board, word):
    for i in range(len(board)):                 # make every cell as the starting point
        for j in range(len(board[i])):
            if exist_helper(i, j, board, word):     # invoke DFS helper function
                return True
    return False
    
def exist_helper(i, j, board, word):
    if not word:                    # word is empty, [word] is found
        return True
    if i<0 or i>=len(board):        # [i] out of bound
        return False
    if j<0 or j>=len(board[i]):     # [j] out of bound
        return False
    if board[i][j] != word[0]:      # current cell [i][j] doesn't match
        return False
                                    # current [i][j] matches first char of [word]
    temp = board[i][j]                          # record value of [i][j] for restore 
    board[i][j] = "#"                           # mark [i][j] as visited
    word = word[1:]                             # remove first char of [word]
    # DFS on four directions
    down = exist_helper(i+1, j, board, word)    
    right = exist_helper(i, j+1, board, word) 
    up = exist_helper(i-1, j, board, word) 
    left = exist_helper(i, j-1, board, word)
    board[i][j] = temp                          # restore value of [i][j]
    return down or right or up or left

# 45.80 Remove Duplicates from Sorted Array II ================================= https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/ 
# Problem: Given a sorted integer array [nums], remove duplicates "in-place" such that duplicates appears at most twice, and return the new length.
#          Consider modify the array "in-place" with O(1) extra space
# Description: Maintain pointers [slow] and [fast], both start from index 2. [slow] track the tail of result list, [fast] finding non-duplicate element
#              and replace duplicate element on [slow]. And the value of [slow] alway less than or equals to [fast]. If [slow-2] == [fast], means the 
#              element [slow-2], [slow-1] and [slow] must share same value, thus the value of [slow] must be replaced, then move [fast] to find a new
#              value that doest not equal to [slow-2] and replace it. If [slow-2] < [fast], an eligible value is found on [fast], [fast] should replace
#              [slow] to remove duplicate, and move both [slow] and [fast] to next element. End iteration when [fast] hit end of list.
# Time Compleixty: O(n)
def removeDuplicates(nums: List[int]) -> int:
    slow = fast = 2
    while fast < len(nums):         # end iteration when [fast] hit end
        if nums[slow-2] < nums[fast]:       # [fast] can be used to replace [slow]
            nums[slow] = nums[fast]
            slow += 1                       # duplicates is eliminated for current [slow], move [slow] to next
        fast += 1                   # move [fast] to find a non-duplicate element to replace, also move [fast] after replacement
    return slow             

# 46.81 Search in Rotated Sorted Array II ==================================== https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Problem: Given an integer list [nums], sorted in ascending order with duplicated elements. [nums] is rotated at an unknown pivot index, such as
#          [0,1,1,2,3] rotate at pivot index 2 becomes [1,2,3,0,1].
#          Given an integer [target], determine if [target] exists in [nums]. Return True or False accordingly
# Description: Leverage algorithm of "Search in Rotated Sorted Array"(without duplicated elements). Maintain pointer [l] and [r] that starts from
#              index [0] and index [len(nums)-1], get [mid] = ([l]+[r])//2, and apply binary search on sorted sublist. If [l]<=[mid], that left 
#              sublist from [l] to [mid] is sorted, if [target] is in between [l] and [mid], shink [r] = [mid]-1, if [target] doesn't fall in the 
#              range of [l] and [mid], move [l] = [mid]+1 to search the other sublist. If [mid]<=[r], that right sublist from [mid] to [r] is 
#              sorted, if [target] is in between [mid] and [r], shink [l]=[mid]+1, if [target] doesn't fall in the range of [mid] and [r], move
#              [r] = [mid]-1 to search the other sublist. And if [mid]==[target], return True. 
#              Since [nums] contains duplicates, we should skip duplicates. While [l] == [mid], keep moving [l] to right, until index [l] equals 
#              to index [mid] or [l]!=[mid]
# Time complexity: O(logn)
def search_2(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:                 # target is found
            return True  
        while l < mid and nums[l] == nums[mid]:     # move [l] to skip duplicates
            l += 1
        if nums[l] <= nums[mid]:                # left half is sorted
            if nums[l] <= target < nums[mid]:      # target is in the sorted half, move [r] to [mid] to continue search this sublist
                r = mid-1
            else:                                   #  target is not in the sorted half, move [l] to [mid] to search other sublist
                l = mid+1
        else:                                   # right half is sorted
            if nums[mid] < target <= nums[r]:      # target is in the sorted half, move [l] to [mid] to continue search this sublist
                l = mid+1
            else:                                   # target is not in the sorted half, move [r] to [mid] to search other sublist
                r = mid-1
    return False

# 47.82 Remove Duplicates from Sorted List II ============================ https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Problem: Given the [head] of a sorted linked list, delete all node that appear more than once, and leave distince node in the list with their
#          original order. Return the head of modified linked list
# Description: Dummy node and Pointers. Maintain a pointer [tail] that tracks the end of linked list with duplicates removed. [tail] is a dummy
#              node initially, maintina [dummy] and [dummy.next] is returned as new head. Maintain [start] and [end] as the "starting" and 
#              "ending" node with same value. Move [end] to find the last element that have same value as [start], if [end] is [start.end] means 
#              there is no duplicate for current node, append the node [start] to [tail]. Move [tail] to next node, and move [start] to [end] to 
#              start new iteration. Stop the loop when [end] hit the end, assign None the [tail] and return [dummy.next]
# Time complexity: O(n)
def deleteDuplicates(self, head: ListNode) -> ListNode:
    dummy = tail = ListNode(0, None)
    start = end = head
    while end:
        while end and start.val == end.val:         # move [end] to find the end of duplicates
            end = end.next
        if start.next == end:           # no duplicate found, append [start] to [tail]
            tail.next = start
            tail = tail.next
            start = end
        else:                           # duplicate found
            start = end
    tail.next = None                    # append None to the end of linked list
    return dummy.next

# 48.86 Partition List ====================================================================== https://leetcode.com/problems/partition-list/
# Problem: Given a [head] of linked list, and a value [x]. Partition the nodes of linked list such that all nodes less than [x] comes before
#          the nodes greater than or equals to [x]. Preserve the original order within each partitions
# Description: Sperate nodes into two linked lists. Create two new dummy nodes of linked list, [dummyLess] is the dummy node that leading 
#              the "less than" portion, [dummyGreat] is the dummy node that leading the "greater or equal to" portion. Iterate through nodes
#              in original linked list, compare node with [x] and append into two linked list accordingly. Append None to the end of  
#              [dummyGreater], append the head of [dummyGreater] to [dummyList], and return the head of [dummyLess]
# Time Complexity: O(n)
def partition(head: ListNode, x: int) -> ListNode:
    dummyLess = tailLess = ListNode(0, None)            # create dummyLess to collect nodes less than [x], and maintain tail to add new node
    dummyGreat = tailGreat = ListNode(0, None)          # create dummyGreat node to collect nodes less than [x], maintain tail to add new node
    while head:                                 # iterate every node in [head] 
        if head.val<x:                              # if node.val < x, append it to [tailLess]
            tailLess.next = head
            tailLess = head
        else:                                       # if node.val >= x, append it ot [tailGreat]
            tailGreat.next = head
            tailGreat = head
        head = head.next                        
    tailLess.next = dummyGreat.next             # append "greater" portion to the end of "less" portion
    tailGreat.next = None                       # append None to the end of "greater" potion
    return dummyLess.next               # return head of "less" portion

# 49.89 Gray Code ============================================================================= https://leetcode.com/problems/gray-code/
# Problem: The gray code is a binary number system where two adjacent values differ in only one bit.
#          Given an integer [n] representing the number of bits in the gray code, return a sequence of gray code.
#          A gray code always starts with 0, Example n = 3
#          [000, 001, 011, 010, 110, 111, 101, 100] is a sequence of gray code
# Description: Iterate i from (0 to n), and maintain sequence as [res]. Every iteration, take existing elements in [res] in reversed order,
#              and add 2**i to every element and append them to [res]. The reason is explained below
#              Inspect sequence of n=3,
#              1. 000
#              2. 001
#              3. 011      010
#              4. 110      111     101     100
#              Initially, only 0 is in sequence, sequence is [0]
#              Take elements reversely from sequence, Add 2**0 to every elements, append them to sequence, sequence is [0, 1]
#              Take elements reversely from sequence, Add 2**1 to every elements, append them to sequence, sequence is [0, 1, 11, 10] 
#              Take elements reversely from sequence, Add 2**2 to every elements, append them to sequence, sequence is [0, 1, 11, 10, 110, 111, 101, 100] 
# Time complexity: O(2^n)
def grayCode(n: int) -> List[int]: 
    res = [0]
    for i in range(n):
        res += [val+2**i for val in reversed(res)]
    return res

# 50.90 Subsets II ========================================================================== https://leetcode.com/problems/subsets-ii/
# Problem: Given an integer list [nums], which may contain duplicates. Return all possible unique subsets of [nums].
# Description: DFS. Use backtracking to construct subsets same as "subset I". Sort [nums] before passing into backtracking, backtrack 
#              function maintains list of elements [nums] that have not been picked yet, the list of elements [temp] that are picked 
#              to construct a subset, and the [res] list that contains all possible subsets. Each backtrack call, append current subset
#              [temp] to [res], skip indices that nums[i-1] == nums[i]. Because taking equal value in the same DFS tree level creates 
#              duplicates subset. And invoke next level backtrack, that current element is removed from non-picked numbers, add current
#              element is appended to [temp]
# Time complexityL O(2**n)
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    def subsetWithDup_helper(nums, temp, res):
        res.append(temp)
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            else:
                subsetWithDup_helper(nums[i+1:], temp+[nums[i]], res)
    res = []
    subsetWithDup_helper(sorted(nums), [], res)
    return res

# 51.91 Decode Ways ========================================================================== https://leetcode.com/problems/decode-ways/
# Problem: Given a string [s], which contains integers that encoded from letter A-Z. The encoding mapping is A=1, B=2 ... Z=26. There exists
#          some digits that the same combination of digits can be decoded to multiple alphabet letters. Such as, [s]=11106 can be mapped to
#          1 1 10 6=>AAJF, and 11 10 6=>KJF. Note "06" cannot be mapped to "F", since "06" is different from "6".
#          Given the string [s] and return number of possible ways to decode [s] 
# Description: Dynamic Programming. Maintain a list [dp], where dp[i] represent the number of ways to decode substring s[:i]. 
#              If 0 < s[i-1] <= 9,it means s[i-1] itself can be decoded to a letter from A to I, the number of ways to decode s[:i-1] should
#              be inheritant to decode s[:i], so dp[i] += dp[i-1]. If 10<=s[i-2:i]<=26, means s[i-2] and s[i-1] can be decoded to a letter
#              from J to Z, the number of ways to decode s[:i-2] should also be inheritant to decode s[:i], thus dp[i] += dp[i-2]. Create [dp] 
#              with len(s)+1 element, initially all set to zero. dp[0] is the base case and dp[0]=1. dp[1] is the number of ways to decode 
#              first letter, if s[0] is "0" and "0" cannot be decode to any letter, so dp[1] = 0 if s[0]=="0", if s[0] != "0" there is one way 
#              to decode a single letter, thus dp[1]=1 if s[0]!="0".
#              Itearte through [s] from index 2 to len(s)+1, dupdate dp[i] as the number of ways to decode s[:i]. Return dp[-1] at the end
# Time complexity: O(n)
def numDecodings(s: str) -> int:
    dp = [0 for _ in range(len(s)+1)]           # create dp with len(s)+1 elements
    dp[0] = 1                                       # initial base offset dp[0] 
    dp[1] = 0 if s[0]=="0" else 1                   # initial number of ways to decode s[0]
    for i in range(2, len(s)+1):              
        if 0 < int(s[i-1]) <= 9:                    # s[i-1] can be decoded   
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:               # s[i-2] and s[i-1] combined can be decoded
            dp[i] += dp[i-2]
    return dp[-1]

# 52.92 Reverse Linked List II ======================================================== https://leetcode.com/problems/reverse-linked-list-ii/
# Problem: Given the [head] of a linked list, and two integers [left] and [right], where [left]<=[right]. Reverse the node from position [left]
#          to position [right], return the head of reversed list.
# Description: Create a [dummy] node where "dummy.next = head". Iterate from [dummy] to find the last node before position [left], denote it 
#              as [beg], the loop should iterate [left-1] times. 
#              After found [beg], use algorithm of "Reverse Linked List". Maintain three pointers [prev], [cur], and [next], where initally [prev]  
#              is None, [cur] points the node at position [left]. Iterate a loop [right-left+1] times, in which [next] is assigned with [cur.next]
#              [cur.next] points to [prev], and shift both [prev] and [cur] to next position.
#              Connect the revsered linked list with the reset of the node. At the end of loop, [prev] should points to the node at position [right] 
#              [cur] should points to the node right after [prev]. Thus, [beg.next.next] which is the last node of reversed list, should points to
#              [cur], which is the first node after reversed part. And [beg.next] should points to [prev] the connect to the first node of reversed
#              list.
# Time complexity: O(n)
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode: 
    if left==right:                     # corner case, no need to reverse if left==right
        return head
    dummy = ListNode(0, head)
    beg = dummy
    for _ in range(left-1):             # find the node before position [left]
        beg = beg.next
    # algorithm of Reverse Linked List
    prev = None
    cur = beg.next
    for _ in range(right-left+1):       # reverse list
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next  
    beg.next.next = cur                 # connect tail of reversed list to the node comes after 
    beg.next = prev                     # connect head of reversed list to the node comes before
    return dummy.next
    
# 53.93 Restore IP Addresses ================================================================== https://leetcode.com/problems/restore-ip-addresses/
# Problem: Given an integer string [s] containing only digits, return all possible valid IP address constructed from [s].
#          A valid IP consists of four parts separated by period ".", and each part is a integer number between 0 and 255. Each part can't have 
#          leading zero, but zero by itself is OK.
#          Ex: 1022310119 => 10.223.101.19 is a valid IP address
#                         => 102.231.0.11 is a valid IP address, since zero by itself is OK
#                         => 1.023.101.19 is invalidm "023" has leading zero
# Descritpion: DFS backtracking. Maintain [pool] as substring not taken, [temp] list track the valid IP sub-domains taken from [pool], [res] a set
#              that contains constructed valid IP addresses. For each recursive call, If [temp] contains four elements and no more char left in 
#              [pool], means a valid IP address is created, add [temp] to [res] in IP format. If len(temp)>4, number of domain is excessed, return
#              to stop this traversal. The recursive case, use for loop iterate [i] from 1 to 3, and validate pool[:i] to be inserted into [temp],
#              if pool[:i] is empty or excess 255, or pool[:i] contains multiple chars with leading zero, return this traversal because it is not 
#              possbile to get a valid domain for this recursive level.
#              Invoke new recursive call with pool[i:] to eliminate taken substring. temp+[take] that [take] is the valid domain pool[:i], and add
#              it to current constructed IP address, also pass [res] to next level
def restoreIpAddresses(s: str) -> List[str]:
    res = set()
    restoreIpAddresses_helper(s, [], res)
    return [el for el in res]

def restoreIpAddresses_helper(pool, temp, res):
    if len(temp)==4 and len(pool)==0:                           # valid IP address is created, [temp] has four domains and no char left in [pool]
        res.add(".".join(temp))                                     # add valid IP to [res]
        return
    if len(temp)>4:                                             # number of domains is exceeded
        return
    for i in range(1,4):                                        # take first three char from [pool] and valid them
        take = pool[:i]
        if not take or int(take)>255:                               # [take] is empty or exceeded 255
            return
        if i!=1 and take[0] == "0":                                 # [take] contains leading zero
            return
        restoreIpAddresses_helper(pool[i:], temp+[take], res)

# 54.95 Unique Binary Search Trees II ================================================ https://leetcode.com/problems/unique-binary-search-trees-ii/
# Problem: Given an integer n, return all the structurally unique binary search tree, which contains nodes from 1 to n. Return the answer in any
#          order
# Description: DFS backtracking. Create a recursive helper function, that take [start] and [end] as the node value should be created within it.
#              Iterate [i] from [start] to [end], where [i] is the root of tree that contains node between [start] to [end]. According to BST
#              property, left subtree of [i] contains nodes from [start] to [i-1], and right subtree contains nodes from [i+1] to [end]. Thus,
#              recursively call helper function on (start, i-1) and (i+1, end). Both recursive call will return a list of nodes which are 
#              all valid BS subtrees created. Connect all nodes returned from (start, i-1) as the left node of [i], and connect all nodes returned
#              from (i+1, end) as the right node of [i]. Append node [i] to a list [res], which is returned and to be used by upper level.
# Time complexity: TODO see Catalan Number
def generateTrees(n: int) -> List[TreeNode]:
    return generateTrees_helper(1, n+1)

def generateTrees_helper(start, end):
    if start==end:
        return None
    res = []
    for i in range(start, end):                                     # take [i] as root of this level
        for l in generateTrees_helper(start, i) or [None]:              # (start, i) are left subtree of [i]
            for r in generateTrees_helper(i+1, end) or [None]:          # (i+1, end) are right subtree of [i]
                node = TreeNode(i, l, r)                            # create node [i] and connect all possible left/right child to it
                res.append(node)                                
    return res                                                  # store [i] in [res] and return [res] to be used by upper level

# 55.96 Unique Binary Search Trees ==================================================== https://leetcode.com/problems/unique-binary-search-trees/
# Problem: Givne an integer [n], return the number of structually unique binary search trees which contains exactly nodes from 1 to [n].
# Description: Dynamic Programming. Consider the number of structually unique BST of [n] nodes is denoted as G(n). If we pick 1 as the root node,
#              no node in left subtree, and n-1 nodes in right subtree. It produces two sub-problems aka G(0) and G(n-1). If we pick 2 as the
#              root node, 1 node in left subtree G(1) and n-2 nodes in right subtree G(n-2). So on so forth, If we pick n-1 as the root node, there
#              are n-2 nodes in left subtree G(n-2), and 1 node in right subtee G(1). If we pick n as the root node, there aren-1 nodes in left 
#              subtree G(n-1) and 0 node in right subtree G(0). And the number of possiblilty is the cross-product of left and right subtree, thus
#              G(i-1)*G(n-i) the production of left and right is the number of BSTs when pick [i] at the root. Thus it has
#              G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-2)*G(1) + G(n-1)*G(0). Use DP to record from G(0) to G(n), and return G(n) at the end
# Time complexity: O(n^2) build [dp] of size n, each dp[i] need to iterate i times
def numTrees(n: int) -> int:
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 1, 1                 # G(0) and G(1) both equals to 1, since zero node and 1 node both have one unique structual
    for i in range(2, n+1):                 # iterate [i] to build [dp]
        for j in range(i):                      # [j] represents pick [j] at root
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]
    
# 56.97 Interleaving String =============================================================== https://leetcode.com/problems/interleaving-string/
# Problem: Given three strings [s1], [s2], [s3], check if [s3] is formed by an interleaving of [s1] and [s2].
#          And interleaving of two string [s] and [t] is a string that consists of character from [s] and [t], where the sequence of characters
#          of [s] and [t] doesn't change
#          Ex: s1 = [abcdef], s2 = {ghijk}, one of the interleaving s3 = {gh}[a]{i}[bcd]{j}[e]{k}[f]
#          where if we remove character of s2 then s3 becomes s1, and if we remove character of s1 then s3 become s2
# Description: Dynamic Programming. Create a 2d boolean list, with len(s1)+1 rows and len(s2)+1 columns. A cell dp[i][j] represents if substring
#              s3[:i+j] is an interleaving that formed from characters of s1[:i] and s2[:j]. To determine value of dp[i][j], it can be formed in
#              two ways. 1) from dp[i-1][j] and pick s1[i-1] as next character, if dp[i-1][j] is True and s1[i-1]==s[i+j-1], meaning dp[i-1][j] 
#              formed an interleaving, and adding s1[i-1] also form an interleaving, then dp[i][j] is True. 2) from dp[i][j-1] and pick s2[j-1] 
#              as next character, if dp[i][j-1] is True and s2[j-1]==s3[i+j-1], then dp[i][j] is Ture. Follow the manner and fullfill every cell
#              in dp, and return dp[-1][-1] as result
# Time complexity: O(m*n), n, m = len(s1), len(s2)
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    r, c, l = len(s1), len(s2), len(s3)
    if r+c!=l:                  # early termination if the size of s1, s2, and s3 doesn't match
        return False
    dp = [[False for _ in range(c+1)] for _ in range(r+1)]      # create [dp]. has len(s1)+1 rows and len(s2)+1 columns
    dp[0][0] = True                                             # when there is not character picked, [0][0] is always true
    for i in range(1, r+1):                                         # the first row represent only pick characters from s2 to form interleaving
        dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
    for j in range(1, c+1):                                         # the first column represent only pick character from s1 to form interleaving
        dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
    for i in range(1, r+1):
        for j in range(1, c+1):                                         # iterate thorugh cells in [dp]
            dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])  # fill [i][j] from either [i-1][j] or [i][j-1]
    return dp[-1][-1]               # last element of [dp] holds result

# 57.98 Validate Binary Search Tree =================================================== https://leetcode.com/problems/validate-binary-search-tree/
# Problem: Given the [root] of a binary search tree, determine if the tree is valid. A valid BST has following proerties:
#          1. left subtree of a [node] contains nodes that smaller than [node.val]
#          2. right subtree of a [node] contains nodes that larger than [node.val]
#          3. both left and right subtrees also satisfy there two rules
# Description: DFS. Maintain helper function which track the [floor] and [ceiling] of current [node.val]. For a [node], the node in its left subtree
#              can have a value that is less than [node.val] meaning ceiling = node.val, and the node in its right subtree can have value that is 
#              greater than [node.val] meaning floor = node.val. [floor] and [ceiling] are intially "float(-inf)" and "float('inf)" and passed down to 
#              each tree level
def isValidBST(root: TreeNode) -> bool: 
    return isValidBST_helper(root, float('-inf'), float('inf'))         # traverse from root of tree, give initial value of floor and ceiling

def isValidBST_helper(root, floor, ceiling):
    if not root:                                # no node left, this path is valid
        return True
    if root <= floor or root >= ceiling:        # current val is invalid
        return False
    # traverse to left child, use root.val as ceiling
    # traverse to right child, use root.val as floor
    # return True when both subtrees are valid
    return isValidBST_helper(root.left, floor, root.val) and isValidBST_helper(root.right, root.val, ceiling)
                
# 58.99 Recover Binary Search Tree =================================================== https://leetcode.com/problems/recover-binary-search-tree/
# Problem: Given the [root] of BST, there are exactly two nodes were swapped and out of place. Swap these two node back to place
# Description: Inorder traversal with stack. If traverse BST inorder, the node values are traversed in ascending order. If node are swapped. then
#              there will have node value than [prev.val] > [cur.val]. And there are two cases: 
#               1) swapped nodes are adjacent, the nodes sequence looks like following when traverse inorder, "... nodes < A > B < nodes ...". Node 
#                   "A" and "B" are out of place, need to swap them.
#               2) swapped nodes are not adjacent, the sequence looks like, "... nodes < A > X <  ... < Y > B < nodes ... ". There are two value
#                   decreasings, and "A" and "B" are the nodes that out of place, need to swap them. 
#              In both case, we want to swap "A" and "B", thus maintain a list of tuples [wrong] to record nodes that out of place. 
#              If swapped nodes are adjacent, then [wrong] contain single tupple (A, B), swap wrong[0][0].val and wrong[0][1].val
#              If swapped nodes are not adjacent, then [wrong] contains two tupples (A, X) and (Y, B), swap wrong[0][0].val and wrong[1][1].val 
#              Swap in both case can be simplified as swapping wrong[0][0].val and wrong[-1][1].val
# Time complexity: O(N)
# Space complexity: O(logN)
def recoverTree(root: TreeNode) -> None:
    cur, prev = root, TreeNode(float('-inf'))               # [prev] as previous node of [cur], that [prev.val] < [cur.val]
    stack, wrong = [], []
    while cur or stack:                                      # inorder traversal with [stack]
        if cur:
            stack.append(cur)
            cur = cur.left
        elif stack:
            cur = stack.pop()
            if cur.val<prev.val:                            # detect swapped nodes
                wrong.append((prev, cur))
            prev, cur = cur, cur.right
    wrong[0][0].val, wrong[-1][1].val = wrong[-1][1].val, wrong[0][0].val   # swap nodes back to place

# 59.102 Binary Tree Level Order Traversal ====================================== https://leetcode.com/problems/binary-tree-level-order-traversal/
# Problem: Given the [root] of a binary tree, return the "level-order traversal" of its node values. Return node values in a 2D list, where each 
#          element of the list is a sub-list that contains nodes in same level
# Description: DFS while tracking node level. Create a helper function, that take a [node], its [level], and a 2D list [res] as parameters.
#              Initally, the [node] is [root] and [level] is 0 since [root] is at depth 0. If len(res)<=level, means the current [node] comes from
#              a new [level], and need to create a new sub-list in [res] to hold nodes from new level. Always append current [node] to res[level],
#              and recursive invoke helper function on [node.left] and [node.right], with [level+1]. If [node] is None, means current path reach 
#              end, end current traversal by returning
# Time complexity: O(N)
def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    levelOrder_helper(root, 0, res)
    return res  

def levelOrder_helper(root, level, res):
    if not root:                            # current path reach end
        return
    if len(res)<=level:                         # hits new level, add new sub-list to hold nodes from new level
        res.append([])
    res[level].append(root.val)                     # add current [node] to corresponding level in [res]
    levelOrder_helper(root.left, level+1, res)          # recursive invoke on child nodes
    levelOrder_helper(root.right, level+1, res)            

# 60.103 Binary Tree Zigzag Level Order Traversal ============================ https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Problem: Given a [root] of binary tree, return the "zig-zag" level order traversal. Return node values in a 2D list, where each 
#          element of the list is a sub-list that contains nodes in same level
#          Ex:           directions      res
#                3         ->          [[3],[20,9],[15,7]]
#             /   \                     
#            9     20      <-
#                /   \
#               15    7    ->
# Descrpiton: DFS while tracking [level]. Create a helper function, that takes [node], and 2D list [res] as parameter. Initially, the [node] is [root]
#             and [level] is zero. Use "deque" to hold node of each level. If len(res)<=level, means the current [node] comes from a new [level], and 
#             need to create a new "deque" to hold it. For even [level], "zig-zag" from left to right, append [node.val] to end of deque res[level]. 
#             For odd [level], "zig-zag" from right to left, prepend [node.val] to beginning of deque res[level]. 
#             At last, convert deque to list then return [res]
from collections import deque
def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    def helper(root, level, res: List[deque]):
        if not root:
            return
        if len(res)<=level:                 # hits new level, expand [res] with a new deque
            res.append(deque())
        if level%2==0:                          # even [level] zig-zag from left to right
            res[level].append(root.val)
        else:                                   # odd [level] zig-zag from right to left
            res[level].appendleft(root.val)
        helper(root.left, level+1, res)
        helper(root.right, level+1, res)
    res = []
    helper(root, 0, res)
    return [list(deq) for deq in res]           # convert deques in [res] to list then return

# 61.105 Construct Binary Tree from Preorder and Inorder Traversal ========= https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Problem: Given two lists that prepresent the "preorder" and "inorder" traversal of same binary tree. Construct the binary tree, and return its root.
#          Both [preorder] and [inorder] consist of unique values
# Descrption: The first element of [preorder] is always the "root", and nodes in left-subtree always come before nodes in right-subtree in [preorder].
#             Find index of preorder[0] in [inorder], the elements comes before preorder[0] belong to left-subtree of "root", elements comes after preorder[0] belong 
#             to right-subtree of "root". Leverage this property, each recursive call retrieve preorder[0], create a "TreeNode" with value=preorder[0]. Find [index] of 
#             preoreder[0] in [inorder], since nodes of left-subtree comes first, then preorder[1:index] are nodes in left-subtree, and preorder[index+1:] are nodes
#             in right-subtree. Similarly, inorder[:index] are left-subtree and inorder[index+1:] are right-subtree. Pass partitions of [preorder] and [inorder] to 
#             build children of current [root]
# Time complexity: O(n^2), [index] look up is linear, and [n] level of recursive
def buildTreePre(preorder: List[int], inorder: List[int]) -> TreeNode:        
    if preorder:
        index = inorder.index(preorder[0])              # find index of preorder[0] in [inorder]
        node = TreeNode(val=preorder[0])                # create current [root] with preorder[0]
        # recursively build children of current [root]
        node.left = buildTree(preorder[1:index+1], inorder[:index])         # preorder[1:index+1] and inorder[:index] contains nodes in left-subtree
        node.right = buildTree(preorder[index+1:], inorder[index+1:])       # preorder[index+1:] and inorder[index+1:] contains nodes in right-subtree
        return node
    # when [preorder] is empty, means path hits end, thus return None
    return None

# Descrption: Maintain a Dictionary of inorder elements and their indices "{inorder[i]:i}" for quick preorder[0] index look up. Use [pre_beg], [pre_end],
#             [in_beg], [in_end] to specify the range of [preorder] and [inorder] to be passed to next recursive call. Borrow same idea of previous,
#             The first element of [preorder] is the "root", find index of preorder[0] in [inorder], denote as [ind]. Current "root" is preorder[0].
#             inorder[in_beg:ind] are node of left-subtree, inorder[ind+1:in_end] are nodes in right-subtree. And we know the number of nodes in left-subtree
#             is "[ind]-[in_beg]". Thus, sublist of [inorder] for left subtree is from [in_beg] to [ind], and for right subtree is from [ind+1] to [in_end]. 
#             sublist of [preorder] for left subtree is from [pre_beg]+1 to [pre_beg]+1+[ind]-[in_beg], sublist for right subtree is fronm [pre_beg]+1+[ind]-[in_beg] 
#             to [pre_end]. 
# Time complexity: O(n), [ind] look up is constant
def buildTreePre_2(preorder: List[int], inorder: List[int]) -> TreeNode:   
    def helper(pre_beg, pre_end, in_beg, in_end):
        if pre_beg<pre_end:                                     # [pre_beg]>=[pre_end] means 
            ind = dic[preorder[pre_beg]]
            root = TreeNode(preorder[pre_beg])
            root.left = helper(pre_beg+1, pre_beg+1+ind-in_beg, in_beg, ind)        # pass sublist to build left subtree
            root.right = helper(pre_beg+1+ind-in_beg, pre_end, ind+1, in_end)       # pass sublist to build right subtree
            return root
        return None
            
    dic = {num:i for i, num in enumerate(inorder)}          # create an "index" loop up dictionary for [inorder]
    return helper(0, len(preorder), 0, len(inorder))

# 62.106 Construct Binary Tree from Inorder and Postorder Traversal ======= https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Problem: Given two list [inorder] and [postorder] representing "inorder" and "postorder" traversal of a binary tree. Construct the binray tree and return its root
# Description: "inorder" traversal is left-root-right, "postorder" traversal is left-right-root. Thus, the "root" is always the last element of "postorder". And in 
#              "inorder", nodes of left-subtree are on the left-side of "root", nodes of right-subtree are on right-side of "root".Each recursive call, we can get
#              "root" from "postorder", and from "inorder" we know the number of nodes in left-subtree and right-subtree. Then for "inorder" and "postorder" lists 
#              we can divide them into two parts that contains left/right-subtree respectively. 
#              Maintain a dictionary that map "postorder" values and indices {postorder[i]:i} for quick index look up. Maintain indices [post_beg], [post_end], 
#              [in_beg] and [in_end] that specify the list range of [postorder] and [inorder] list in current recursive level
# Time complexity: O(n)
def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    def helper(in_beg, in_end, post_beg, post_end):
        if post_beg >= post_end: 
            return None
        ind = dic[postorder[post_end-1]]
        root = TreeNode(postorder[post_end-1])
        root.left = helper(in_beg, ind, post_beg, post_beg+ind-in_beg)
        root.right = helper(ind+1, in_end, post_beg+ind-in_beg, post_end-1)
        return root
    dic = {num:i for i, num in enumerate(inorder)}
    return helper(0, len(inorder), 0, len(postorder))

# 63.107 Binary tree level order traversal II =================================== URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Problem: Bottom-up level order traversal, given a root of a binary tree, return a 2D list where nodes of same level are wrapped in same sub-list,
#          and highest level is at the beginning of the list, root is at the end of the list.
# Description: DFS with [level] count. Use a helper function, which tracks [level] as the "depth" of current node. Maintain [res] as 2D result list, where
#              "i"th element contains nodes at "i"th depth. Return reversed [res] at the end as "bottom-up" level order traversal.
#              Initally, helper function takes [root] as starting node, [level] = 0, and [res] is an empty list
#              In helper function. if len(res)<=level, means a new level is hit and need to create a new sub-list in [res] to hold nodes of new level.
#              Add current [node] to its corresponding level res[level].append(node.val). Then invoke helper function on [node.left] and [node.right]
#              with [level+1]. If current [node] is None, then stop current path by returning
# Time Complexity: O(n)
def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    res = []
    levelOrderBottom_helper(root, 0, res)
    return res[::-1]

def levelOrderBottom_helper(root, level, res):
    if not root:                # hit None, end current path
        return
    if len(res)<=level:             # a new level is hit, add new sub-list to hold nodes from new level
        res.append([])
    res[level].append(root.val)         # add current node to corresponding level
    levelOrderBottom_helper(root.left, level+1, res)            # invoke function on child nodes
    levelOrderBottom_helper(root.right, level+1, res)

# 64.109 Convert Sorted List to Binary Search Tree ================================ https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# problem: Given the [head] of a linked list, whose nodes are sorted in ascending order. Convert it to a height balanced BST, and return the root.
# Description: Recursive. Use two pointer [slow] and [fast] to find the middle node [mid], [slow] starts from [head] and [fast] starts from [head.next.next]. 
#              Traverse [slow] and [fast] towards tail, [slow] moves a node at a time, [fast] moves two nodes at a time. When [fast] or [fast.next] reach end, 
#              [slow.next] is [mid]. Use [mid] to make [root] of current recursion, and nodes between [head] and [slow] is the sublist that belongs to 
#              left-subtree, and nodes from [mid.next] to end is the sublist that belongs to right-subtree. Break the connect between [slow] and [mid] to 
#              separate left and right sublist.
# Time compexity: O(NlogN), O(N) to build node for a level, there are O(logN) levels
def sortedListToBST(head: ListNode) -> TreeNode:
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    slow, fast = head, head.next.next               # use [slow] and [fast] to search for [mid]
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid = slow.next
    slow.next = None                                # break connection between left and right sublist
    root = TreeNode(mid.val)
    root.left = sortedListToBST(head)               # build left subtree with nodes from [head] to [slow]
    root.right = sortedListToBST(mid.next)          # build right subtree with nodes from [mid.next] to end
    return root       

# 65.113 Path Sum II =========================================================================================== https://leetcode.com/problems/path-sum-ii/
# Problem: Given the [root] of a binary tree and an integer [targetSum]. Return all "root-to-leaf" path that the nodes along the path sum up to [targetSum]
#          Return the result as 2D list, where each element consists of nodes in a path
# Description: DFS. Implement a helper function, that maintain [res] as the result 2D list, maintain [temp] that consists nodes along a path, maintain 
#              [targetSum] representing the remaining sum after subtracting node values in [temp], and the current node [root]
#              If current node [root] is a leaf that has not child, and [targetSum]==[root.val], meaning a path is found then append [temp] to [res]. If
#              [root] hit end of path, means this path doesn't qualify, stop current recursion by returning. Each recursion, reduce [targetSum] by [root.val]
#              and append [root.val] to [temp], then search both [root.left] and [root.right] subtrees.
def pathSum2(root: TreeNode, targetSum: int) -> List[List[int]]:
    def helper(root, temp, targetSum, res):
        if not root:                        # DFS hit end, stop current DFS
            return
        if not root.left and not root.right:        # hit leaf
            if root.val == targetSum:                   # qualified path is found. append [temp] to [res]
                temp.append(root.val)
                res.append(temp)
                return
            else:
                return
        helper(root.left, temp+[root.val], targetSum-root.val, res)     # recursion on left child
        helper(root.right, temp+[root.val], targetSum-root.val, res)    # recursion on right child
    res = []
    helper(root, [], targetSum, res)
    return res

# 66.114 Flatten Binary Tree to Linked List ===================================== https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Problem: Given [root] of a binary tree, flatten it to a linked list. The linked list use [root] as its "head", and "right" child points to next
#          node, and "left" node is set to None. The linked list follow "pre-order" traversal order. (root-left-right)
# Description: Post-order traversal and a global variable [prev] tracking previous node to connect with. Use "post-order" traversal to construct 
#              the linked list from right to left. [prev] is the head of previously created linked list, and need to be appended to the [right] of current 
#              node. After traverse [left] and [right] of a node, connect [prev] to [right] of current node, set [left] to None and update [prev] to
#              current node, since current node is the new head of previously created linked list
class FlattenBinaryTree:
    def __init__(self):
        self.prev = None                # tracking the head of previously created linked list
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        # "post-order" traverse
        self.flatten(root.right)        
        self.flatten(root.left)
        root.right = self.prev          # append previously created linked list to current node
        root.left = None                # set its [left] to None
        self.prev = root                # update [prev] to current node

# 67.116 Populating Next Right Pointers in Each Node ==================== https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Problem: Given the [root] of a "perfect binary tree", where all leaves are on the same level. And every non-leaf node has two childen. The node
#          has reference to "left", "right" and "next", as following
#          struct Node {
#               int val;
#               Node *left;
#               Node *right;
#               Node *next; 
#          }
#          Populate each next pointer to point to its next right node. If there is no right node, then points to None
# Description: DFS. For a [node]. [node.left] connects to [node.right], and [node.right] connect to [node.next.left].
#                       node ----------> node.next --> None
#                       /  \              /    \
#                   left -> right ---> left --> right --> None
#              Recursivly call on [node.left] and [node.right] to build next level. If [node] is None, return to stop
def connect(root: 'Node') -> 'Node':
    if not root:
        return
    if root.left:                               # connect [left] to [right]
        root.left.next = root.right
    if root.right:                              # connect [right] to [node.next.left]
        root.right.next = root.next.left if root.next else None
    connect(root.left)
    connect(root.right)
    return root

# 68.117 Populating Next Right Pointers in Each Node II ============= https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Problem: Given the [root] of a bianry tree, where the tree may not be "perfect binary tree". Populate each next pointer to point to its next 
#          node on right. If there is no next-right node, point the next point to None.. The node has references to "left", "right", and "next":
#               struct Node {
#                   int val;
#                   Node *left;
#                   Node *right;
#                   Node *next; 
#               }
# Description: Maintian [prev] as node in previous level that [prev.left] and [prev.right] are nodes in current level. [dummy] refers to the "head"
#              node of current level, where [dummy.next] is the first node on current level. [cur] refers to the current node, that is used to 
#              connect "next-right" node. 
#              Start with [prev] at [root]. And traverse though each level, [dummy] and [cur] start from first node of next level. Assign [prev.left]  
#              and [prev.right] to [cur.next] if they exists. Update [prev] to [prev.next] and update [cur] to [cur.next] to build tree horizontally.
#              When [prev] hits None, means traverse of current level is finished. Start traverse next level, update [prev] with [dummy.next].
#              If [prev] is still None after updating, means the entire traversal is finished. 
def connect(self, root: 'Node') -> 'Node':
    prev = root
    while prev:                         # build completed if outter [prev] is None
        cur = dummy = Node(0)               # [dummy] track first node of current level
        # traverse and build current level
        while prev:
            if prev.left:
                cur.next = prev.left
                cur = cur.next
            if prev.right:
                cur.next = prev.right
                cur = cur.next
            prev = prev.next                # move [prev] horizontally to continue build current level
        prev = dummy.next               # move [prev] to the beginning of next level
    return root

# 69.129 Sum Root to Leaf Numbers ==================================================== https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Problem: Given a [root] of binary tree, where nodes in the tree can only contain value from 0 to 9. Each path from root to leaf represents
#          a number, where value of root is highest digit and value of leaf is the lowest digit. Ex, a path 1 -> 2 -> 3 represents number 123
#          Return the total sum of all root-to-leaf path. A leaf node is a node without any child
# Description: DFS, maintain [cur] as the current sum along the path. Each resursive call, [cur] is multiplied by 10 and added with [root.val],
#              [cur] = [cur]*10+[root.val]. If [root.left] or [root.right] exists, DFS on [root.left] and [root.right] with updated [cur].
#              When [root] is a leaf, aka, [root.left] and [root.right] are None. Add [cur] into [res], that [res] = [cur]*10+[root.val]. Return
#              [res] at the end
def sumNumbers(root: Optional[TreeNode]) -> int:
    def helper(root, cur, res):
        if not root.left and not root.right:            # hit leaf, add [cur] into [res]
            res[0] += (cur*10)+root.val
            return
        # DFS on left and right child, [cur] is updated
        if root.left:                                   
            helper(root.left, cur*10+root.val, res)
        if root.right:
            helper(root.right, cur*10+root.val, res)
    res = [0]               # [res] is a list, that is passed by reference
    helper(root, 0, res)
    return res[0]

# 70.130 Surrounded Regions ================================================================ https://leetcode.com/problems/surrounded-regions/
# Problem: Given a m*n matrix [board] contains "X" and "O", capture regions of "O" that are 4-direction surrounded by "X", and "O" into "X"
#          Surrounded regions should not be on the border, that "O"s on border is not converted to "X"
#          Ex:
#          X X X X          X X X X
#          X O O X   ===>   X X X X 
#          X X O X          X X X X
#          X O X X          X O X X
# Description: If a "O" is no connect with border, it need to be converted. Use DFS to find the "O" on border and convert it to a temporary 
#              character. Then iterate through [board] convert remaining "O"s to "X", since they are not connected to boarder.
# Time complexity: O(n), n = m*n
def solve(board: List[List[str]]) -> None:
    def dfs(row, col):
        # convert "O" to "." if it is connected to border
        if 0<=row<len(board) and 0<=col<len(board[row]) and board[row][col] == "O":
            board[row][col] = "."
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
    for r in [0, len(board)-1]:         # dfs on first and last row
        for c in range(len(board[r])):
            dfs(r, c)
    for r in range(len(board)):         # dfs on first and last column
        for c in [0, len(board[r])-1]:
            dfs(r, c)
    for r in range(len(board)):         # convert remaining "O" to "X" and revert "." to "O"
        for c in range(len(board[r])):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == ".":
                board[r][c] = "O"

# 71.131 Palindrome Partitioning =================================================== https://leetcode.com/problems/palindrome-partitioning/
# Problem: Given a string [s], find all possible ways to partition the string, so that each substring is a palindrome.
# Description: DFS backtracking. Backtrack through substring of [s], if s[:i] is a palindrome, then add s[:i] to [temp] list and continue
#              backtracking on the rest of substring s[i:]. If not more character left in [s], add [temp] to [res] list. 
#              To check palindrome, use s[:i] == s[:i][::-1]. 
#              And [i] should start from 1 to len(s)+1, since s[:i] should start from s[:1]
# Time complexity: O(2^n) worst case when all characters are same in [s]
def partition(s: str) -> List[List[str]]:
    def helper(s, temp, res):
        if not s:
            res.append(temp)
        for i in range(1,len(s)+1):             # backtracking on every character from i=1 to i=len+1
            if s[:i][::-1] == s[:i]:                    # check palindrome
                helper(s[i:], temp+[s[:i]], res)        # append palindrome to [temp] then backtrack on rest of string
    res =[]
    helper(s, [], res)
    return res

# 72.133 Clone graph ========================================================================= https://leetcode.com/problems/clone-graph/
# Problem: Given a reference of a [node] in a connected graph. Deep copy the entire graph and return to cooresponding node of [node] in 
#          copied graph. Definition of graph node is as follow
#          class GraphNode:
#               def __init__(self, val=0, neighbors=[]):
#                   self.val = val
#                   self.neighbors = []
# Description: DFS. Maintain a dictionary that keys are node of original graph, and values are cloned node in new graph. While DFS through
#              original graph, for every [neigh] of [node.neighbors]. If [neigh] is in dictionary, means [neigh] is already cloned, but
#              still need to be appended to the cloned [node.neighbors]. If [neigh] is not in didctionary, then create a new node with same
#              value and insert it to dictionary, and append it to the cloned [node.neighbors]. 
#              Initally, dictionary contains the "root" [node] and its cloned node, and DFS from there
# Time complexity: O(V+E) iterate through vertices and edges
def cloneGraph(node: 'GraphNode') -> 'Node':
    def helper(node: 'GraphNode', dic: dict):
        for neigh in node.neighbors:
            if neigh not in dic:                    # if [neigh] is not cloned
                dic[neigh] = GraphNode(neigh.val)       # clone [neigh], and save it in dictionary
                helper(neigh, dic)                      # DFS on [neigh]
            dic[node].neighbors.append(dic[neigh])  # always connect cloned [neigh] with cloned [node]
    
    if not node:
        return None
    dic = {node: GraphNode(node.val)}   # initially start with [node]
    helper(node, dic)
    return dic[node]                # return cloned [node]

# 73.134 Gas Station ========================================================================= https://leetcode.com/problems/gas-station/
# Problem: Given two integer arrays [gas] and [cost], where elements in [gas] represent the amount of gas a car can refill at certain index
#          [i] and elements in [cost] represent the amount of gas cost to move from current index [i] to next index [i+1]. Assume indeices 
#          form a circle that the car can move from last index to first index. Find and return the starting index that the car has enough 
#          gas to travel all indecies, return -1 if the car can't travel the circle
# Description: The only way the the car can not travel the cirle is when total amount of gas is less than total cost sum(gas)<sum(cost).
#              Check it and return -1, otherwise there always exists a starting index. 
#              Greedy. traverse through [gas] and [cost] from index 0 to end, calculate the accumulate remaining gas at each index. Find 
#              the index with lowest remaining gas, the index next to the lowest is the answer. 
# Time complexity: O(n)
def canCompleteCircuit(gas, cost):
    if sum(gas)<sum(cost):
        return -1
    remain, index, lowest = 0, 0, float('inf')
    for i in range(len(gas)):           # search for index with lowest [remain]
        remain += gas[i]-cost[i]
        if lowest >= remain:
            lowest, index = remain, i
    return (index+1)%len(gas)           # return the next index of [lowest]

# 74.137 Single Number II ===================================================================== https://leetcode.com/problems/single-number-ii/
# Problem: Given a list of integer [nums], where every element appear three times except for one element only appear once. Find and return the 
#          single number in O(n) time complexity and use O(1) space
# Description: Bitwise solution. If a number appear three times, for each bit of these number, they must sum up to either 3 or 0. Thus, sum up 
#              all numbers in [nums] and modulo 3, the remaining must be the bit of the single number. Do the same from bit 0 to 32, we have
#              the bitwise of the single number. 
#              In case the single number is negative (2's complement), if the [res] is larger than (1<<31), [res] is negative. Use [res]-(1<<32)
#              to get 2's complement of [res]
# Time complexity: O(n)
# Space complexity: O(1)
def singleNumber(nums: List[int]) -> int:
    res = 0
    for i in range(32):
        cnt = 0
        for n in nums:
            if n & (1<<i) == (1<<i):            # increate [cnt] if [i]th bit of [n] is 1
                cnt += 1
        res |= (cnt%3)<<i                       # extract the single bit
    return res if res<(1<<31) else res-(1<<32)      # check negativity before returning