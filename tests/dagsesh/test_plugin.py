"""`dagsesh.plugin` unit test cases."""

from airflow.models import DagBag


def test_dagbag(dagbag: DagBag) -> None:
    """Test the "dagbag" fixture."""
    assert isinstance(dagbag, DagBag), '"dagbag" fixture should provide'
