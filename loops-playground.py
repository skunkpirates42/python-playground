# will print 0 - 9
for x in range(10):
  print(x)

# will print 1-10
for x in range(1, 11):
  print(x)

# We can print each letter in a string by writing the following
greet = 'hello'
for x in range(len(greet)):
  print(x)

for x in (greet):
  print(x)
print(greet)

# We can do stuff with strings in a list too
words = ['cat', 'window', 'defenestrate']
for w in words:
  print(w, len(w))