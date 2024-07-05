from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        subject=request.POST['asunto']
        message=request.POST['mensaje'] + " " + request.POST['email']
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["ejemplo.sendmails@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return redirect("gracias.html")

        '''formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["ejemplo.sendmails@gmail.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
        '''
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})