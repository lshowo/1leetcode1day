#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

'''test 
    "/a/./b/../../c/"\n
    "/home//foo/"\n
    "/../"\n
    "/home//foo/"\n
    "/..."\n
    "/."\n
    "/..."\n
    "/abc/..."\n
    "/a//b////c/d//././/.."\n
'''

'''
以/划分文件item
    item 为 . ：不作处理。
    item 为 .. ：弹出栈定元素
    item 为有效值 ：存入栈中；
'''

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for i in path.split('/'):
            if i not in ['', '.', '..']:
                stack.append(i)
            elif i == '..' and stack:
                stack.pop()
        return "/" + "/".join(stack)
# @lc code=end
