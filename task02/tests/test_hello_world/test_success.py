from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        event = {
            'rawPath': '/hello',
            'requestContext': {
                'http': {
                    'method': 'GET'
                }
            }
        }
            
        self.assertEqual(self.HANDLER.handle_request(event , dict()), {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                'statusCode': 200,
                'message': "Hello from Lambda"
            }
        })

