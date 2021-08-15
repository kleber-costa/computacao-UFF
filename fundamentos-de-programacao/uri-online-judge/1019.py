entrada = int(input())

print("%d" % (entrada // 3600), ((entrada % 3600) // 60), ((entrada % 3600) % 60), sep=':')