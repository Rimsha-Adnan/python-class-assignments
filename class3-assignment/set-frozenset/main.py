# Set
# set is a collection of items that are unique and unordered
# set is mutable
# set is unindexed
# set is unhashable

num = {1, 2, 3, 4, 5}
print(num)

num.add(6)
print(num)

num.remove(3)
print(num)

num.discard(1)
print(num)

num.pop()
print(num)

num.clear()
print(num)

num.update([6, 7, 8, 9, 10])
print(num)

num.union([1, 2, 3, 4, 5])
print(num)

num.intersection([1, 2, 3, 4, 5])
print(num)

num.difference([1, 2, 3, 4, 5])
print(num)

num.symmetric_difference([1, 2, 3, 4, 5])
print(num)

num.issubset([1, 2, 3, 4, 5])
print(num)

num.issuperset([1, 2, 3, 4, 5])
print(num)

num.isdisjoint([1, 2, 3, 4, 5])
print(num)

num.copy()
print(num)

# Frozen Set
# frozen set is a collection of items that are unique and unordered
# frozen set is immutable
# frozen set is unindexed
# frozen set is unhashable

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)

frozen_set.add(6)
print(frozen_set)   




















