from vision.ocr.tesseract_ocr import ocr_image
from vision.product.product_info import extract_product_info
from vision.compliance.compliance_checker import check_compliance
def run_vision_pipeline(path):
 text=ocr_image(path); info=extract_product_info(text); return {'ocr_text':text,'product_info':info,'compliance':check_compliance(info)}
