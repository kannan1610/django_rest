from rest_framework import generics
from .models import Enquiry
from .serializers import EnquirySerializer
from django.core.mail import send_mail
from django.conf import settings

class EnquiryListCreate(generics.ListCreateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

    def perform_create(self, serializer):
        enquiry = serializer.save()
        subject = 'Enquiry Confirmation'
        message = f'Thank you for your enquiry, your name:{enquiry.username}. your fees:{enquiry.course} discount{enquiry.scheme} We have received your enquiry and will get back to you soon.'
        recipient_list = [enquiry.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

class EnquiryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer


# from rest_framework import generics
# from .models import Enquiry
# from .serializers import EnquirySerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.core.mail import send_mail
# from django.conf import settings

# class EnquiryListCreate(generics.ListCreateAPIView):
#     queryset = Enquiry.objects.all()
#     serializer_class = EnquirySerializer
    
# def perform_create(self, serializer):
#     enquiry = serializer.save()
#     subject = 'Enquiry Confirmation'
#     message = f'Thank you for your enquiry, {enquiry.name}. We have received your enquiry and will get back to you soon.'
#     recipient_list = [enquiry.email]
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

# class EnquiryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Enquiry.objects.all()
#     serializer_class = EnquirySerializer




   







# views.py
# from rest_framework import generics
# from .models import Enquiry
# from .serializers import EnquirySerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# class EnquiryListCreate(generics.ListCreateAPIView):
#     queryset = Enquiry.objects.all()
#     serializer_class = EnquirySerializer



# @csrf_exempt
# def enquiry_view(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             # Process the data here
#             return JsonResponse({'message': 'Enquiry submitted successfully'})
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     return JsonResponse({'error': 'Invalid method'}, status=405)
