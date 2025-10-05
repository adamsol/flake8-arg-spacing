
def pytest_make_parametrize_id(config, val, argname):
    # https://github.com/pytest-dev/pytest/issues/3617
    return f' ("{val}") '
