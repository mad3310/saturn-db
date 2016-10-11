saturn-db
=========

---
saturn-db是数据库系统包，包含了一些常用的方法。


# 获取配置上下文


```python
app = 'saturn'
from saturn.db.store.context import init_context
from saturn.db.store import SqlStore

# 库会从环境变量中以app大写开头的环境变量中读取配置
# 如果app='saturn'
# 则会读取SATURN_XXXXX_XXX环境变量

context = init_context(app)
db = SqlStore.init_by_context(context)

# Context也可以自己创建，但一般不需要：

context = SQLContext(APP='saturn',
                     DEVELOP_MODE=DEVELOP_MODE,
                     DB_HOST=DB_HOST,
                     DB_PORT=DB_PORT,
                     DB_USER=DB_USER,
                     DB_PASSWD=DB_PASSWD,
                     DB_NAME=DB_NAME,
                     READ_SOURCE=READ_SOURCE
                     )

db = SqlStore.init_by_context(context)
```
