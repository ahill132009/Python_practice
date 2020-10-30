from collections import Counter
from collections import defaultdict
import string

latin_characters = string.ascii_lowercase

# Make with defaultdict
dd = defaultdict(int)
for ltr in latin_characters:
	dd[ltr] = 0

string = str(input('Write any string: '))
for x in string:
	dd[x] += 1

itog = []
for ltr, n in dd.items():
	itog.extend([ltr*n])

print(''.join(itog))


# Make with Counter
c = Counter()
for ltr in latin_characters:
	c[ltr] = 0

string = str(input('Write any string: '))
for x in string:
	c[x] += 1

print(''.join(list(c.elements())))