# # s = "()[]{}"
# # s = "{[()]}"
# # stack = []
# # dict = {")": "(", "]": "[", "}": "{"}
# # def isValid():
# #     for char in s:
# #         if char not in dict.keys():
# #             stack.append(char)
# #         else:
# #             stack.remove(dict[char])
# #     if stack:
# #         return False
# #     else:
# #         return True
# # print(isValid())
# # a = [1,2,3]
# # print(a[:len(a)])
# def mm():
#     s = ["h","e","l","l","o"]
#     le = len(s)
#     for i in range(le):
#         s = s[:i]+[s[-1]]+s[i:le-1]
#     return s
# # print(mm())
# s = "A man, a plan, a canal: Panama"
# b = ""
# for i in s:
#     if i.isalnum():
#         b+= i.lower()
# print()

# def aa():
#     s = "abcaa"
#     l = 0
#     r = len(s) - 1
#     while l<r:
#         if s[l] == s[r]:
#             l +=1
#             r -=1
#         else:
#             if l%2 != 0:
#                 print(l,r)
#                 s = s[:l]+s[-r:]
#                 print(s)
#                 return s == s[::-1]
#             else:
#                 print(l,r)
#                 s = s[:l]+s[-r:]
#                 print(s)
                
#                 return s==s[::-1]
#     return s==s[::-1]
        
# print(aa())
# def aa():
#         s ="ccbbc"
#         l = 0
#         r = len(s) - 1
#         while l<r:
#             if s[l] == s[r]:
#                 l +=1
#                 r -=1
#             else:
#                 t = s[:l]+s[l+1:]
#                 if t == t[::-1]:
#                     s = s[:l]+s[l+1:]
#                     # print(s)
#                     # print(s)
#                     return s == s[::-1]
#                 else:
#                     s = s[:r]+s[r+1:]
#                     print(l,r)
#                     print(s)
#                     return s == s[::-1]

#         return s==s[::-1]
# print(aa())
# l = 1
# s = 'ccbbc'
# s = s[:l]+s[l+1:]
# print(s)


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s) - 1
#         while l<r:
#             if s[l] == s[r]:
#                 l +=1
#                 r -=1
#             else:
#                 t = s[:l]+s[l+1:]
#                 if t == t[::-1]:
#                     return True
#                 else:
#                     s = s[:r]+s[r+1:]
#                     return s == s[::-1]

#         return s==s[::-1]

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s) - 1
#         def cheak(s,l,r):
#             while l<r:
#                 if s[l] != s[r]:
#                     return False
#                 l+=1
#                 r-=1
#             return True
#         while l<r:
#             if s[l] == s[r]:
#                 l+=1
#                 r-=1
#             else:
#                 return cheak(s,l+1,r) or cheak(s,l,r-1)
#         return True