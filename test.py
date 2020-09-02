"""
このファイルに解答コードを書いてください
"""
path = 'input.txt'


# textをリストに変換
with open(path) as f:
    l_strip = [s.strip() for s in f.readlines()]

# mを抽出
m = int(l_strip[-1])

# 最後の行を取り出す
l_strip = l_strip[:-1]

# l_stripから辞書を作成 {i:s}
d = {}
for i_s in range(len(l_strip)):
    i, s = l_strip[i_s].split(':')
    i = int(i)
    d[i] = s
d2 = sorted(d)
# 答えの出力　ans
ans = ''
for i in d2:
    if m % i ==0:
        ans += d[i]

if ans == '':
    print(m)
    exit()
print(ans)