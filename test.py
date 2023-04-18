import re
str = "You were sent $1 from <a href = http://www.torn.com/profiles.php?XID=2801163>Aries0N</a> with the message: test"
string=re.sub("\<.*?\>","()",str)
string=string.replace('(','')
string=string.replace(')','')
print(string)