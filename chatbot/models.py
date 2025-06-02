from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Open"
        IN_PROGRESS = "in_progress", "In Progress"
        RESOLVED = "resolved", "Resolved"
        CLOSED = "closed", "Closed"

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.OPEN
    )
    assigned_department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="tickets"
    )

    class Meta:
        db_table = "ticket"

    def __str__(self):
        return self.title


class UserQuery(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    query_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "userquery"

    def __str__(self):
        return f"Query by User {self.user_id} at {self.created_at}"
