class Utils:
    @staticmethod
    def clean(text):
        return [item.strip() for item in text.split(",")]

text=" water,  milk,  ginger,honey "
print(Utils.clean(text)) #can be called without creating object 
