from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    'http': URLRouter(
        [
            path('ws/data/', consumers.DataConsumer.as_asgi()),
        ]
    ),
})
