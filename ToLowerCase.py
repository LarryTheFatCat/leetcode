class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isupper():
            return s.lower()
        for letters in s:
            if letters.isupper():
                return s.lower()
        else:
            return s