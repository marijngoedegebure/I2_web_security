def unsafe_user(request):
    """
    Returns context variables required by apps that use Django's authentication
    system.

    If there is no 'user' attribute in the request, uses AnonymousUser (from
    django.contrib.auth).
    """
    if hasattr(request, 'unsafe_user'):
        unsafe_user = request.unsafe_user
    else:
        unsafe_user = None

    return {
        'unsafe_user': unsafe_user,
    }
