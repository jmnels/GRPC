import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures
import multiprocessing 
import os
import time
import json
import branch
import Customer
import sys

# Opening JSON file from command line
f = open(sys.argv[1],"r")
name = sys.argv[1]
# returns JSON object as
# a dictionary
data = json.load(f)

channel = grpc.insecure_channel('localhost:50051')
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
server2 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

stub = None
br = []
b=[]
c = []
clock = 0
procId = 0
outList = []


def executeEvents(p_dict, ev_dict, p_val, p_clock, idi, events):
        """This method executes the individual events requested by the clients thtough RPC"""
        #procId = tick['procId']
        
        c = Customer.Customer(idi, events, channel)

        clock = p_clock.value

        d = {clock: 0}


        for e in events:
            
            pid = os.getpid()
            i = e["interface"]
            if i == 'deposit' or i == 'withdraw':
                v = e["money"]
            else:
                v = 0
            
            dest = e["dest"]

            if dest == 1:
                c.createStub1()
                stub = c.stub
            else:
                c.createStub2()
                stub = c.stub

            if i == "query":
                dj = json.dumps(d)
                number = example_pb2.Number(value=v, dict = dj)
                response = stub.query(number)
                output = {'id': idi, 'balance': [response.value]}
                outList.append(output)
                with open('output.txt', 'w') as outfile:
                    json.dump(outList, outfile, indent=2)

            elif i == "deposit":
                dj = json.dumps(d)
                number = example_pb2.Number(value=v, dict = dj)
                response = stub.deposit(number)

            else:
                dj = json.dumps(d)
                number = example_pb2.Number(value=v, dict = dj)
                response = stub.withdraw(number)
        
if __name__ == "__main__":
    
    for j in data:
        if j["type"] == "bank":
            b.append(j)

    a = b[0]
    ident = a["id"]
    bal = a["balance"]  
    example_pb2_grpc.add_Bank1Servicer_to_server(branch.Branch1(ident, bal, 1), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    a2 = b[1]
    ident = a2["id"]
    bal = a2["balance"]  
    example_pb2_grpc.add_Bank2Servicer_to_server(branch.Branch2(ident, bal, 1), server)
    server2.add_insecure_port('0.0.0.0:0')
    server2.start()

    manager = multiprocessing.Manager()
    p_dict = manager.list()
    ev_dict = manager.list()
    p_val = manager.Value('i', 0)
    p_clock = manager.Value('i', 0)
    for i, j in enumerate(data):
        if j["type"] == "customer":
            c.append(j)
            eyed = j["id"]
            events = j["events"]
            
            customer = multiprocessing.Process(target=executeEvents, args=(p_dict, ev_dict, p_val, p_clock, eyed, events))
            customer.start()
            customer.join()
    
    x = input("Press q to stop servers: ")
    if x == "q":
        server.stop(None)
        server2.stop(None)
        