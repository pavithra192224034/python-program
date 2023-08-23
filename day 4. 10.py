def isScramble(s1, s2):
    memo = {}
    
    def helper(s1, s2):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        
        if s1 == s2:
            memo[(s1, s2)] = True
            return True
        
        if sorted(s1) != sorted(s2):
            memo[(s1, s2)] = False
            return False
        
        n = len(s1)
        for i in range(1, n):
            if (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or \
               (helper(s1[:i], s2[n-i:]) and helper(s1[i:], s2[:n-i])):
                memo[(s1, s2)] = True
                return True
        
        memo[(s1, s2)] = False
        return False
    
    return helper(s1, s2)

# Example usage
s1 = "great"
s2 = "rgeat"
result = isScramble(s1, s2)
print(result)  # Output: True




