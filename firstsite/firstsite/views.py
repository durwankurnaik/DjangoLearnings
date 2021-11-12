# Made by Durwankur
from django.http import HttpResponse
from django.shortcuts import render


# Some time-pass content
# def index(request):
#     return HttpResponse('''
# <ul>
#     <li><h1>Spring</h1></li>
#     <h3>
#         <ul>
#             <li>
#                 <a href="https://www.youtube.com/playlist?list=PL0zysOflRCekeiERASkpi-crREVensZGS">
#                 Spring Framework Tutorial
#                 </a>
#             </li>
#             <li>
#                 <a href="https://www.youtube.com/playlist?list=PL0zysOflRCelAb51IrexpUSeB0dpr9p6g">
#                 Spring MVC Tutorials
#                 </a>
#             </li>
#             <li>
#                 <a href="https://www.youtube.com/playlist?list=PL0zysOflRCelmjxj-g4jLr3WKraSU_e8q">
#                     Spring Boot Tutorial
#                 </a>
#             </li>
#         </ul>
#         <li><h1>Django</h1></li>
#         <ul>
#             <li>
#                 <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">
#                     Django Framework Tutorial
#                 </a>
#             </li>
#         </ul>
#     </h3>
# </ul>
# ''')
# By the use of above method "HttpResponse()", the django decodes html given within the python file

# Text utils website
def index(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = str(request.GET.get('text', 'default'))
    removepunc = request.GET.get('removepunc', 'off')
    capsall = request.GET.get('capfirst', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    punc_remove = ""
    nl_remove = ""
    space_remove = ""

    params = {}

    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                punc_remove += char
        params['puncremoved'] = punc_remove

    if newlineremove == 'on':
        for char in djtext:
            if char != '\n':
                nl_remove += char
        params['nlremoved'] = nl_remove

    if spaceremove == 'on':
        for char in djtext:
            if char != ' ':
                space_remove += char
        params['spaceremoved'] = space_remove

    if capsall == 'on':
        caps_all = djtext.upper()
        params['capsall'] = caps_all

    if charcount == 'on':
        char_count = len(djtext)
        params['charcount'] = char_count

    return render(request, 'analyse.html', params)
