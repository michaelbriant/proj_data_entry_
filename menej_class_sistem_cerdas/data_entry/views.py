from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddressForm, PenggunaForm, ContentForm
from .models import Pengguna
from django.http import JsonResponse
from .models import Content
from django.contrib import messages

def set_data_entry(request):
    form = PenggunaForm()  # Inisialisasi form

    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'data_entry/input_data_1.html', context)

def set_pengguna(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    context = None
    form = PenggunaForm(None)
    email_p = None
    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['email'] = email
            request.session.modified = True
            form.save()
            list_pengguna = Pengguna.objects.all().order_by('-id')
            context = {
                'form': form,
                'list_pengguna' : list_pengguna,
                'email_p' : email_p,
            }
            return render(request, 'data_entry/input_data_1.html',context)
    else:
        context = {
            'form': form,
            'list_pengguna' : list_pengguna,
        }
    return render(request, 'data_entry/input_data_1.html',context)

def view_pengguna(request, id):
    try:
        pengguna = Pengguna.objects.get(pk=id)
        return render(request, 'data_entry/pengguna_detail.html', {'user_id': pengguna.id})
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def get_pengguna_detail_api(request, user_id):
    try:
        pengguna = Pengguna.objects.get(pk=user_id)
        data = {
            'email': pengguna.email,
            'address_1': pengguna.address_1,
            'address_2': pengguna.address_2,
            'city': pengguna.city,
            'state': pengguna.state,
            'zip_code': pengguna.zip_code,
            'tanggal_join': pengguna.tanggal_join.strftime('%Y-%m-%d')
        }
        return JsonResponse(data)
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def set_content(request):
    form = ContentForm(None)
    list_content = Content.objects.all().order_by('-id')  # Ambil semua content terbaru
    context = None
    pengguna = None
    email = None

    if request.session.get('email', None):
        email = request.session.get('email', None)
        pengguna = Pengguna.objects.filter(email=email).first()
        if pengguna:
            initial_data = {'author': pengguna}
            form = ContentForm(initial=initial_data)

    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            # Setelah save, refresh list content
            list_content = Content.objects.all().order_by('-id')
            context = {
                'form': form,
                'list_content': list_content,
                'email': email,
                'pengguna': pengguna,
            }
            return render(request, 'data_entry/create_content.html', context)
    else:
        context = {
            'form': form,
            'list_content': list_content,
            'email': email,
            'pengguna': pengguna,
        }
    return render(request, 'data_entry/create_content.html', context)

def search_pengguna_by_state(request):
    state = request.GET.get('state')  # Ambil parameter 'state' dari URL
    if state:
        pengguna_list = Pengguna.objects.filter(state__icontains=state)
    else:
        pengguna_list = Pengguna.objects.all()

    data = []
    for pengguna in pengguna_list:
        data.append({
            'id': pengguna.id,
            'email': pengguna.email,
            'state': pengguna.state,
            'city': pengguna.city,
            'tanggal_join': pengguna.tanggal_join.strftime('%Y-%m-%d')
        })

    return JsonResponse(data, safe=False)

def update_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    form = PenggunaForm(instance=pengguna)

    if request.method == "POST":
        form = PenggunaForm(request.POST, instance=pengguna)
        if form.is_valid():
            form.save()
            return redirect('data_entry:set_pengguna')  

    context = {
        'form': form,
        'pengguna': pengguna,
    }
    return render(request, 'data_entry/edit_pengguna.html', context)

def delete_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    pengguna.delete()
    messages.success(request, 'Data pengguna berhasil dihapus.')
    return redirect('data_entry:set_pengguna')