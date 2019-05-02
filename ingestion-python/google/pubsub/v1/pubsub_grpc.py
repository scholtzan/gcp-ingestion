# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/pubsub/v1/pubsub.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.resource_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.pubsub.v1.pubsub_pb2


class PublisherBase(abc.ABC):

    @abc.abstractmethod
    async def CreateTopic(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.Topic, google.pubsub.v1.pubsub_pb2.Topic]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTopic(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.UpdateTopicRequest, google.pubsub.v1.pubsub_pb2.Topic]') -> None:
        pass

    @abc.abstractmethod
    async def Publish(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.PublishRequest, google.pubsub.v1.pubsub_pb2.PublishResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTopic(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.GetTopicRequest, google.pubsub.v1.pubsub_pb2.Topic]') -> None:
        pass

    @abc.abstractmethod
    async def ListTopics(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ListTopicsRequest, google.pubsub.v1.pubsub_pb2.ListTopicsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListTopicSubscriptions(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ListTopicSubscriptionsRequest, google.pubsub.v1.pubsub_pb2.ListTopicSubscriptionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListTopicSnapshots(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ListTopicSnapshotsRequest, google.pubsub.v1.pubsub_pb2.ListTopicSnapshotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTopic(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.DeleteTopicRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.pubsub.v1.Publisher/CreateTopic': grpclib.const.Handler(
                self.CreateTopic,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.Topic,
                google.pubsub.v1.pubsub_pb2.Topic,
            ),
            '/google.pubsub.v1.Publisher/UpdateTopic': grpclib.const.Handler(
                self.UpdateTopic,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.UpdateTopicRequest,
                google.pubsub.v1.pubsub_pb2.Topic,
            ),
            '/google.pubsub.v1.Publisher/Publish': grpclib.const.Handler(
                self.Publish,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.PublishRequest,
                google.pubsub.v1.pubsub_pb2.PublishResponse,
            ),
            '/google.pubsub.v1.Publisher/GetTopic': grpclib.const.Handler(
                self.GetTopic,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.GetTopicRequest,
                google.pubsub.v1.pubsub_pb2.Topic,
            ),
            '/google.pubsub.v1.Publisher/ListTopics': grpclib.const.Handler(
                self.ListTopics,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ListTopicsRequest,
                google.pubsub.v1.pubsub_pb2.ListTopicsResponse,
            ),
            '/google.pubsub.v1.Publisher/ListTopicSubscriptions': grpclib.const.Handler(
                self.ListTopicSubscriptions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ListTopicSubscriptionsRequest,
                google.pubsub.v1.pubsub_pb2.ListTopicSubscriptionsResponse,
            ),
            '/google.pubsub.v1.Publisher/ListTopicSnapshots': grpclib.const.Handler(
                self.ListTopicSnapshots,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ListTopicSnapshotsRequest,
                google.pubsub.v1.pubsub_pb2.ListTopicSnapshotsResponse,
            ),
            '/google.pubsub.v1.Publisher/DeleteTopic': grpclib.const.Handler(
                self.DeleteTopic,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.DeleteTopicRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class PublisherStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateTopic = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/CreateTopic',
            google.pubsub.v1.pubsub_pb2.Topic,
            google.pubsub.v1.pubsub_pb2.Topic,
        )
        self.UpdateTopic = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/UpdateTopic',
            google.pubsub.v1.pubsub_pb2.UpdateTopicRequest,
            google.pubsub.v1.pubsub_pb2.Topic,
        )
        self.Publish = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/Publish',
            google.pubsub.v1.pubsub_pb2.PublishRequest,
            google.pubsub.v1.pubsub_pb2.PublishResponse,
        )
        self.GetTopic = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/GetTopic',
            google.pubsub.v1.pubsub_pb2.GetTopicRequest,
            google.pubsub.v1.pubsub_pb2.Topic,
        )
        self.ListTopics = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/ListTopics',
            google.pubsub.v1.pubsub_pb2.ListTopicsRequest,
            google.pubsub.v1.pubsub_pb2.ListTopicsResponse,
        )
        self.ListTopicSubscriptions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/ListTopicSubscriptions',
            google.pubsub.v1.pubsub_pb2.ListTopicSubscriptionsRequest,
            google.pubsub.v1.pubsub_pb2.ListTopicSubscriptionsResponse,
        )
        self.ListTopicSnapshots = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/ListTopicSnapshots',
            google.pubsub.v1.pubsub_pb2.ListTopicSnapshotsRequest,
            google.pubsub.v1.pubsub_pb2.ListTopicSnapshotsResponse,
        )
        self.DeleteTopic = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Publisher/DeleteTopic',
            google.pubsub.v1.pubsub_pb2.DeleteTopicRequest,
            google.protobuf.empty_pb2.Empty,
        )


