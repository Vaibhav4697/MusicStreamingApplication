import sys
import os
import tqdm
import requests
import urllib.request
import Feeders


# resolve args
def resolve_args():
    if len(sys.argv) < 2:
        print("No search keys specified")
        sys.exit(0)
    else:
        keys_list = []
        i = 1
        while i < len(sys.argv):
            keys_list.append(sys.argv[i])
            i += 1
        return keys_list


# execution flow of script
feeder = Feeders.Feeder()
keys = resolve_args()
print(keys)
print(feeder.from_yts(keys))
print(feeder.from_1337x(keys))
