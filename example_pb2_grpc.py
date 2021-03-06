# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2


class Bank1Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.query = channel.unary_unary(
                '/Bank1/query',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )
        self.deposit = channel.unary_unary(
                '/Bank1/deposit',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )
        self.withdraw = channel.unary_unary(
                '/Bank1/withdraw',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )
        self.propogate = channel.unary_unary(
                '/Bank1/propogate',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )


class Bank1Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def propogate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Bank1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
            'deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.deposit,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
            'withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.withdraw,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
            'propogate': grpc.unary_unary_rpc_method_handler(
                    servicer.propogate,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bank1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bank1(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank1/query',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank1/deposit',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank1/withdraw',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def propogate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank1/propogate',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class Bank2Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.query = channel.unary_unary(
                '/Bank2/query',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )
        self.deposit = channel.unary_unary(
                '/Bank2/deposit',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )
        self.withdraw = channel.unary_unary(
                '/Bank2/withdraw',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )
        self.propogate = channel.unary_unary(
                '/Bank2/propogate',
                request_serializer=example__pb2.Number.SerializeToString,
                response_deserializer=example__pb2.Number.FromString,
                )


class Bank2Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def propogate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Bank2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
            'deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.deposit,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
            'withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.withdraw,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
            'propogate': grpc.unary_unary_rpc_method_handler(
                    servicer.propogate,
                    request_deserializer=example__pb2.Number.FromString,
                    response_serializer=example__pb2.Number.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bank2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bank2(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank2/query',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank2/deposit',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank2/withdraw',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def propogate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank2/propogate',
            example__pb2.Number.SerializeToString,
            example__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
