def set_user(request):
    return {
        "user": request.user,
    }
