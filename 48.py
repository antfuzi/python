alist = range(5)
it = iter(alist)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)
