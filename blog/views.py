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
        indie_alt += int(answers.get('indie_alt', 0))
        pop += int(answers.get('pop', 0))
        rap_hiphop += int(answers.get('rap_hiphop', 0))
        rock += int(answers.get('rock', 0))
        rb += int(answers.get('rb', 0))

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
