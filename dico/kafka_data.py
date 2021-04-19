class KafkaResponse:
    """
    Definition the  word definition response structure
    """

    def __init__(self, word: str, definition: str):
        """
        Constructor
        :param word: we are looking for the definition of this word
        :param definition: the definition of the word
        """
        self.word = word
        self.definition = definition

    def __str__(self):
        return f'definition of {self.word}: {self.definition}'


class KafkaRequest:
    """
    Definition the  word definition request structure
    """

    def __init__(self, word: str, response_topic: str):
        """
        Constructor
        :param word: we are looking for the definition of this word
        :param response_topic: the definition will be sent to topic
        """
        self.word = word
        self.response_topic = response_topic

    def __str__(self):
        return f'search definition of {self.word}'
