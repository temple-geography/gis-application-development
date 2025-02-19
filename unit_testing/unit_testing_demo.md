The test files in this directory are prepended with `~` so that they are not discovered by **pytest** until we want them to be.

1. Run `is_palindrome0.py`.
2. Break code, rerun `is_palindrome0.py`.
3. Replace main with `def test_is_palindrome():`.
4. Put test in separate file `test_is_palindrome.py`.
5. Demo `test_shapes0.py`.
5. Show fixtures in `test_shapes.py`. Note that fixtures can be put in separate files for use in other tests.

Paremtrization (not demonstrated): [With pytest, what's the benefit of using parameters instead of multiple assert statements for a test?](https://stackoverflow.com/questions/66481583/with-pytest-whats-the-benefit-of-using-parameters-instead-of-multiple-assert-s)
