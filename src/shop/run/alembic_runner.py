import sys

from alembic.config import CommandLine, Config

from shop.adapters import database, log


class Settings:
    db = database.DBSettings()
    alembic = database.AlembicSettings()


class Logger:
    log.configure(Settings.db.LOGGING_CONFIG)


def make_config():
    config = Config()
    config.set_main_option(
        'script_location', Settings.alembic.ALEMBIC_SCRIPT_LOCATION
    )
    config.set_main_option(
        'version_locations', Settings.alembic.ALEMBIC_VERSION_LOCATIONS
    )
    config.set_main_option('sqlalchemy.url', Settings.db.DB_URL)
    config.set_main_option(
        'file_template', Settings.alembic.ALEMBIC_MIGRATION_FILENAME_TEMPLATE
    )
    config.set_main_option('timezone', 'UTC')

    return config


def run_cmd(*args):
    log.configure(Settings.db.LOGGING_CONFIG)

    cli = CommandLine()
    cli.run_cmd(make_config(), cli.parser.parse_args(args))


if __name__ == '__main__':
    run_cmd(*sys.argv[1:])
