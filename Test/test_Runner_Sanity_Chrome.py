import unittest
from unittest import TestLoader, TestSuite, TextTestRunner

from Test.test_VerifyElementsAreSortedByAscOrder import TestVerifyElementsAreSortedByAsc
from Test.test_VerifyIfDropdownWithDefaultOptionIsPresented import TestVerifyIfSortByDropdownExist
from Test.test_VerifySixOptionsListedIntoDropdown import TestVerifyIfSixOptionAreVisualized

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestVerifyElementsAreSortedByAsc),
        loader.loadTestsFromTestCase(TestVerifyIfSortByDropdownExist),
        loader.loadTestsFromTestCase(TestVerifyIfSixOptionAreVisualized)
    ))
    runner = TextTestRunner(verbosity=3)
    runner.run(suite)




