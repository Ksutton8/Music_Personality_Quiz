from django.shortcuts import render

# Create your views here.

def music_quiz(request):
    if request.method =='POST':

        rap_hiphop = 0
        indie_alt = 0
        rb = 0
        pop = 0
        rock = 0

        answers = request.POST

       #indie_alt += int(answers.get('indie_alt', 0))
        #pop += int(answers.get('pop', 0))
        #rap_hiphop += int(answers.get('rap_hiphop', 0))
        #rock += int(answers.get('rock', 0))
        #rb += int(answers.get('rb', 0))
    
        #Question 1
        answer_q1 = answers.get('q1', '')
        if answer_q1 == 'A':
            rap_hiphop += 2
            rock += 2
            pop += 2
        elif answer_q1 == 'B':
            indie_alt += 2
            rb += '2'
        elif answer_q1 == 'C':
            indie_alt += 2
            rb += 2
        else:
            rap_hiphop += 2
            pop += 2

        #Question 2
        answer_q2 = answers.get('q2', '')
        if answer_q2 == 'A':
            pop += 3
        elif answer_q2 == 'B':
            rap_hiphop += 3
        elif answer_q2 == 'C':
            indie_alt += 3
        elif answer_q2 == 'D':
            rb += 3
        else:
            rock += 3

        #Question 3
        answer_q3 = answers.get('q3', '')
        if answer_q3 == 'A':
            indie_alt += 1
        elif answer_q3 == 'B':
            indie_alt += 1
        elif answer_q3 == 'C':
            pop += 1
        elif answer_q3 == 'D':
            rb += 1
        elif answer_q3 =='E':
            rock += 1
        else:
            rap_hiphop += 1

    
        #Question 4
        answer_q4 = answers.get('q4', '')
        if answer_q4 == 'A':
            indie_alt += 2
            rb += 2
        else:
            pop += 2
            rock += 2
            rap_hiphop += 2


        #Question 5
        answer_q5 = answers.get('q5', '')
        if answer_q5 == 'A':
            indie_alt += 3
        elif answer_q5 == 'B':
            pop += 3
        elif answer_q5 == 'C':
            rap_hiphop += 3
        elif answer_q5 == 'D':
            rock += 3
        else:
            rb += 3

        genre_score = max(indie_alt, pop, rap_hiphop, rock, rb)

        if indie_alt == genre_score:
            recommended_artists = ['Indie artists']  
        elif rock == genre_score:
            recommended_artists = ['Rock artists']  
        elif pop == genre_score:
            recommended_artists = ['Pop artists']  
        elif rb == genre_score:
            recommended_artists = ['R&B artists']  
        elif rap_hiphop == genre_score:
            recommended_artists = ['Rap/Hip-hop artists']  

        return render(request, 'blog/results.html', {'genre_score': recommended_artists})
    else:
        return render(request, 'blog/music_quiz.html')
