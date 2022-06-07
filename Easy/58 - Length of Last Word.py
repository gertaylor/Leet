def lengthOfLastWord( s):
        """
        :type s: str
        :rtype: int
        """
        result= s.split(" ")
        str_list = list(filter(None, result))
        return len(str_list[-1])

print(lengthOfLastWord("   fly me   to   the moon  "))