
--— Порт
box.cfg {listen = 3301}
--Пароль
box.schema.user.passwd('Test')

--— Создаем спейс
datamqtt = box.schema.create_space(
'mqttdata',
{
format = {
{name = "Day", type = 'number'},
{name = "TickTime", type = 'number'},
{name = "Speed", type = 'number'}
}, if_not_exists = true
}
)

--— Создаем индексы
datamqtt:create_index('primary',{
parts = {'Day','TickTime','Speed'}
})
datamqtt:create_index('ticktime',{
parts = {'TickTime'},
unique=false,
type='TREE'
})
datamqtt:create_index('speed',{
parts = {'Speed'},
unique=false,
type='TREE'
})

--— Загрузим модули
mqtt = require('mqtt')
json = require('json')

--— Создадим соединение
connection = mqtt.new("shaparsa", true)

connection:login_set('Hans', 'Test')

--— Коннект к серверу
connection:connect({host='194.67.112.161', port=1883})

--— Что делаем с принятым сообщением
connection:on_message(function (message_id, topic, payload, gos, retain)
print("+")
--— Принимимаем в формате json
local jsondata = json.decode(payload)
datamqtt:insert({jsondata.Day, jsondata.TickTime, jsondata.Speed})
end)

--— Подпишемся на топик по варианту
connection:subscribe('v13')