# 只可讀取內容 不可以修改內容

coordinates = (10, 20, 30)
x = coordinates[0]      # 使用索引存取
last = coordinates[-1]  # 存取最後一個元素

# 切片
part = coordinates[1:3]  # 取得部分元素

# 計算長度
length = len(coordinates)

# 檢查元素是否存在
exists = 20 in coordinates  # 回傳 True

# 計數和查找
numbers = (1, 2, 2, 3, 2)
count = numbers.count(2)    # 計算特定元素出現次數
index = numbers.index(3)    # 找出元素第一次出現的索引