"""download-router-config Config Class."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#


from dataclasses import dataclass
from datetime import datetime
from os import environ as os_environ


@dataclass
class Config:
    """Class for Application variables."""

    def __init__(self):
        """Application Variables."""
        self.app_dict = {
            "author": "Jørn Larsen <jorn.larsen@jotun-utvikling.no>",
            "date": "2024-11-01",
            "desc": "A Python script to capture the running-config of Cisco Routers and Switches.",
            "title": "download_router_config",
            "url": "https://github.com/Jotun-Utvikling-AS/DownloadRouterConfigCisco",
            "version": "4.1.5",
        }

        # Logging Variables
        self.log_dict = {
            "filename": f"""{os_environ.get("LOG_PATH", "./log/")}{self.app_dict["title"]}_{datetime.now().strftime("%Y%m%d")}.log""",
            "level": os_environ.get("LOG_LEVEL", "INFO"),
            "path": os_environ.get("LOG_PATH", "./log/"),
        }
