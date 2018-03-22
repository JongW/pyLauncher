class UserPath(object):

    def __init__(self, input_value):
        self.input_value = input_value

    def match(self):

        if self.input_value == 'ss':
            return r"C:\Windows\sysnative\SnippingTool.exe"
        else:
            return ""
