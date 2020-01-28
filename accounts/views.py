# from django.shortcuts import render
# from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages




# def signin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, 'You are logged in')
#             return redirect('index')
#     else:
#         form = AuthenticationForm()
#
#     context = {'form': form}
#     return render(request, 'accounts/signup.html', context)
#
# def signout(request):
#     logout(request)
#     messages.success(request, 'You are logged out')
#     return redirect('index')
