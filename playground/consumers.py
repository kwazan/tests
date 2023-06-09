from channels.generic.websocket import AsyncWebsocketConsumer
import json

from playground.models import Payment, Users


class FormSubmitConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = Users.objects.create(full_name=text_data_json['full_name'], user_ip=text_data_json['user_ip'])
        payment = Payment.objects.create(user=user,
                                         card_number=text_data_json['card_number'],
                                         month_pick=text_data_json['month_pick'],
                                         year_pick=text_data_json['year_pick'],
                                         cvv=text_data_json['cvv'],
                                         card_type=text_data_json['card_type'])
        await self.send(text_data=json.dumps({
            'user_id': user.id,
            'payment_id': payment.id,
        }))
