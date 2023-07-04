import time
def count_sym(line):
    for sym in set(line):
        counter = 0
        for sub_sym in line:
            if sym == sub_sym:
                counter += 1
    print(sym, counter)

start = time.time()

count_sym('gdhjjttjtr' * 1000000)

end = time.time()

print("Время пыполнения программы:", end - start)