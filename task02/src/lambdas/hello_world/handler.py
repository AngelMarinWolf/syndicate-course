from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        path = event['rawPath']
        method = event['requestContext']['http']['method']

        if path == '/hello' and method == 'GET':
            statusCode = 200
            message = "Hello from Lambda"
        else:
            statusCode = 400
            message = f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"

        response = {
            "statusCode": statusCode,
            "message": message
        }
        
        return response
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
