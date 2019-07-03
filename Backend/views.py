from django.shortcuts import render_to_response , render
from django.http import HttpResponse
from django.template import RequestContext
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Authentication,NoteApp,Notes
from rest_framework.views import APIView
from .serializer import AuthSerializer,NoteSerializer
import copy
import json
# Create your views here.
def index(request):
    return HttpResponse("Jai Shri Ram")

class registerUser(APIView):
    queryset = Authentication.objects.all()
    serializer_class = AuthSerializer
    '''Primary class for the purpose to register the user on the database. This specific class deals with adding the username and password on the Authentication
    collection. Password should be encrypted by using suitable encrypting algorithm like SSH256 before saving the value.'''
    def post(self,request):
        authUser = Authentication.objects.filter(username = request.GET['username'])
        authEmail = Authentication.objects.filter(username = request.GET['email'])
        if(set(authUser) == set(Authentication.objects.none()) and set(authEmail)==set(Authentication.objects.none())):
            auth = Authentication()
            auth.username = request.GET['username']
            auth.password = request.GET['password']
            auth.name = request.GET['name']
            auth.email =request.GET['email']
            auth.save()
            return HttpResponse("success")
        else:
            return HttpResponse("exist")

class changePassword(APIView):
    queryset = Authentication.objects.all()
    serializer_class = AuthSerializer
    '''This class is used to change the password of user\'s password. Developer needs to pass the data using 3 variables {"currentPass","newPass","renewPass"}
        This class uses POST method and deals with all the exceptional cases that may arrive.'''
    
    def post(self,request):
        Auth = Authentication.objects.get(username = request.GET["username"])
        if request.GET["email"] == "" and request.GET["currentPass"] != "": 
            password = Authentication.objects.get(username = request.GET["username"]).password
            if request.GET["currentPass"] == request.GET["renewPass"] or request.GET["newPass"] == request.GET["currentPass"]:
                return HttpResponse("Old and current password same")
            elif password == request.GET["currentPass"]:
                if request.GET["newPass"] == request.GET["renewPass"]:
                    Auth.password = request.GET["newPass"]
                    Auth.save()
                    return HttpResponse("Password changed")
                else:
                    return HttpResponse("Both of the new passwords are not the same")
            else:
                return HttpResponse("Invalid current password entered")
        elif request.GET["email"] != "" and request.GET["password"] != "":
            password = Authentication.objects.get(username = request.GET["username"]).password
            if password == request.GET["password"]:
                Auth.email = request.GET["email"]
                Auth.save()
                if request.GET["email"] == Authentication.objects.get(username = request.GET["username"]).email:
                    return HttpResponse("Email is same as before.")
                return HttpResponse("Email changed")
            else:
                HttpResponse("Invalid current password entered")
        else:
            HttpResponse("Failed to make changes")
            #Function to change the email id of the user.

class deleteUser(APIView):
    '''This class is solely made for testing purpose and can be used in deployement if and only if the application wants to allow the user to permanently
    delete his account.'''
    queryset = Authentication.objects.all()
    serializer_class = AuthSerializer

    def post(self,request):

        Auth = Authentication.objects.get(username = request.GET['username'])
        Auth.delete()
        Auth.save()
        print("User's account removed")
        return HttpResponse("User's account removed")  

class SignIn(APIView):
    queryset = Authentication.objects.all()
    serializer_class = AuthSerializer
    '''This class deals with the authentication part. If the password passed by the user matches from the record of our database, user is given a valid token
    else, Invalid username or password is shown/displayed as a message.'''

    def post(self,request):
        if request.GET['password'] == Authentication.objects.get(username = request.GET['username']).password:
            return HttpResponse("success") 
        else:
            return HttpResponse("invalid")
    
class fetchInfo(APIView):
    queryset = Authentication.objects.all()
    serializer_class = AuthSerializer

    def post(self,request):
        print(str(Authentication.objects.get(username = request.GET['username']).name))
        if request.GET['password'] == Authentication.objects.get(username = request.GET['username']).password:
            if request.GET['email']!="" and request.GET['name']!="":
                return HttpResponse(Authentication.objects.get(username = request.GET['username']).email+"/"+Authentication.objects.get(username = request.GET['username']).name)
            else:
                return HttpResponse("invalid query")
        else:
            return HttpResponse("invalid credentials")

'''--------------------------------------------------- Defining class for notes application-----------------------------------------------------------------'''

class viewNotes(APIView):
    queryset = NoteApp.objects.all()
    serializer_class = NoteSerializer

    def post(self,request):
        
        if(NoteApp.objects.filter(username = request.GET["username"]).exists()):
            noteVar = NoteApp.objects.get(username = request.GET["username"])
            note = noteVar.notesApp
            l = []
            for i in range(len(note)):
                l.append({"notesTitle": note[i].notesTitle,"notesDesc":note[i].notesDesc})
            l.reverse()
            return HttpResponse(json.dumps(l))
        else:
            return HttpResponse("fail")

class makeNotes(APIView):
    queryset = NoteApp.objects.all()
    serializer = NoteSerializer

    def post(self,request):
        if(NoteApp.objects.filter(username = request.GET["username"]).exists()):
            noteVar = NoteApp.objects.get(username = request.GET['username'])
        else:
            noteVar = NoteApp()
            noteVar.username = request.GET["username"]
        note = noteVar.notesApp
        obj = Notes()
        obj.notesTitle = request.GET["notesTitle"]
        obj.notesDesc = request.GET["notesDesc"]
        note.append(obj)
        noteVar.save()
        return HttpResponse("success")
        
class modifyNote(APIView):
    queryset = NoteApp.objects.all()
    serializer = NoteSerializer

    def post(self,request):
        if(NoteApp.objects.filter(username = request.GET["username"]).exists()):
            noteVar = NoteApp.objects.get(username = request.GET["username"])
            note = noteVar.notesApp
            note.reverse()
            index = int(request.GET["index"])
            if(request.GET["action"]=="modify"):
                if(index>=len(note)):
                    return HttpResponse("fail")
                else:
                    note[index].notesTitle = request.GET["notesTitle"]
                    note[index].notesDesc = request.GET["notesDesc"]
                    note.reverse()
                    noteVar.save()
                    return HttpResponse("modified")
            elif(request.GET["action"]=="delete"):
                if(index>=len(note)):
                    return HttpResponse("fail")
                else:
                    note.pop(index)
                    note.reverse()
                    noteVar.save()
                    return HttpResponse("deleted")
        else:
            return HttpResponse("fail")



            
    
