from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        'id': 1,
        'question_text': 'Qual é a capital do Brasil?',
        'options': ['Brasília', 'Rio de Janeiro', 'São Paulo', 'Salvador'],
        'answer': 'Brasília'
    }
]

@app.route('/')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for question in questions:
        if request.form.get(str(question['id'])) == question['answer']:
            score += 1
    return render_template('result.html', score=score, total_questions=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
