import re

path = "/Users/iminhyeong/Downloads/OtterCTF.vmem"

with open(path, "rb") as f:
    data = f.read()

hexData = data.hex()

pattern = re.compile(r'64([0-9a-f]{12,16})4006([0-9a-f]{36})5a0c0000')

matches = pattern.findall(hexData)

if matches:
    print(f"{len(matches)}개 발견")
    for i, m in enumerate(matches, 1):
        print(f"[{i}] {m}")
else:
    print("아무것도 발견되지 않았습니다.")
