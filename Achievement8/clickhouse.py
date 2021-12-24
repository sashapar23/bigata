import tarantool
import pandas as pd
import pandahouse as ph

# подключаемся к тарантулу
connection = tarantool.connect("localhost", 3301, user='admin', password='Test')
# сохраняем данные в переменную
tester = connection.space('mqttdata')
data = tester.select()
# панда-датафрейм
df = pd.DataFrame(data, columns=['Day', 'TickTime', 'Speed'])
# коннектимся к кликхаусу
connection = dict(database='databaseCH', user='default')
# переносим данные в него
ph.to_clickhouse(df, 'table', connection=connection, index=False)
