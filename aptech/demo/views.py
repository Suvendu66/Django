from django.shortcuts import render

# Create your views here.
def index(request):
    # context={
    #     "firstname":"Aptech"
    # }
    # return render(request,'index.html',context)
    data=[
        {
            "course":'python',
            "duration":'2 month'
        },
        {
            "course":'java',
            "duration":'3 month'
        }
    ]
    context ={
                'data':data
             }
    return render(request,'index.html',context)