from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cpu")

def index(request):
    return render(request, 'stablediffusion/index.html')

def prompt(request):
    prompt = request.GET.get('prompt', '')
    image = pipe(prompt).images[0]  # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)
    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG")
    return response
