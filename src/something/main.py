def does_not_work():
    import src.something.test
    import src.something.new_test

    t1 = src.something.test.Test()
    t2 = src.something.new_test.NewTest()
    print(t1, t2)


def works():
    import src.something.new_test
    import src.something.test

    t1 = src.something.test.Test()
    t2 = src.something.new_test.NewTest()
    print(t1, t2)


does_not_work()
works()
