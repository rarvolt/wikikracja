# django-registration specific settings
REGISTRATION_HMAC = False

if REGISTRATION_HMAC:
    ACCOUNT_ACTIVATION_DAYS = 7
    # Settings for mailing system
    EMAIL_HOST = ''
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
