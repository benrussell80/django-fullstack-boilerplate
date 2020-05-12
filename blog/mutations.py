import graphene
from django.utils import timezone
from graphql_auth.bases import Output
from graphql_auth.decorators import login_required
from graphql_relay.node.node import from_global_id

from . import errors, models, types


class CreatePost(Output, graphene.relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        published_at = graphene.DateTime(required=True)

    post = graphene.Field(types.PostNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        post = models.Post.objects.create(author=info.context.user, **inputs)
        return cls(post=post)


class CreateComment(Output, graphene.relay.ClientIDMutation):
    class Input:
        post_global_id = graphene.GlobalID(required=True)
        body = graphene.String(required=True)

    comment = graphene.Field(types.CommentNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('post_global_id'))
        if _type != 'CommentNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        comment = models.Comment(
            author=info.context.user,
            **inputs
        )
        comment.post_id = _id
        comment.save()
        return cls(comment=comment)


class CreatePostLike(Output, graphene.relay.ClientIDMutation):
    class Input:
        post_global_id = graphene.GlobalID(required=True)

    post = graphene.Field(types.PostNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('post_global_id'))
        if _type != 'PostNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        post = models.Post.objects.get(pk=_id)
        post.likes.add(user)
        return cls(post=post)


class CreateCommentLike(Output, graphene.relay.ClientIDMutation):
    class Input:
        comment_global_id = graphene.GlobalID(required=True)

    comment = graphene.Field(types.CommentNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('comment_global_id'))
        if _type != 'CommentNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        comment = models.Comment.objects.get(pk=_id)
        comment.likes.add(user)
        return cls(comment=comment)


class UpdateComment(Output, graphene.relay.ClientIDMutation):
    class Input:
        comment_global_id = graphene.GlobalID(required=True)
        body = graphene.String(required=True)

    comment = graphene.Field(types.CommentNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('comment_global_id'))
        if _type != 'CommentNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        comment = models.Comment.objects.get(pk=_id)
        if comment.author != user:
            return cls(
                success=False,
                errors=[errors.UNAUTHORIZED]
            )
        update(comment, inputs)
        comment.save()
        return cls(comment=comment)


class UpdatePost(Output, graphene.relay.ClientIDMutation):
    class Input:
        post_global_id = graphene.GlobalID(required=True)
        title = graphene.String()
        body = graphene.String()
        published_at = graphene.DateTime()
        
    post = graphene.Field(types.PostNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('post_global_id'))
        if _type != 'PostNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        post = models.Post.objects.get(pk=_id)
        if post.author != user:
            return cls(
                success=False,
                errors=[errors.UNAUTHORIZED]
            )
        update(post, inputs)
        post.save()
        return cls(post=post)


class DeleteComment(Output, graphene.relay.ClientIDMutation):
    class Input:
        comment_global_id = graphene.GlobalID(required=True)

    deleted = graphene.Boolean(default_value=True)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('comment_global_id'))
        if _type != 'CommentNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        comment = models.Comment.objects.get(pk=_id)
        if comment.author != user and not user.is_staff:
            return cls(
                success=False,
                errors=[errors.UNAUTHORIZED]
            )
        comment.delete()
        return cls()


class DeletePostLike(Output, graphene.relay.ClientIDMutation):
    class Input:
        post_global_id = graphene.GlobalID(required=True)

    post = graphene.Field(types.PostNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('post_global_id'))
        if _type != 'PostNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        post = models.Post.objects.get(pk=_id)
        if post.author != user:
            return cls(
                success=False,
                errors=[errors.UNAUTHORIZED]
            )
        post.likes.remove(user)
        return cls(post=post)


class DeleteCommentLike(Output, graphene.relay.ClientIDMutation):
    class Input:
        comment_global_id = graphene.GlobalID(required=True)

    comment = graphene.Field(types.CommentNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('comment_global_id'))
        if _type != 'CommentNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        comment = models.Comment.objects.get(pk=_id)
        if comment.author != user:
            return cls(
                success=False,
                errors=[errors.UNAUTHORIZED]
            )
        comment.likes.remove(user)
        return cls(comment=comment)


class DeletePost(Output, graphene.relay.ClientIDMutation):
    class Input:
        post_global_id = graphene.GlobalID(required=True)

    deleted = graphene.Boolean(default_value=True)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **inputs):
        _type, _id = from_global_id(inputs.pop('post_global_id'))
        if _type != 'PostNode':
            return cls(
                success=False,
                errors=[errors.WRONGTYPE]
            )
        user = info.context.user
        post = models.Post.objects.get(pk=_id)
        if post.author != user and not user.is_staff:
            return cls(
                success=False,
                errors=[errors.UNAUTHORIZED]
            )
        post.delete()
        return cls()


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
    create_post_like = CreatePostLike.Field()
    create_comment_like = CreateCommentLike.Field()

    update_comment = UpdateComment.Field()
    update_post = UpdatePost.Field()

    delete_comment = DeleteComment.Field()
    delete_comment_like = DeleteCommentLike.Field()
    delete_post = DeletePost.Field()
    delete_post_like = DeletePostLike.Field()
