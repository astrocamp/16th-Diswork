## Setup Steps 設定步驟

#### 虛擬環境:
```
$ pip install poetry
$ poetry init -n
$ poetry shell
$ poetry install
```
## Node.js
```
$ install node
$ npm init -y
$ npm run dev
```
```
$ make server
```

### 使用私人聊天設定步驟
1. 到 docker 官方下載 [docker](https://www.docker.com/) 
2. $ docker run -p 6379:6379 -d redis:7
3. 再來安裝 channels_redis，以便 Channels 與 Redis 互動。
4. python3 -m pip install channels_redis
5. 確認與 redis 通訊可以輸入以下指令，沒有測試可以跳過
```
$ python3 manage.py shell
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```

