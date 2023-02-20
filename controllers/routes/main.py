from atri_utils import *
from fastapi import Request, Response

from .atri import Atri


def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.TextBox1.styles.display="flex"
    at.TextBox1.styles.color="#696969"
    at.TextBox1.styles.fontFamily="DMSans"
    at.TextBox1.styles.fontWeight="500"
    at.TextBox1.styles.fontSize="18px"
    at.TextBox1.styles.paddingTop="20px"
    at.TextBox1.styles.paddingBottom="30px"
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
   
    pass