import functools
import os
import shutil
import subprocess
from uranium import current_build, task_requires

current_build.packages.install("uranium-plus[vscode]")
import uranium_plus

current_build.config.update(
    {
        "uranium-plus": {
            "module": "recruitment_portal_service",
            "publish": {"additional_args": ["--release"]},
            "test": {
                "packages": ["pytest-xdist"]
            },
        }
    }
)

uranium_plus.bootstrap(current_build)

@current_build.task
def migrate(build):
    # using subprocess.call as we don't want to
    # error out if the container is not running.
    subprocess.call(["./.venv/bin/python", "manage.py", "makemigrations"])
    subprocess.call(["./.venv/bin/python", "manage.py", "migrate"])

current_build.tasks.append("main", "migrate")


def ensure_main_ran(fn):

    @functools.wraps(fn)
    def wrapped(build):
        if not build.history.get("main_ran"):
            build.run_task("main")
        build.history["main_ran"] = True
        fn(build)

    return wrapped


def dev(build):
    """ run the application in development mode. """
    subprocess.call(["./.venv/bin/python", "manage.py", "runserver"])

build.task(dev)
