from api.v1.films.dependencies.utils import UNSAFE_METHODS


class TestUnsafeMethods:
    def test_doest_contain_safe_methods(self) -> None:
        safe_methods = {"HEAD", "GET", "OPTIONS"}
        assert not UNSAFE_METHODS & safe_methods

    def test_test_all_methods_are_upper(self) -> None:
        assert all(method.isupper() for method in UNSAFE_METHODS)
