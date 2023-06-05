from glob import glob

files = glob('./labels/*.txt')

fruit_counter = 0
node_counter = 0
flower_counter = 0

for file in files:
    with open(file, 'r') as f:
        labels = f.read().splitlines()
        for label in labels:
            if label[0] == '0':
                fruit_counter += 1
            elif label[0] == '1':
                node_counter += 1
            elif label[0] == '2':
                flower_counter += 1

print(f'fruit: {fruit_counter}')
print(f'node: {node_counter}')
print(f'flower: {flower_counter}')
