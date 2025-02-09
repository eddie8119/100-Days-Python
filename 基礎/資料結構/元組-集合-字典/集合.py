# 去重 
# 無順序性 沒有索引值 沒有切片


empty_set = set()              # 空集合
numbers = {1, 2, 3, 4, 5}      # 使用大括號
from_list = set([1, 2, 2, 3])  # 從串列轉換，重複元素會被移除

# 基本操作
set1 = {1, 2, 3}
set1.add(4)          # 新增元素
set1.remove(2)       # 移除元素（如果不存在會報錯）
set1.discard(5)      # 移除元素（如果不存在不會報錯）
set1.pop()           # 隨機移除一個元素
set1.clear()         # 清空集合



# 無法串列-集合-字典
# 為什麼集合不能add() 串列 集合 但可以新增元組

# 集合的一個重要特性：集合只能包含「可雜湊」(hashable)的元素
    # 可雜湊的物件：
        # 元組 (tuple)
        # 數字 (int, float)
        # 字串 (string)
    # frozenset（不可變集合）
        # 不可雜湊的物件：
        # 串列 (list)
        # 字典 (dict)
        # 集合 (set)

# 這是可以的
my_set = set()
my_set.add((1, 2, 3))  # 元組是可雜湊的

# 這會產生錯誤
my_set.add([1, 2, 3])  # TypeError: unhashable type: 'list'
my_set.add({1, 2, 3})  # TypeError: unhashable type: 'set'

# 元組是不可變的
tuple1 = (1, 2, 3)
# tuple1[0] = 4  # 這會產生錯誤

# 串列是可變的
list1 = [1, 2, 3]
list1[0] = 4  # 這是允許的