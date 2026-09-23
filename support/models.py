from django.db import models
from django.contrib.auth.models import User
from orders.models import Order

# Create your models here.
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} with {self.user.username}"

class Message(models.Model):
    ROLE_CHOICES = [
        ("user", "User"),
        ("agent", "Agent"),
    ]
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    # sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} Message {self.id} {self.content[:50]} from {self.sender.username} at {self.created_at}"


class AgentLog(models.Model):
    EVENT_CHOICES = [
        ("support", "Support Agent"),
        ("tool_call", "Tool Call"),
        ("tool_result", "Tool Result"),
        ("manager", "Manager Agent"),
        ("risk", "Risk Agent"),
        ("final", "Final Reply"),
    ]
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="agentlogs")
    event_type = models.CharField(max_length=100, choices=EVENT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agent Log {self.id} and {self.event_type} for Conversation {self.conversation.id} with message {self.message[:50]} at {self.created_at}"