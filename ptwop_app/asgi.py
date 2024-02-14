"""
ASGI config for ptwop_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ptwop_app.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "https": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(room.routing.websocket_urlpatterns))
        ),
})
