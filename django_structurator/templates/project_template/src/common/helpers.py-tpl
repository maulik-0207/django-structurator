import logging
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

logger = logging.getLogger("django")

# use like this: from common.helpers import send_email
def send_email(subject: str, ctx: dict[str,any], template_path: str, recipient_list: list[str], attachment_list: list[dict] = []) -> int:
    try:
        email_from = settings.EMAIL_HOST_USER
        html_message = render_to_string(template_name=template_path, context=ctx)
        plain_message = strip_tags(html_message)
        
        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=email_from,
            to=recipient_list,
        )
        message.attach_alternative(html_message, 'text/html')

        # Attach any files if provided
        for attachment in attachment_list:
            if attachment.get("filename") and attachment.get("content") and attachment.get("mimetype"): 
                message.attach(
                    filename=attachment.get("filename"),
                    content=attachment.get("content"),
                    mimetype=attachment.get("mimetype")
                )

        # Send the email and return the result
        result = message.send()
        return result  # Returns the number of successfully sent emails
    except Exception as e:
        logger.error(f"Error while sending email (Sub: {subject}, template: {template_path}, Recipient List: {recipient_list}): {e}", exc_info=True)
        return 0
