# Using any to check at lease one conditions is fulfilled
subs, likes, comments = 2400, 20, 78
conditions = [subs > 100, likes > 100, comments > 80]

if any(conditions):
    print('Awesome youtube video')
