from decouple import Config, RepositoryEnv
from os.path import join
from main_app.settings import BASE_DIR

test_config = Config(RepositoryEnv(
    join(BASE_DIR, 'main_app/tests/configs/test.env')))
