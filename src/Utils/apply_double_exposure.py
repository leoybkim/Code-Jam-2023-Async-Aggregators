import io

from PIL import Image
from PyQt6.QtCore import QBuffer
from PyQt6.QtGui import QImage

from lib.double_exposure.double_exposure import create_double_exposure


def apply_double_exposure(img1, img2, slider_value):
    """
    Apply double exposure to an image

    :param img1:
    :param img2:
    :param slider_value:
    :return:
    """

    img1_path = str(img1)
    img1 = Image.open(img1_path)

    # Get img2 from path and load as Image
    img2_path = str(img2[0])
    img2 = Image.open(img2_path)

    # Convert slider value to float between 0 and 1
    slider_value = slider_value / 100

    # Apply double exposure
    pil_img = create_double_exposure(img1, img2, slider_value)

    # Convert PIL Image to QPixMap
    qimage = QImage(pil_img.tobytes(), pil_img.width, pil_img.height, QImage.Format.Format_RGB888)
    return qimage


def qimage_to_pil_image(qimage: QImage) -> Image:
    """Converts a PyQt QImage to a PIL Image."""
    buffer = QBuffer()
    buffer.open(QBuffer.OpenModeFlag.ReadWrite)
    qimage.save(buffer, "PNG")
    pil_im = Image.open(io.BytesIO(bytes(buffer.data())))
    return pil_im