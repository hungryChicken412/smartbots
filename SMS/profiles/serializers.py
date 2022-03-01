from dataclasses import field
from rest_framework import serializers, viewsets
from .models import Profile, chatlog, ChatbotProfile,faq, User



# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'username',
        ]


class FaqTalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = faq
        fields = [
            'question',
            'ans',
        ]




class ChatbotTalkSerializer(serializers.ModelSerializer):
    
    faqs = FaqTalkSerializer(many=True, read_only=True)
    class Meta:
        model = ChatbotProfile
        fields = [
            'faqs',
            'context',
            'greeting',
        ]


