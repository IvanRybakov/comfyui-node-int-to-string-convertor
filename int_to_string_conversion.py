class IVRIntToString:

    def __init__(self):
        pass
    
    def INPUT_TYPES():
        return {
            "required": {
                "INT_input": ("INT", {
                    "forceInput": True
                }),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "convert"

    def convert(self, INT_input):
        return (str(INT_input),)

NODE_CLASS_MAPPINGS = {
    "Int To String": IVRIntToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Int To String": "Int To String Convertor"
}
