import pandas as pd
import tarantool
connection = tarantool.connect("localhost", 3301, user="admin", password="Test")

tester = connection.space('mqttdata')

data = tester.select()

df = pd.DataFrame(data, columns=['Day', 'TickTime', 'Speed'])

print('Median:', df.groupby(['Day'])['Speed'].median())
print('MinValue Time:', df.groupby(['Day'])['TickTime'].min())
print('MaxValue Time:', df.groupby(['Day'])['TickTime'].max())
