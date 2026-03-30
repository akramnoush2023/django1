import ssl
from django.core.mail.backends.smtp import EmailBackend

class UnsafeEmailBackend(EmailBackend):
    def ssl_context(self):
        # Create a default context and disable strict verification
        context = super().ssl_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context
