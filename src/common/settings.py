import tkinter

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "Методы оптимизации"
    debug: bool = True
    ver_tk: str = tkinter.Tcl().eval("info patchlevel")


settings = Settings()

print.settings()