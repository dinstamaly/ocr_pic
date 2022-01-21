import pytesseract
import mimetypes
from django.http.response import HttpResponse
from pathlib import Path
from django.views.generic import FormView
from .forms import *
from django.views.decorators.csrf import csrf_exempt

try:
    from PIL import Image
except:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class HomeView(FormView):
    form_class = UploadForm
    template_name = 'pic/index.html'
    success_url = '/'

    def form_valid(self, form):
        upload = self.request.FILES['file']
        print(type(pytesseract.image_to_string(Image.open(upload))))  # =====> add line
        return super().form_valid(form)


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        # response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload))
        BASE_DIR = Path(__file__).resolve().parent.parent
        filename = 'test.txt'
        filepath = BASE_DIR / 'downloadapp/Files' / filename
        # path = open(filepath, 'r')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(content, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # response_data['content'] = content

        return response
