from django.contrib import admin

# Register your models here.
from blog.models import Post, Comment, Reply, Document


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = (
        "title",
        "post_type",
        "created_at",
        "published_at",
        "is_published",
    )
    list_display_links = ("title",)
    search_fields = (
        "title",
        "content",
        "post_type",
    )
    list_filter = (
        "is_published",
        "post_type",
    )
    list_editable = ("is_published",)
    empty_value_display = "empty"
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = (
        "post_title",
        "full_name",
        "email",
        "created_at",
        "is_approved",
    )
    search_fields = (
        "post__title",
        "full_name",
        "email",
        "content",
    )
    list_filter = ("is_approved",)
    list_editable = ("is_approved",)
    empty_value_display = "empty"

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = "post title"
    post_title.admin_order_field = "post__title"


@admin.register(Reply)
class ReplayAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = (
        "post_title",
        "comment_full_name",
        "created_at",
        "content",
    )

    search_fields = (
        "comment__post__title",
        "comment__full_name",
        "comment__email",
        "content",
    )

    def post_title(self, obj):
        return obj.comment.post.title

    post_title.short_description = "Post Title"
    post_title.admin_order_field = "comment__post__title"

    def comment_full_name(self, obj):
        return obj.comment.full_name

    comment_full_name.short_description = "Commenter Name"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    ordering = ("-uploaded_at",)
    list_display = (
        "title",
        "post_title",
        "post_is_published",
        "uploaded_at",
    )
    list_display_links = ("title",)
    search_fields = ("title", "post__title")
    list_filter = ("post__is_published",)

    empty_value_display = "empty"

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = "post title"
    post_title.admin_order_field = "post__title"

    def post_is_published(self, obj):
        return obj.post.is_published

    post_is_published.boolean = True
    post_is_published.short_description = "Published"
    post_is_published.admin_order_field = "post__is_published"
