from datetime import datetime


class GetDateTime:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "format": ("STRING", {"default": "%Y-%m-%d"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "0nedark/utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def execute(self, format):
        return (datetime.now().strftime(format),)


NODE_CLASS_MAPPINGS = {
    "0nedark_GetDateTime": GetDateTime,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "0nedark_GetDateTime": "Get DateTime",
}
