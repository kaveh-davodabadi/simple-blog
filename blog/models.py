from django.db import models

# Create your models here.


class Post(models.Model):
    POST_TYPE_CHOICES = (
        ("project", "Project"),
        ("blog", "Blog"),
    )
    post_type = models.CharField(max_length=50, choices=POST_TYPE_CHOICES)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/post-image/")
    related_url = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=70)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.full_name}"


class Reply(models.Model):
    comment = models.OneToOneField(
        Comment, on_delete=models.CASCADE, related_name="reply"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.comment.full_name}"


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")
    image = models.ImageField(upload_to="documents/images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="documents")

    def __str__(self):
        return f"{self.title} ({self.post.title})"
