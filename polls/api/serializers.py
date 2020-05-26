from rest_framework import serializers

from ..models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'question_id']


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choice_set']

    def create(self, validated_data):
        choices_data = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        for choice_date in choices_data:
            Choice.objects.create(question=question, **choices_data)
        return question
