from __future__ import print_function
import grpc
import Calculator_pb2
import Calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = Calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
NumbersToAdd = Calculator_pb2.Numbers(Num1=5,Num2=6)

# make the call
response = stub.Add(NumbersToAdd)

# print the response
print(response.sum)