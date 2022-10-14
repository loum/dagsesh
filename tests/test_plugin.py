""":module:`common_airflow_pytest.plugin` unit test cases.
"""
import airflow.models


def test_working_dir(working_dir):
    """Test the "working_dir" fixture.
    """
    msg = '"working_dir" fixture should provide string type'
    assert isinstance(working_dir, str), msg


def test_dagbag(dagbag):
    """Test the "dagbag" fixture.
    """
    msg = '"dagbag" fixture should provide'
    assert isinstance(dagbag, airflow.models.DagBag), msg
