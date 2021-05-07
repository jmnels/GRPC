import grpc
import example_pb2
import example_pb2_grpc

class Customer:
    """This is the parent class that spawns all the client processes
    ,creates the stubs and executes the client events"""
    def __init__(self, id, events, channel):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None
        # channel
        self.channel = channel

    # TODO: students are expected to create the Customer stub
    def createStub1(self):
        """This method creates the stubs to be used by the client processes for RPC"""
        self.stub = example_pb2_grpc.Bank1Stub(self.channel)

    def createStub2(self):
        """This method creates the stubs to be used by the client processes for RPC"""
        self.stub = example_pb2_grpc.Bank2Stub(self.channel)
    
