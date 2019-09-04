import logging
import json
import os

from config.auth import OAuth2
from config.spring import ConfigClient

import attr

from glom import glom


logging.getLogger(__name__).addHandler(logging.NullHandler())


@attr.s(slots=True)
class CF:

    _vcap_services = json.loads(os.getenv('VCAP_SERVICES'))
    uri = attr.ib(
        type=str,
        default=glom(
            _vcap_services,
            'p-config-server.0.credentials.uri'
        )
    )
    oauth2 = attr.ib(
        type=OAuth2,
        default=OAuth2(
            access_token_uri=glom(
                _vcap_services,
                'p-config-server.0.credentials.access_token_uri'
            ),
            client_id=glom(
                _vcap_services,
                'p-config-server.0.credentials.client_id'
            ),
            client_secret=glom(
                _vcap_services,
                'p-config-server.0.credentials.client_secret'
            )
        )
    )
    client = attr.ib(
        type=ConfigClient,
        default=ConfigClient()
    )

    def __attrs_post_init__(self):
        self.oauth2.configure()
        if self.client.address == 'http://localhost:8888/configuration':
            self.client.address = self.uri

    def get_config(self):
        header = {f"Bearer {self.oauth2.token}"}
        return self.client.get_config(header)
