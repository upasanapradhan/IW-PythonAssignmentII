def conv(my_string, seperator):
    var = [my_string[0].lower()]
    for x in my_string[1:]:
        if x in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            var.append(seperator)
            var.append(x.lower())
        else:
            var.append(x)
    return ''.join(var)


my_string = 'ThisIsCamelCased'
print(conv(my_string, '_'))
print(conv(my_string, '-'))