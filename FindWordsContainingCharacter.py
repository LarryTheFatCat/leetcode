class Solution(object):
    def findWordsContaining(self, words, x):
        common_pos = []
        for i in range(0,len(words)):
            if x in words[i]:
                common_pos.append(i)
        return common_pos