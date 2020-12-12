from django.http import HttpResponse

def helloworldfunc(request):
  responseobject = HttpResponse('hello world')
  return responseobject

  # requestオブジェクトを受け取りresponseオブジェクトを返す