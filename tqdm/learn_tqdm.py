from tqdm import tqdm

for i in tqdm(range(1000)):
    # do something
    pass

for char in tqdm(["a", "b", "c", "d"]):
    # do something
    pass

from tqdm import trange

for i in trange(100):
    # do something
    pass

bar = tqdm(["a", "b", "c", "d"])
for char in bar:
    bar.set_description("Processing %s" % char)
