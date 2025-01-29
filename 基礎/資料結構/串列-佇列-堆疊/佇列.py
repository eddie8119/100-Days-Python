# 先進先出
# Python 中使用 collections.deque 實現

from collections import deque
queue = deque()
queue.append(1)     
queue.append(2)
queue.popleft()    # 移除最先加入的元素