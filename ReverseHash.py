def reverseHash(hash):
	res = ""
	st = "acdegilmnoprstuw"
	try:
		while hash>7:
			ch = hash%37
			res = st[ch] + res
			hash = hash / 37
	except IndexError:
		return "No string can be hashed to this number"	
	if hash!=7:
		return "No string can be hashed to this number"
	else:
		return res

def hashString(s):
    h = 7
    letters = "acdegilmnoprstuw"
    for i in range(len(s)):
		h = (h * 37 + letters.index(s[i]))
    return h

def testNormalString():
	testString = "ggilmnopst"
	requiredHash = hashString(testString)
	outputString = reverseHash(requiredHash)
	assert outputString == testString

def testSingleChar():
	testString = "a"
	requiredHash = hashString(testString)
	outputString = reverseHash(requiredHash)
	assert outputString == testString

def testEmptyString():
	testString = ""
	requiredHash = hashString(testString)
	outputString = reverseHash(requiredHash)
	assert outputString == testString

def testInvalidHash():
	testString = "No string can be hashed to this number"
	requiredHash = 4567 #Any random number because it is a wrong hash.
	outputString = reverseHash(requiredHash)
	assert outputString == testString

"""
Below testcase Stores "G" 10000 times in string. This test case took about 32.5 seconds when value OF LIMIT was changed to 99999. Bigger strings will take more time
"""

def testBigString():
	testString = ""
	limit = 10000
	for i in range(limit): 
		testString+="g"
	requiredHash = hashString(testString)
	outputString = reverseHash(requiredHash)
	assert outputString == testString
