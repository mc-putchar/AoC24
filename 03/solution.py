import re

def read(file):
    memory = ""
    with open(file, 'r') as f:
        memory = f.read().replace('\n', '')
    return memory

def find_muls(input):
    muls = re.findall(r"mul\(\d+,\d+\)", input)
    return muls

def find_cond_muls(input):
    cond = re.sub(r"don\'t\(\).*?do\(\)", "NOP", input)
    #print(f'EXT:\n{cond}')
    donts = re.sub(r"don\'t\(\).*", "NOP", cond)
    #print(f'\nIGNORE=====\n{donts}')
    muls = re.findall(r"mul\(\d+,\d+\)", donts)
    return muls

def main():
    mem = read("input")
    muls = find_muls(mem)
    result = 0
    for mul in muls:
        nums = re.findall(r'\d+', mul)
        result += int(nums[0]) * int(nums[1])
    print(result)
    muls = find_cond_muls(mem)
    result = 0
    for mul in muls:
        nums = re.findall(r'\d+', mul)
        result += int(nums[0]) * int(nums[1])
    print(result)

if __name__ == "__main__":
    main()