class SubscriberBase(abc.ABC):

    @abc.abstractmethod
    async def CreateSubscription(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.Subscription, google.pubsub.v1.pubsub_pb2.Subscription]') -> None:
        pass

    @abc.abstractmethod
    async def GetSubscription(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.GetSubscriptionRequest, google.pubsub.v1.pubsub_pb2.Subscription]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSubscription(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.UpdateSubscriptionRequest, google.pubsub.v1.pubsub_pb2.Subscription]') -> None:
        pass

    @abc.abstractmethod
    async def ListSubscriptions(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ListSubscriptionsRequest, google.pubsub.v1.pubsub_pb2.ListSubscriptionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSubscription(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.DeleteSubscriptionRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ModifyAckDeadline(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ModifyAckDeadlineRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def Acknowledge(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.AcknowledgeRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def Pull(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.PullRequest, google.pubsub.v1.pubsub_pb2.PullResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamingPull(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.StreamingPullRequest, google.pubsub.v1.pubsub_pb2.StreamingPullResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ModifyPushConfig(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ModifyPushConfigRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetSnapshot(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.GetSnapshotRequest, google.pubsub.v1.pubsub_pb2.Snapshot]') -> None:
        pass

    @abc.abstractmethod
    async def ListSnapshots(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.ListSnapshotsRequest, google.pubsub.v1.pubsub_pb2.ListSnapshotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateSnapshot(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.CreateSnapshotRequest, google.pubsub.v1.pubsub_pb2.Snapshot]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSnapshot(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.UpdateSnapshotRequest, google.pubsub.v1.pubsub_pb2.Snapshot]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSnapshot(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.DeleteSnapshotRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def Seek(self, stream: 'grpclib.server.Stream[google.pubsub.v1.pubsub_pb2.SeekRequest, google.pubsub.v1.pubsub_pb2.SeekResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.pubsub.v1.Subscriber/CreateSubscription': grpclib.const.Handler(
                self.CreateSubscription,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.Subscription,
                google.pubsub.v1.pubsub_pb2.Subscription,
            ),
            '/google.pubsub.v1.Subscriber/GetSubscription': grpclib.const.Handler(
                self.GetSubscription,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.GetSubscriptionRequest,
                google.pubsub.v1.pubsub_pb2.Subscription,
            ),
            '/google.pubsub.v1.Subscriber/UpdateSubscription': grpclib.const.Handler(
                self.UpdateSubscription,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.UpdateSubscriptionRequest,
                google.pubsub.v1.pubsub_pb2.Subscription,
            ),
            '/google.pubsub.v1.Subscriber/ListSubscriptions': grpclib.const.Handler(
                self.ListSubscriptions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ListSubscriptionsRequest,
                google.pubsub.v1.pubsub_pb2.ListSubscriptionsResponse,
            ),
            '/google.pubsub.v1.Subscriber/DeleteSubscription': grpclib.const.Handler(
                self.DeleteSubscription,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.DeleteSubscriptionRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.pubsub.v1.Subscriber/ModifyAckDeadline': grpclib.const.Handler(
                self.ModifyAckDeadline,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ModifyAckDeadlineRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.pubsub.v1.Subscriber/Acknowledge': grpclib.const.Handler(
                self.Acknowledge,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.AcknowledgeRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.pubsub.v1.Subscriber/Pull': grpclib.const.Handler(
                self.Pull,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.PullRequest,
                google.pubsub.v1.pubsub_pb2.PullResponse,
            ),
            '/google.pubsub.v1.Subscriber/StreamingPull': grpclib.const.Handler(
                self.StreamingPull,
                grpclib.const.Cardinality.STREAM_STREAM,
                google.pubsub.v1.pubsub_pb2.StreamingPullRequest,
                google.pubsub.v1.pubsub_pb2.StreamingPullResponse,
            ),
            '/google.pubsub.v1.Subscriber/ModifyPushConfig': grpclib.const.Handler(
                self.ModifyPushConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ModifyPushConfigRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.pubsub.v1.Subscriber/GetSnapshot': grpclib.const.Handler(
                self.GetSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.GetSnapshotRequest,
                google.pubsub.v1.pubsub_pb2.Snapshot,
            ),
            '/google.pubsub.v1.Subscriber/ListSnapshots': grpclib.const.Handler(
                self.ListSnapshots,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.ListSnapshotsRequest,
                google.pubsub.v1.pubsub_pb2.ListSnapshotsResponse,
            ),
            '/google.pubsub.v1.Subscriber/CreateSnapshot': grpclib.const.Handler(
                self.CreateSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.CreateSnapshotRequest,
                google.pubsub.v1.pubsub_pb2.Snapshot,
            ),
            '/google.pubsub.v1.Subscriber/UpdateSnapshot': grpclib.const.Handler(
                self.UpdateSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.UpdateSnapshotRequest,
                google.pubsub.v1.pubsub_pb2.Snapshot,
            ),
            '/google.pubsub.v1.Subscriber/DeleteSnapshot': grpclib.const.Handler(
                self.DeleteSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.DeleteSnapshotRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.pubsub.v1.Subscriber/Seek': grpclib.const.Handler(
                self.Seek,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.pubsub_pb2.SeekRequest,
                google.pubsub.v1.pubsub_pb2.SeekResponse,
            ),
        }


class SubscriberStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateSubscription = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/CreateSubscription',
            google.pubsub.v1.pubsub_pb2.Subscription,
            google.pubsub.v1.pubsub_pb2.Subscription,
        )
        self.GetSubscription = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/GetSubscription',
            google.pubsub.v1.pubsub_pb2.GetSubscriptionRequest,
            google.pubsub.v1.pubsub_pb2.Subscription,
        )
        self.UpdateSubscription = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/UpdateSubscription',
            google.pubsub.v1.pubsub_pb2.UpdateSubscriptionRequest,
            google.pubsub.v1.pubsub_pb2.Subscription,
        )
        self.ListSubscriptions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/ListSubscriptions',
            google.pubsub.v1.pubsub_pb2.ListSubscriptionsRequest,
            google.pubsub.v1.pubsub_pb2.ListSubscriptionsResponse,
        )
        self.DeleteSubscription = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/DeleteSubscription',
            google.pubsub.v1.pubsub_pb2.DeleteSubscriptionRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ModifyAckDeadline = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/ModifyAckDeadline',
            google.pubsub.v1.pubsub_pb2.ModifyAckDeadlineRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.Acknowledge = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/Acknowledge',
            google.pubsub.v1.pubsub_pb2.AcknowledgeRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.Pull = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/Pull',
            google.pubsub.v1.pubsub_pb2.PullRequest,
            google.pubsub.v1.pubsub_pb2.PullResponse,
        )
        self.StreamingPull = grpclib.client.StreamStreamMethod(
            channel,
            '/google.pubsub.v1.Subscriber/StreamingPull',
            google.pubsub.v1.pubsub_pb2.StreamingPullRequest,
            google.pubsub.v1.pubsub_pb2.StreamingPullResponse,
        )
        self.ModifyPushConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/ModifyPushConfig',
            google.pubsub.v1.pubsub_pb2.ModifyPushConfigRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/GetSnapshot',
            google.pubsub.v1.pubsub_pb2.GetSnapshotRequest,
            google.pubsub.v1.pubsub_pb2.Snapshot,
        )
        self.ListSnapshots = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/ListSnapshots',
            google.pubsub.v1.pubsub_pb2.ListSnapshotsRequest,
            google.pubsub.v1.pubsub_pb2.ListSnapshotsResponse,
        )
        self.CreateSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/CreateSnapshot',
            google.pubsub.v1.pubsub_pb2.CreateSnapshotRequest,
            google.pubsub.v1.pubsub_pb2.Snapshot,
        )
        self.UpdateSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/UpdateSnapshot',
            google.pubsub.v1.pubsub_pb2.UpdateSnapshotRequest,
            google.pubsub.v1.pubsub_pb2.Snapshot,
        )
        self.DeleteSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/DeleteSnapshot',
            google.pubsub.v1.pubsub_pb2.DeleteSnapshotRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.Seek = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.Subscriber/Seek',
            google.pubsub.v1.pubsub_pb2.SeekRequest,
            google.pubsub.v1.pubsub_pb2.SeekResponse,
        )
