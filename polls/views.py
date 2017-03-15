from django.shortcuts import render, redirect
from polls.forms import PostForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Question


@login_required
def index(request):
    latest_question_list = Question.objects.order_by('question_text').all()
    if request.method == 'GET':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            count = 0
            questions = Question.objects.values()

            for i in range(len(questions)):
                answer = form.cleaned_data['question{0}'.format((i + 1))]
                correct = questions[i]['correct']
                if answer == correct:
                    count += 1

            result = count / len(questions) * 100

            user = request.user
            message = "Правильних відповідей: {2}%".format(user.first_name, user.last_name,result)

            return render(request, 'thanks.html', {'message': message})

    context = {'latest_question_list': latest_question_list, 'form': form}
    return render(request, 'index.html', context)


def thanks(request):
    logout(request)
    return render(request, 'thanks.html')

