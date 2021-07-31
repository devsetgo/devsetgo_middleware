import uuid
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from devsetgo_lib.logging_config import config_log
from uuid import uuid4
import datetime

from devsetgo_middleware import AccessLoggerMiddleware

config_log(
    logging_directory="myLoggingFolder",
    # or None and defaults to logging
    log_name="mylog.log",
    # or None and defaults to "log.log"
    logging_level="debug",
    # or "info" or "debug" or "warning" or "error" or "critical"
    # or None and defaults to "info"
    log_rotation="1 MB",
    # or None and default is 10 MB
    log_retention="1 Day",
    # or None and defaults to "14 Days"
    log_backtrace=True,
    # or None and defaults to False
)

def homepage(request):
    return PlainTextResponse('Hello, world!')

def user_me(request):
    request.session.clear()
    username = "John Doe"
    request.session["id"] = str(uuid4())
    request.session["email_address"] = 'bob@bob.com'
    request.session["updated"] = str(datetime.datetime.now())
    return PlainTextResponse('Hello, %s!' % username)

def user(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s!' % username)

# async def websocket_endpoint(websocket):
#     await websocket.accept()
#     await websocket.send_text('Hello, websocket!')
#     await websocket.close()

def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
    Route('/user/me', user_me),
    Route('/user/{username}', user),
    # WebSocketRoute('/ws', websocket_endpoint),
    # Mount('/static', StaticFiles(directory="static")),
]
import secrets
middleware = [
    Middleware(
        SessionMiddleware,
        secret_key=secrets.token_urlsafe(10),
        max_age=7200,
        same_site="lax",
        https_only=False,
    ),
    Middleware(AccessLoggerMiddleware,user_identifier='id'),
]
app = Starlette(debug=True, routes=routes, on_startup=[startup],middleware=middleware,)