def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    for i in range(0, len(haystack)) :
        if haystack[i:i + len(needle)] == needle:
            return i
    
    return -1


print(strStr("aaaaa", "bba"))
        