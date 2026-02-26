def test_get_activities(client):
    r = client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)


def test_signup_and_unregister(client):
    # Pick an existing activity from the current dataset
    r = client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert data
    activity = next(iter(data.keys()))

    email = "test@example.com"
    r = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r.status_code == 200

    r = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert r.status_code == 200


def test_root_redirect(client):
    r = client.get("/", follow_redirects=False)
    assert r.status_code in (301, 302, 307, 308)
    loc = r.headers.get("location", "")
    assert loc.endswith("/static/index.html")
