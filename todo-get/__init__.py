import logging, json

import azure.functions as func
from services.todo_service import get_todos
from FlaskApp import app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = get_todos()
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)
    #return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})