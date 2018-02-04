import operator

def ngrams(inputtext, n):
  		inputtext = inputtext.split()
  		output = {}
  		for i in range(len(inputtext)-n+1):
			#print(inputtext[i:i+n])
    			g = '  '.join(inputtext[i:i+n])

    			output.setdefault(g, 0)
    			output[g] += 1
			#print(output)
  		return output
open_file = open('democratic_speeches.txt','r+').read() 
d = ngrams(open_file,2)


try:
	
	with open('democratic_speeches_2_grams.txt','a+') as out_json:

		for w in sorted(d, key=d.get, reverse=True):
                    out_json.write(str(w)+": "+str(d[w])+'\n')

except KeyError:
	print ("Error")

open_file_republic = open('republican_speeches.txt','r+').read() 
r = ngrams(open_file_republic,2)


try:
	
	with open('republican_speeches_2_grams.txt','a+') as out_json:

		for z in sorted(r, key=r.get, reverse=True):
                    out_json.write(str(z)+": "+str(r[z])+'\n')

except KeyError:
	print ("Error")
