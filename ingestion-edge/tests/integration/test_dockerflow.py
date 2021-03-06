# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.

import requests


def test_heartbeat(requests_session: requests.Session, server: str):
    r = requests_session.get(server + "/__heartbeat__")
    r.raise_for_status()
    assert r.json() == {
        "checks": {"check_disk_bytes_free": "ok", "check_queue_size": "ok"},
        "details": {},
        "status": "ok",
    }


def test_lbheartbeat(requests_session: requests.Session, server: str):
    r = requests_session.get(server + "/__lbheartbeat__")
    r.raise_for_status()
    assert r.text == ""


def test_version(requests_session: requests.Session, server: str):
    r = requests_session.get(server + "/__version__")
    r.raise_for_status()
    assert sorted(r.json().keys()) == ["build", "commit", "source", "version"]
