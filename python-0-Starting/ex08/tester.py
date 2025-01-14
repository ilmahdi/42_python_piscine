from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(60)):
    sleep(0.01)
print()
# print(tqdm.__doc__)
# print(tqdm(range(21)))
for elem in tqdm(range(40)):
    sleep(0.01)
print()
