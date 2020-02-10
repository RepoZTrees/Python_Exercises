"""
Input: "A man, a plan, a canal: Panama"
Output: True

"""

sentence = "A man, a plan, a canal: Panama"
new_sentence = sentence.replace(':','')
remove_commas = new_sentence.replace(',','')
remove_space = remove_commas.replace(' ','')
lower_case_sentence = remove_space.lower()
print(new_sentence)
print(remove_commas)
print(remove_space)
print(lower_case_sentence)

pal_sentence =[]
def palindrome():
    for i in lower_case_sentence:
        pal_sentence.append(i)
    pal_sentence.reverse()
    join_sentence = ''.join(pal_sentence)
    
    if join_sentence == lower_case_sentence:
        return True
    else:
        return False
    
p = palindrome()
print(p)
