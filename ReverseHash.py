hash = input("Enter hash\n")
res = ""
st = "acdegilmnoprstuw"
while hash>7:
	ch = hash%37
	res = st[ch] + res
	hash = hash / 37
if hash!=7:
	print "No string can be hashed to this number"
else:
	print res
