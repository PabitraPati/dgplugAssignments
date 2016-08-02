###############################################################
'''
Take  any log from the top of https://dgplug.org/irclogs/2016/  and 
then for a given line number try to find who spoke that line.

Like: 1 <kushal> now let's see
      ...
      34 <avik> spoke to gkadam on this

you need to find :- 'avik' spoke in line 34
'''
##############################################################

def find_who_spoke(line_no):
    content = ''
    with open('log1.txt', 'r') as f:
        content += f.read()

    di = {}
    lines= content.split('\n')
    count = 0

    for line in lines:
        count += 1
        if '<' in line:
            nick = ((line.split('<')[1]).split('>'))[0]
            di[count]=di.get(count, nick)
    print ("%s spoke in line %d" %(di[line_no], line_no)) if line_no in di else print ("Invalid line number entered")

line_no = input("Enter line number you want to find who spoke :-  ")
find_who_spoke(int(line_no))
