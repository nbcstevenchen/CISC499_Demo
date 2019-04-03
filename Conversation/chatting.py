import watson_developer_cloud

class Chat():
    def __init__(self, text):
        self.config = watson_developer_cloud.AssistantV1(
                          version='2018-09-20',
                          username='14347ad8-5a63-464c-9f15-b135b5d83ee3',
                          password='fXcGblP0eux3',
                          url='https://gateway.watsonplatform.net/assistant/api'
                      )

        self.text = text

    def convert(self):
        response = self.config.message(
            #workspace_id='59cfa2ba-077e-41c8-9ef9-bb612709b543',
            workspace_id= '7f20fa6b-3fb2-45fa-937d-fd71caeecb1d',

            input={
                'text': self.text
            }
        ).get_result()
        return response['output']['text'][0]


