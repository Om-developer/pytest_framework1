import time

import pytest


from test_texpractice.loggs import logclass
from test_texpractice.requirement import Requirement


@pytest.mark.usefixtures("setup")
class Test_login(logclass):

    def test_001(self):
        log = self.getthelogs()
        req = Requirement(self.driver)
        req.input_name()
        log.info("name inputted")
        req.pass_input()
        log.info("pass input successfully")
        req.text_input()
        log.info("text input successfully")
        req.file_upload()
        log.info("file uploaded")
        req.check_box()
        log.info("checkbox done")
        req.radio_btn()
        req.selector()
        req.drop_down()
        req.submit()
        time.sleep(4)
