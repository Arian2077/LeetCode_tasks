class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        lst_s1 = sentence1.split()
        lst_s2 = sentence2.split()
        
        while lst_s1 and lst_s2 and lst_s1[0] == lst_s2[0]:
            lst_s1.pop(0)
            lst_s2.pop(0)
        while lst_s1 and lst_s2 and lst_s1[-1] == lst_s2[-1]:
            lst_s1.pop()
            lst_s2.pop()
        print(lst_s1)
        print(lst_s2)
        if lst_s1 == [] or lst_s2 == []:
            return True
        return False

sentence1 = "qbaVXO Msgr aEWD v ekcb"
sentence2 = "Msgr aEWD ekcb"
solution = Solution()
solution.areSentencesSimilar(sentence1, sentence2)
