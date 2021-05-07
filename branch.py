import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures
import time
import json

channel = grpc.insecure_channel('localhost:50051')

class Branch1(example_pb2_grpc.Bank1Servicer):
    """This is the parent class for the individual branches
    as well as all the exposed methods for the RPC"""


    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.wSet = dict()

    # TODO: students are expected to process requests from both Client and Branch
    def query(self, request, context):
        """This is the exposed method for the query RPC defined in example.proto
        It receives the customer request to see the balance and returns the balance to customer process"""
        writeSet = json.loads(request.dict)
        gtg = self.check(writeSet)
        
        response = example_pb2.Number()
        response.value = self.balance
        response.dict = json.dumps(gtg)
        
        return response

    def withdraw(self, request, context):
        """This is the exposed method for the withdraw RPC defined in example.proto
        It receives the customer request to take out money and then propogates the balance through the system"""
        writeSet = json.loads(request.dict)
        gtg = self.check(writeSet)

        response = example_pb2.Number()
        response.value = self.balance-request.value
        self.balance = self.balance-request.value

        response.dict = json.dumps(gtg)
        balance = self.balance
        
        self.prop(balance)

        return response

    def deposit(self, request, context):
        """This is the exposed method for the deposit RPC defined in example.proto
        It receives the customer request to add money to their account and propogates the balance to the other branches"""
        writeSet = json.loads(request.dict)
        gtg = self.check(writeSet)

        response = example_pb2.Number()
        response.value = self.balance+request.value
        self.balance = self.balance+request.value
        balance = self.balance
        
        response.dict = json.dumps(gtg)
        
        self.prop(balance)

        return response

    def propogate(self, request, context):
        """This is the exposed method for the propogate RPC defined in example.proto
        it receives the branch request to propogate the updated balance throughout the system"""
        response = example_pb2.Number()
        self.balance = request.value
        response.value = self.balance
        response.dict = ''
        
        return response

    def check(self, writeSet):

        lastWriter = list(writeSet.keys())
        lastWrite = lastWriter[0]
        if lastWrite in self.wSet or lastWrite == '0':
            lastWrite = int(lastWrite) + 1
            writeSet.clear()
            writeSet.update(lastWrite = self.balance)
            self.wSet.update(lastWrite = self.balance)
            return writeSet
        else:
            print('Error: please try again.')

    def prop(self, balance):
        
        stub = example_pb2_grpc.Bank2Stub(channel)
        number = example_pb2.Number(value=balance, dict = '')
        response = stub.propogate(number)


class Branch2(example_pb2_grpc.Bank2Servicer):
    """This is the parent class for the individual branches
    as well as all the exposed methods for the RPC"""


    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.wSet = dict()

    # TODO: students are expected to process requests from both Client and Branch
    def query(self, request, context):
        """This is the exposed method for the query RPC defined in example.proto
        It receives the customer request to see the balance and returns the balance to customer process"""
        
        response = example_pb2.Number()
        response.value = self.balance
        response.dict = ''
        return response

    def withdraw(self, request, context):
        """This is the exposed method for the withdraw RPC defined in example.proto
        It receives the customer request to take out money and then propogates the balance through the system"""
        writeSet = json.loads(request.dict)
        gtg = self.check(writeSet)

        response = example_pb2.Number()
        response.value = self.balance-request.value
        self.balance = self.balance-request.value

        response.dict = json.dumps(gtg)
        balance = self.balance
        
        self.prop(balance)

        return response

    def deposit(self, request, context):
        """This is the exposed method for the deposit RPC defined in example.proto
        It receives the customer request to add money to their account and propogates the balance to the other branches"""
        writeSet = json.loads(request.dict)
        gtg = self.check(writeSet)

        response = example_pb2.Number()
        response.value = self.balance+request.value
        self.balance = self.balance+request.value
        balance = self.balance
        
        response.dict = json.dumps(gtg)
        
        self.prop(balance)

        return response

    def propogate(self, request, context):
        """This is the exposed method for the propogate RPC defined in example.proto
        it receives the branch request to propogate the updated balance throughout the system"""
        response = example_pb2.Number()
        self.balance = request.value
        response.value = self.balance
        response.dict = ''
        
        return response

    def check(self, writeSet):

        lastWriter = list(writeSet.keys())
        lastWrite = lastWriter[0]
        if lastWrite in self.wSet or lastWrite == '0':
            lastWrite = int(lastWrite) + 1
            writeSet.clear()
            writeSet.update(lastWrite = self.balance)
            self.wSet.update(lastWrite = self.balance)
            return writeSet
        else:
            print(lastWrite)
            print(writeSet)

    def prop(self, balance):
        
        stub = example_pb2_grpc.Bank2Stub(channel)
        number = example_pb2.Number(value=balance, dict = '')
        response = stub.propogate(number)