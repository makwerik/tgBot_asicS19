<h1>Телеграм бот для просмотра актуального состояния по asic S19</h1>
<h2>Возможности : </h2>
<p>Просмотр состояния кулеров</p>
<p>Просмотр температуры чипов</p>
<p>Просмотр температуры плат</p>

<h3>Настройка :</h3>
<h3> Для auth.json: </h3>
<p> - После авторизации на локальном сервере асика, жмем F12 > Сеть > Fetch/XHR > забираем из заголовка запроса "Authorization" > помещаем данные в data/auth.json</p>
<h3> Для config.yaml: </h3>
<p> - "token": 'Сюда помещаем токен вашего бота в тг'.</p>
<p> - "url": 'Сюда помещаем ваш локальный адрес асика например: (192.168.0.40)</p>
<h3>Terminal</h3>
<code>pip install -r requirements.txt</code>
<code> python main.py</code>