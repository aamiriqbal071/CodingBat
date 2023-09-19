
# Your cell phone rings.
# Return true if you should answer it. Normally you answer, except in the morning you only answer if it is your mom calling.
# In all cases, if you are asleep, you do not answer.


# answerCell(false, false, false) → true
# answerCell(false, false, true) → false
# answerCell(true, false, false) → false

def answerCell(isMorning, isMom, isAsleep):
    if isAsleep:
        return False
    elif isMorning and not isMom:
        return False
    else:
        return True


print(answerCell(False, False, False))  
print(answerCell(False, False, True))   
print(answerCell(True, False, False))   

