def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = int("".join(map(str, digits)))
        res += 1
        array = [int(x) for x in str(res)]
        return array

print(plusOne([1,2,3]))