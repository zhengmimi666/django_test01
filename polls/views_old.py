from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.http import Http404
from django.urls import reverse

def index(request):
    #投票问题列表
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)



def detail(request, question_id):
    #问题的详情页面
    print(" 问题的id：",question_id)
    # try:
    #     q = Question.objects.get(id=question_id)    #get仅查询单条数据，查询无结果报错
    # except:
    #     raise Http404("问题id不存在")
    q = get_object_or_404(Question,pk=question_id)
    print("问题的名称",q.question_text)
    # c = Choice.objects.filter(question=q)
    c = Choice.objects.filter(question_id=q.id)
    for i in c:
        print("问题的选项",i.choice_text)
    # return HttpResponse("You're looking at question %s." % question_id)
    # return render(request, 'polls/detail.html', {'question': q,'choice': c})
    return render(request, 'polls/detail.html', {'question': q})

def results(request, question_id):
    #投票的结果页面
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))