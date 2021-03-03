from screens.authorize import ScreenAuthorize # YayMuffins - We import the function ScreenAuthorize from the module in <app_root>/screens/authorize.py
from ui.ui import UserInterface # YayMuffins - We import the function "UserInterface" from the module in <app_root>/ui/ui.py
import config # YayMuffins - We import the config file from <app_root>/config.py

if __name__ == "__main__":
    firstScreen = ScreenAuthorize()
    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
                       config.SOUND)

    while (True):
        ui.tick()
