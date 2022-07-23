from django.contrib.auth.models import Group, Permission
# Defining groups
from django.contrib.contenttypes.models import ContentType

from accounts.models import User
from videos.models import Video, Comment, Tag

regular_group = Group.objects.get_or_create(name='Regular')
admin_group = Group.objects.get_or_create(name='Admin')

# Defining Permissions
video_content_type = ContentType.objects.get_for_model(Video)
comment_content_type = ContentType.objects.get_for_model(Comment)
tag_content_type = ContentType.objects.get_for_model(Tag)
user_content_type = ContentType.objects.get_for_model(User)

watch_video = Permission.objects.create(
    codename='can_watch',
    name='Can watch video',
    content_type=video_content_type
)

like_dislike_video = Permission.objects.create(
    codename='can_like_dislike',
    name='Can like/dislike video',
    content_type=video_content_type
)

add_comment = Permission.objects.create(
    codename='can_comment',
    name='Can add comment to a video',
    content_type=comment_content_type
)

add_tag = Permission.objects.create(
    codename='can_add_tag',
    name='Can add tag to a video',
    content_type=tag_content_type
)

ban_video = Permission.objects.create(
    codename='can_ban_video',
    name='Can ban a video',
    content_type=video_content_type
)

strike_user = Permission.objects.create(
    codename='can_set_strike',
    name='Can set strike status of a user',
    content_type=user_content_type
)

# Assign permissions
regular_group.permissions.add(watch_video)
regular_group.permissions.add(like_dislike_video)
regular_group.permissions.add(add_comment)

admin_group.permissions.add(add_tag)
admin_group.permissions.add(ban_video)
admin_group.permissions.add(strike_user)