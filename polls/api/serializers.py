from rest_framework import serializers

from ..models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes', 'question_id']


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choice_set']

    def create(self, validated_data):
        choice_set = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        for choice_data in choice_set:
            Choice.objects.create(question=question, **choice_data)
        return question

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get("question_text", instance.question_text)
        instance.pub_date = validated_data.get("pub_date", instance.pub_date)
        instance.save()

        choice_set = validated_data.get('choice_set')

        for choice in choice_set:
            choice_id = choice.get('id', None)
            if choice_id:
                new_choice = Choice.objects.get(id=choice_id, question=instance)
                new_choice.choice_text = choice.get("choice_text", new_choice.choice_text)
                new_choice.votes = choice.get("votes", new_choice.votes)
                new_choice.save()
            else:
                Choice.objects.create(question=instance, **choice)

        return instance
