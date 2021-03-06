import settings
import json

class Theme:

    def __init__(self, theme = settings.DEFAULT_THEME):
        json_data = open("%s/graphics/themes/%s/config.json" % (settings.APP_ROOT_PATH, theme))
        data = json.load(json_data)

        self.background_animated = data["background_animated"]
        self.organism_scale = data["organism_scale"]
        self.food_scale = data["food_scale"]