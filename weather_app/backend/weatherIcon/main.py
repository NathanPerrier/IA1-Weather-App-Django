from .weather import GetWeatherCode

class GetWeatherIcon:
    def __init__(self):
        pass
    
    def get_icon_name(self):
        ''' returns a weather code '''
        try:
            time_of_day = GetWeatherCode().get_time_of_day()
            return f'{GetWeatherCode().get_weather_code()}-{time_of_day}'
        except Exception as e:
            print('error:', e)
            return None
    
    def get_weather_icon(self):
        try:
            return (f'//images//weatherIcons//animated//{self.get_icon_name()}.svg' if self.does_icon_exist(f'//images//weatherIcons//animated//{self.get_icon_name()}.svg') else self.get_backup_icon())
        except:
            return self.get_backup_icon()
        
    def get_backup_icon(self):
        try:
            return (f'//images//weatherIcons//animated//{GetWeatherCode.get_weather_code()}.svg' if self.does_icon_exist(f'//images//weatherIcons//animated//{GetWeatherCode.get_weather_code()}.svg') else f'//images//weatherIcons//animated//1000-{GetWeatherCode().get_time_of_day()}.svg')
        except:
            return f'//images//weatherIcons//animated//1000-{GetWeatherCode().get_time_of_day()}.svg'
        
    def does_icon_exist(self, icon):
        try:
            with open(f'./weather_app/static/{icon}') as f:
                return True
        except:
            return False