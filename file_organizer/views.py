from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .models import FileUploadModels
from .forms import FileUploadForm

def page(request):
    form = FileUploadForm()
    return render(request, "index.html", {"form": form})

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        form = FileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            for line in file_obj:
                date = line.decode("utf-8").strip()
                tipo = date[0]
                data = date[1:9]
                valor = int(date[10:19])/100
                cpf = date[19:30]
                cartao = date[30:42]
                hora = date[42:48]
                dono_da_loja = date[48:62]
                nome_loja = date[62:81]
                saveFile = FileUploadModels.objects.create(tipo=tipo, data=data, valor=valor, cpf=cpf, cartao=cartao, hora=hora, dono_da_loja=dono_da_loja, nome_loja=nome_loja)
            saveFile.save()
            print("File Upload")
            return Response(status=status.HTTP_201_CREATED)
        else:
            form = FileUploadForm()
            
        return render(request, "index.html", {"form": form})

                  
        