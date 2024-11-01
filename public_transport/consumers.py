import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LiveTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'live_updates'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        location = data['location']
        
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type' : 'send_update',
                'location' : location
            }
        )
        
        async def send_update(self, event):
            location = event['location']
            await self.send(text_data=json.dumps({
                'location' : location
            }))
           
