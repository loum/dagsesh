"""`dagsesh.plugin` unit test cases.

"""
from typing import Text

from airflow.models import DagBag


def test_working_dir(working_dir: Text) -> None:
    """Test the "working_dir" fixture."""
    msg = '"working_dir" fixture should provide string type'
    assert isinstance(working_dir, str), msg


def test_dagbag(dagbag: DagBag) -> None:
    """Test the "dagbag" fixture."""
    msg = '"dagbag" fixture should provide'
    assert isinstance(dagbag, DagBag), msg
