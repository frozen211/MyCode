word1 = "abcba"
word2 = "assess"

# quickly count the number of unique characters
mask = 0
for c in word1:
  mask |= (1 << (ord(c) - ord('a')))
# The number of "1" in the mask is the number of unique characters
print(str(bin(mask)))
print(mask.bit_count())

mask2 = 0
for c in word2:
  mask2 |= (1 << (ord(c) - ord('a')))

# use AND operation we can check if they have the same characters
print(mask & mask2)

