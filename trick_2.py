# Using all to check all the conditions
subs, likes, comments = 2400, 200, 78
conditions = [subs > 100, likes > 100, comments > 20]

if all(conditions):
    print('Awesome youtube video')
