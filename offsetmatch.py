import matplotlib.pyplot as plt
def countmatches(a, b):
    matches = 0
    for a_char, b_char in zip(a, b):
        if a_char == b_char:
            matches += 1
    return(matches)

def offsetmatches(a,b):
    global xvalues
    xvalues=[]
    global yvalues
    yvalues=[]
    for offset in range(30):
        xvalues.append(offset)
        yvalues.append(countmatches(a,b))
        a = '1' + a
    return offset

string1 = string2 = "VSPCWMNQEQBMVSPQSXYKOXAMXWCADIRSBEBGZMQASRECVMRAEVYZSXSPCIBNREPCDVYNEVSQSRGLDMLASHSLDIQRSEASVMQAYRQCAYYRCIKNBSGLOYGQWSBJOGRSCISBYPMPKYARYVDGXMZSCTFYCIJJEWTCVMRKKYPGCZCFSGSJKWMJVMAGDYBGXPCMOKCRFIQRSFSJEQNMBXRGDSPQOQKYEVGQZSQSOVCJYFMPDMQTORCLKXGQOXGYWEAAEQQYXTJYMIPYDWYNSILYWEJCCYYBKIJGDWMBKPCQFMRYOZGTKQSQPISESERLOUSCXSLSVXPGMMCQEPJYWGMPZIPNEVSQWMNCVPCLDIQOEICLSQCSCGCJOVGQAYCKKKLYWEQQKMLHEWRMCIBAYRQCAYYRXIAYBGSSDHYNSFSQKPGOEEKCBERTYPSRZERGXVFMXGSQVEASCEROEEKBSGRSWMKNOVBGOXLSVPYCQIRCBERTOPCPKXNPOXGSWFJYXHGRKXLMXHGYW"
offsetmatches(string1, string2)
del xvalues[0]
del yvalues[0]
#delete first values because 100% match with offset 0
plt.plot(xvalues,yvalues)
plt.xlabel('Offset')
plt.ylabel('Matches')
plt.title('Matches and offsets')
plt.show()
