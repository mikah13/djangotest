from rest_framework import serializers
from .models import Question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]