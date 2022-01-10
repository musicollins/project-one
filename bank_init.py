from UI.menu import UI
from data_source.data_source import DataSourceText

def app_start(_ui: UI):
    ui = _ui
    ui.menu()
    



if __name__ == "__main__":
    app_start(_ui = UI())


