from .models import Exam, Question, Answer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

def list_exam(request):
    request.session['score'] = 0
    exams = Exam.objects.all()
    return render(request, 'list_exam/list_exam.html', {'exams': exams})


def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().order_by('id')
    total_questions = len(questions)
    q_index = int(request.GET.get('q', 0))

    if request.method == 'POST':
        q_index = int(request.POST.get('q_index', 0))
        question = questions[q_index]
        answers = question.answers.all()

        answer_value = request.POST.get('answer')
        if answer_value is not None:
            selected_id = int(answer_value)
            correct_answer = answers.filter(is_correct=True).first()
            correct_id = correct_answer.id if correct_answer else None
            is_correct = (selected_id == correct_id)

            if is_correct:
                request.session['score'] = request.session.get('score', 0) + 1

            # Hiển thị lại câu hiện tại với feedback
            return render(request, 'list_exam/start_exam.html', {
                'exam': exam,
                'question': question,
                'answers': answers,
                'q_index': q_index,
                'q_index_plus_1': q_index + 1,
                'total_questions': total_questions,
                'selected_id': selected_id,
                'correct_id': correct_id,
                'is_correct': is_correct,
                'has_next_question': (q_index + 1 < total_questions),
                'score': request.session.get('score', 0)
            })
        else:
            error_message = 'Bạn cần chọn một đáp án trước khi tiếp tục.'
            return render(request, 'list_exam/start_exam.html', {
                'exam': exam,
                'question': questions[q_index],
                'answers': questions[q_index].answers.all(),
                'q_index': q_index,
                'q_index_plus_1': q_index + 1,
                'total_questions': total_questions,
                'error_message': error_message,
            })

    else:
        question = questions[q_index]
        answers = question.answers.all()
        return render(request, 'list_exam/start_exam.html', {
            'exam': exam,
            'question': question,
            'answers': answers,
            'q_index': q_index,
            'q_index_plus_1': q_index + 1,
            'total_questions': total_questions,
        })
