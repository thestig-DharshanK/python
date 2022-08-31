import  re
print("emailid","\n")
emailid=str(input())
if(re.search("^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$",emailid)):
    print("email verified")
else:
    print("incorrect email")

#?: The preceding item is optional and matched at most once (i.e., occurs 0 or 1 times or optional).
#*: The preceding item will be matched zero or more times, i.e., 0+
#+: The preceding item will be matched one or more times, i.e., 1+
#{m}: The preceding item is matched exactly m times.
#{m,}: The preceding item is matched m or more times, i.e., m+
#{m,n}: The preceding item is matched at least m times, but not more than n times.