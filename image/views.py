from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from .models import Image
import os
import base64
from .utils import get_coordinates, get_coordinates_for_bounding_box




class HomeView(TemplateView):
    template_name = 'upload_image.html'
    
    # upload image to database
def upload_image(request):
    if request.method == 'POST':
        try:
            image_before = request.FILES['image_before']
            image = Image(image_before=image_before)
            image.save()
            return redirect(f'/image_element_detection/?id={image.id}')
        except:
            return redirect('/')    
    

    
class ImageElementDetectionView(TemplateView):
    template_name = 'image_element_detection.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_data = self.request.GET
        if 'id' in get_data:
            id = get_data['id']
            image_to_process = Image.objects.get(id=id)
            image_path = os.path.join('media', str(image_to_process.image_before))
            coordinates = get_coordinates(image_path)
            
            with open('media/images/processings/' + id + '.txt', 'w') as f:
                for coordinate in coordinates:
                    f.write(str(coordinate) + '\n')
            
            list_of_coordinates = get_coordinates_for_bounding_box('media/images/processings/' + id + '.txt')
            sample_images = []
            for file in os.listdir('media/images/samples'):
                sample_images.append(str('/media/images/samples/' + file))
                
            context['sample'] = ','.join(sample_images)
            context['coordinates'] = list_of_coordinates
            context['image'] = image_to_process.image_before.url
            context['url'] = f'/image_after/?id={id}'
            context['final_url'] = f'/final_page/?id={id}'
        else:
            context['coordinates'] = None
            context['image'] = None
            context['url'] = None
            context['final_url'] = None
        return context
    
    def post(self, request, *args, **kwargs):
        get_data = self.request.GET
        if 'id' in get_data:
            id = get_data['id']
            image_to_process = Image.objects.get(id=id)
            string = request.POST['image_after']
            string = string.replace('data:image/png;base64,', '').replace('="', '')
            if not os.path.exists('media/images/after'):
                os.makedirs('media/images/after')
            with open('media/images/after/' + id + '.png', 'wb') as f:
                f.write(base64.decodebytes(string.encode()))
            image_to_process.image_after = 'images/after/' + id + '.png'
            image_to_process.save()
        
        return redirect(f'/image_after/?id={id}')
    

class FinalPageView(TemplateView):
    template_name = 'final_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_data = self.request.GET
        if 'id' in get_data:
            id = get_data['id']
            image_to_process = Image.objects.get(id=id)
            context['image'] = image_to_process.image_after.url
        else:
            context['image'] = None
        return context