from itertools import zip_longest, cycle, chain,count,combinations, combinations_with_replacement, permutations,repeat

names = ['Sam', 'Nick', 'John', 'James']
names_female=['Ann', 'Kate']
surnames = ["Black", 'Smith', 'White', 'Bond']
emails = ['hi@google.com', 'bbbb@example.com', 'cat@google.com']

all_names=names+names_female
names_male_and_femail=[names,names_female]

def demo_zip():
    pairs = zip(names, surnames)
    print(list(pairs))

    # and we can separate
    names_pairs = [('Sam', 'Black'), ('Nick', 'Smith'), ('John', 'White')]
    result = list(zip(*names_pairs))
    print(result)

    result_3 = zip(names, surnames, emails)
    print(list(result_3))


def demo_zip_longest():
    collection = zip_longest(names, surnames, emails, fillvalue="")
    print(list(collection))


def demo_cycle():
    email_demo = ['a@b.com', 'c@d.com']  # 4 names in 'names' and only 2 emails, we can create infinity cycle
    pairs = zip(names, cycle(email_demo))
    print(list(pairs))
    #or
    s=cycle(email_demo)
    pairs=zip(names,s)
    print(list(pairs))

def demo_chain():
    print(names_male_and_femail)
    print(list(chain(*names_male_and_femail))) #we can join 2 collections
    print(list(chain.from_iterable(names_male_and_femail))) #same without '*'
    print(list(chain(names, names_female, surnames,emails)))

def demo_count():
    #c=count() from 0
    c=count(10,step=2)
    #print(c)
    #print(next(c))
    #print(next(c))
    #print(c)
    result=zip(chain.from_iterable(names_male_and_femail),c)
    print(list(result))

def demo_combinations():
    nums=list(range(10))
    print(nums)
    print(list(combinations(nums,2))) #only unique pairs of numbers

    print(list(combinations(names,2)))
    print(list(combinations(all_names, 3)))

def demo_combinations_with_rp():
    print(list(combinations_with_replacement(range(3),2)))


def demo_permutations():
    print(list(permutations(names,2)))
    print(list(permutations(range(3),2)))

def demo_repeat():
    c=cycle([3])
    print(list(map(pow, range(5),c)))

    #or
    r=repeat(2)
    print(list(map(pow, range(5),r)))

def main():
    demo_zip()
    demo_zip_longest()
    demo_cycle()
    demo_chain()
    demo_count()
    demo_combinations()
    demo_combinations_with_rp()
    demo_permutations()
    demo_repeat()


if __name__ == '__main__':
    main()
