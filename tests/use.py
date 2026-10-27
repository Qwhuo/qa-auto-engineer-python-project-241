from gendiff import generate_diff

diff = generate_diff("./d1.json", "./d2.json")
print(diff)