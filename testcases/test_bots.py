import pytest
from _pytest.fixtures import SubRequest
@pytest.fixture
def sth(request:SubRequest):
    yield
    outcome = request.node.rep_call.outcome
    if outcome == 'failed':
        print('用例失败')
    elif outcome == 'passed':
        print('用例成功')

class TestClass(sth):
    def test_login(self):
        assert 1 == 1
