from mypackage import myModule

def test_sq_cube():
    """
    make sure top_n works correctly
    """

    assert myModule.sq_cube([1,2,3,4,6]) == [[4, 8], [16, 64], [36, 216]], 'incorrect'
    assert myModule.sq_cube([9.80665, 3.141, 1.618033988, 2.41421562]) == [[100, 1000], [4, 8], [4, 8]], 'incorrect'
    assert myModule.sq_cube([50/2, 40/3, 30/4, 20/5, 10/6]) == [[64, 512], [16, 64], [4, 8]], 'incorrect'
