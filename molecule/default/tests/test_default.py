"""Role testing files using testinfra."""

def test_user(host):
    u = host.user("node-exporter")
    assert u.exists

def test_group(host):
    g = host.group("node-exporter")
    assert g.exists

def test_node_exporter_service(host):
    s = host.service("node_exporter")
    assert s.is_enabled
    assert s.is_running

def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9100")
    assert s.is_listening