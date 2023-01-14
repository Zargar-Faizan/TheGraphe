import pdb

from django.shortcuts import render, redirect

from task.models import Movie, Moviedesc, Moviedialogue
import string


# Create your views here.
def index(request):
    if request.method == "POST":
        moviename=request.POST.get("movie")
        movieDuration=request.POST.get("duration")
        castname=request.POST.getlist("castname[]")
        gender=request.POST.getlist("gender[]")
        charactername=request.POST.getlist("charactername[]")
        dialogue=request.POST.getlist("dialogue[]")
        starttime=request.POST.getlist("start-time[]")
        endtime=request.POST.getlist("end-time[]")

        if moviename != "" and movieDuration !="" and castname !="" and gender != "" and charactername !="":
            data=Movie(movieName=moviename,movieDuration=movieDuration)
            data.save()
            while ("" in castname):
                castname.remove("")
            while("" in charactername):
                charactername.remove("")
            while ("" in dialogue):
                castname.remove("")
            while ("" in starttime):
                charactername.remove("")
            while ("" in endtime):
                endtime.remove("")
            movieid=Movie.objects.get(movieName=moviename)
            for (castname,gender,charactername) in zip(castname,gender,charactername):
                des=Moviedesc(castname=castname,gender=gender,charactername=charactername,movieid=movieid)
                des.save()

            for (dialogue,starttime,endtime) in zip(dialogue,starttime,endtime):
                dialogue=removepunction(dialogue)
                des = Moviedialogue(dialogue=dialogue,starttime=starttime,endtime=endtime,movieid=movieid)
                des.save()


    return render(request,'index.html')


def removepunction(variable):
    for punctuation in string.punctuation:
        if punctuation != '.':
            while True:
                replaced =  variable.replace(punctuation * 2, punctuation)
                if replaced == variable:
                    break
                variable = replaced
    print(variable)
    return variable