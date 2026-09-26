from vision.extraction.is_number import extract_is_numbers
def test_is(): assert '1234' in extract_is_numbers('BIS IS 1234')
