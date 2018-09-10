
import grpc
import time
from concurrent import futures
import Calculator
import Calculator_pb2
import Calculator_pb2_grpc


# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(Calculator_pb2_grpc.CalculatorServicer):

    def Add(self, request, context):
        response = Calculator_pb2.Result
        response.sum = (request.Num1+request.Num2)
        return response


# creating gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
Calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0) 