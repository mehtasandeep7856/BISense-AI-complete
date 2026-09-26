from vision.compliance.compliance_checker import check_compliance
def test_comp(): assert check_compliance({'is_numbers':[],'licence_numbers':[]})['overall_status']=='unavailable'
