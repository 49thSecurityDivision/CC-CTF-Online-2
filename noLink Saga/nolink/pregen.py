#!/usr/bin/python3
import uuid

if __name__ == '__main__':
    for x in range(2000):
        print('"' + str(uuid.uuid4()) + '",')