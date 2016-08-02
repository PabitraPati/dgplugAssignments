###############################################################
'''
Take the 4 logs from the top of https://dgplug.org/irclogs/2016/  and 
then try to find for each nick ever present in those files, 
who spoke with whom highest number of times.

Like: kushal spoke to avik 35 times
      avik spoke to gkadam 55 times

and like that, for all the nicks.
'''
##############################################################

content = ''
with open('log1.txt','r') as f:
    content += f.read()

with open('log2.txt','r') as f:
    content += '\n'+ f.read()

with open('log3.txt','r') as f:
    content += '\n' + f.read()

with open('log4.txt','r') as f:
    content += '\n' +f.read()

nicks = []
dict = {}
lines= content.split('\n')
# find all the nicks
nicks = list(set([((line.split('<')[1]).split('>')[0]) for line in lines  if '<' in line ]))

dict = {nick:{} for nick in nicks}
# Now find conversation
for line in lines:
    if '<' in line:
        s = ((line.split('<')[1]).split('>'))
        nick, msg = s[0],s[1]
        nicks_from_msg = [nick for nick in nicks if nick in msg]
        for n in nicks_from_msg:
            dict[nick][n]=dict[nick].get(n,0)+1  
   
for k,v in dict.items():
    max =0
    name = ''
    for k1,v1 in dict[k].items():
        (name,max) = (k1,v1) if max< v1 else (name,max)
    print("%s has no converstaion with anyone" %(k)) if (name,max) == ('',0) else print ("%s has maximum number of converstaion with %s for %d times" %(k,name, max) ) 

