# C:\CalmDownSpike\app\__init__.py

# This file can be left empty for now if not used.
from datetime import timedelta
from app import create_app


app = create_app()


def _make_timedelta(value: timedelta | int | None) -> timedelta | None:
    if value is None or isinstance(value, timedelta):
        return value

    return timedelta(seconds=value)


migrate = Migrate(app, db)