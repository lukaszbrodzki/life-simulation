import yaml


class Config:
    @staticmethod
    def get_settings(settings: str) -> int | float | str:
        with open('config/config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)

        settings_split = settings.split(".")

        setting = config

        for setting_name in settings_split:
            setting = setting[setting_name]

        return setting
