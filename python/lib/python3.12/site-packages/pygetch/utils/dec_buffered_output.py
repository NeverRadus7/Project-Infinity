# encoding: utf-8

DEBUG = False

def buffer_output(f):
    from functools import wraps

    # note:  f must still return SOMETHING, mind you.

    buff = []

    @wraps(f)
    def buffer_wrap(*args, **kwargs):
        if DEBUG:
            print('[called]')
            print('buffer:',buff)

        if buff:
            if DEBUG:
                print('<returning buffered output!>')
            return buff.pop(0)
        else:
            out = f(*args, **kwargs)
            assert type(out) == tuple
            if out == tuple():
                return '' # this is needed if we wrap a function not guaranteed to return anything (e.g., b/c/o timeout)
            else:
                buff.extend(list(out[1:])) # leave first to be returned
                return out[0]

    return buffer_wrap


@buffer_output
def unpredictable_IO():
    import random, string

    out = []

    while True:
        print('generated...')
        out.append(random.choice(string.printable))
        if random.randint(0,1):
            break

    return tuple(out)


if __name__ == '__main__':
    print('\ncall #1')
    print(unpredictable_IO())

    print('\ncall #2')
    print(unpredictable_IO())

    print('\ncall #3')
    print(unpredictable_IO())
