from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Question
from .forms import AddQuestionForm
# Create your views here


class MainView(View):
    def get(self, request):
        return render(request, template_name="main.html")


class AllQuestionsView(View):
    def get(self, request):
        questions = Question.object.all()
        ctx = {
            "questions": questions,
        }

        return render(request, template_name="all_questions.html",
                      context=ctx)


class AddQuestionView(View):
    def get(self, request):
        form = AddQuestionForm()
        ctx ={
            "form": form,
        }
        return render(request,
                      template_name="add_question.html",
                      context=ctx)

    def post(self, request):
        form =AddQuestionForm(request.POST)

        if form.is_valid():
                question = form.save()

        return redirect(reverse("show-question", kwargs={"id": question.id}))

        ctx ={
            "form": form,
        }
        return render(request,
                      template_name ="add_question.html",
                      context=ctx)

