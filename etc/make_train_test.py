#!/usr/bin/env python3
import sys
import random

def main():
    random.seed(8675309)
    rand_index = None
    percent = 80

    with open(sys.argv[1], "w") as out1:
        with open(sys.argv[2], "w") as out2:
            num2 = 0
            for path in sys.argv[3:]:
                with open(path, "r") as f:
                    lines = f.readlines()
                    if rand_index is None:
                        rand_index = list(range(len(lines)))
                        random.shuffle(rand_index)
                        num2 = int(len(lines) * (percent / 100))

                    assert len(lines) == len(rand_index)
                    for i, ri in enumerate(rand_index):
                        if i < num2:
                            out1.write(lines[ri])
                        else:
                            out2.write(lines[ri])

if __name__ == "__main__":
    main()
