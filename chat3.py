
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')  #用空白去分割
    time = s[0][:5]  # 開始值0 最後一個不包含 所以是01234  
    name = s[0][5:]  # 從第五個開始走到結尾 (結尾值不寫就是走到結尾)
    print(time)
    print(name)