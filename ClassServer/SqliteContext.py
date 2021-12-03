from Interfase.Context import Context
from ClassServer.Сonfiguration import Configuration


class SqliteContext(Context):
    def create_context(self):

        data_base_config = Configuration("ApplicationConfiguration").load().data_base

        if not data_base_config.name_database or not data_base_config.name_database.strip():
            raise Exception("Необходимо указать файл базы данных.")

        connect_database = f'sqlite:///{data_base_config.default_dir_database}//' \
                           f'{data_base_config.name_database.strip()}?check_same_thread=False'
        return connect_database
