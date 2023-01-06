from django.urls import path
from .views import HomeView, ImageElementDetectionView, upload_image, FinalPageView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload_image/', upload_image, name='upload_image'),
    path('image_element_detection/', ImageElementDetectionView.as_view(), name='image_element_detection'),
    path('image_after/', csrf_exempt(ImageElementDetectionView.as_view()), name='image_after'),
    path('final_page/', FinalPageView.as_view(), name='final_page'),    
]
