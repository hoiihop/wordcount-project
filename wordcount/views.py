from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}

    for word in wordlist:
        word_dict[word] = wordlist.count(word)

    word_dict_sorted = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    
    result = {'fulltext': fulltext, 
            'count': len(wordlist),
            'word_dict': word_dict_sorted
            }

    return render(request, 'count.html', result)

def about(request):
    title = 'About Us'
    return render(request, 'about.html', {'title': title})