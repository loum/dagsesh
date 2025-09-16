"""Unit test cases for `dagsesh.lazy`."""

from dagsesh import lazy


def test_lazy_init() -> None:
    """Initialise a dagsesh.lazy.Loader object."""
    # Given a Python module
    local_name = "ospath"

    # and a Python module to lazy import
    module_name = "os.path"

    # when I initialise a dagsesh.utils.Loader
    _ospath = lazy.Loader(local_name, globals(), module_name)

    # I should get an airflow.models instance
    assert isinstance(
        _ospath, lazy.Loader
    ), "Object is not an dagsesh.utils.lazy.Loader instance"

    # and after invocation I can use an os.path function
    assert _ospath.exists(__file__), "os.path.exists() did not return expected value"
