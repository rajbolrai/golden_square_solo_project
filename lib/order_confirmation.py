class OrderConfirmation:
    # User-facing properties:
    #   order: list of Food instances
    #   request: instance of request module
    def __init__(self, order, request):
        # Parameters:
        #   order: Menu instance
        #   request: request module
        # Side-effects:
        #   Sets the order and request properties
        pass # No code here yet

    def confirm(self):
        # request to twilio api to send message
        #return:
        #   text message to user mobile phone 
        pass

    def generate_receipt(self):
        #return:
        #   itemised receipt of order, in form of string with total in the end
        pass