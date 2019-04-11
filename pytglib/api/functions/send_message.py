

from ..utils import Object


class SendMessage(Object):
    """
    Sends a message. Returns the sent message 

    Attributes:
        ID (:obj:`str`): ``SendMessage``

    Args:
        chat_id (:obj:`int`):
            Target chat 
        reply_to_message_id (:obj:`int`):
            Identifier of the message to reply to or 0
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the messageNot supported in secret chats 
        from_background (:obj:`bool`):
            Pass true if the message is sent from the background
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            Markup for replying to the message; for bots only 
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sent

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendMessage"

    def __init__(self, chat_id, reply_to_message_id, disable_notification, from_background, reply_markup, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.disable_notification = disable_notification  # bool
        self.from_background = from_background  # bool
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "SendMessage":
        chat_id = q.get('chat_id')
        reply_to_message_id = q.get('reply_to_message_id')
        disable_notification = q.get('disable_notification')
        from_background = q.get('from_background')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return SendMessage(chat_id, reply_to_message_id, disable_notification, from_background, reply_markup, input_message_content)
