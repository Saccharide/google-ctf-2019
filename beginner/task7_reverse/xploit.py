
chrs = [106,119,113,119,49,74,172,242,216,208,339,264,344,267,743,660,893,892,1007,975,10319,10550,10503,11342,11504,12533,12741,12833,13437,13926,13893,14450,14832,15417,15505,16094,16285,16599,16758,17488]
#diff= [2,3,5,7,11,]
print(len(chrs))
chrs = [format(x,'015b') for x in chrs]
#diff = [x for x in range(2,len(chrs)+2)]
diff = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061,16361, 16561, 16661, 17471]
print(len(diff))
diff = [format(x,'015b') for x in diff]
print(len(diff[0]))
#result = [chr(chrs[i] - diff[i]) for i in range(len(chrs))]
#print("result = ", ''.join(result))
result = []
for i in range(len(chrs)):
    char = ""
    for j in range(15):
        char += str(int(chrs[i][j]) ^ int(diff[i][j]))
    result.append(char)

result_str = ""
for i in result:
    result_str += chr(int(i, 2)%256)

print(result_str)
