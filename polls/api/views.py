from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView

from .serializers import QuestionSerializer, ChoiceSerializer
from ..models import Question, Choice


class PollView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SinglePollView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceView(ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(Question, id=self.request.data.get('question_id'))
        return serializer.save(question=question)


class SingleChoiceView(RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
